# I target to japanese in this project. 
# I just want to make database of flower name from my own book.
# このプロジェクトでは、日本語にだけ対応すればいいと思ってます。
# I can not upload my sample photo because I dont have license to that documents.
# please use your own images.

import os
import cv2
import pytesseract
import numpy as np

def load_from_file():
    # Tesseractの実行ファイルのパスを指定
    pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

    # TESSDATA_PREFIX環境変数を設定
    os.environ['TESSDATA_PREFIX'] = '/opt/homebrew/share/tessdata/'


    # 画像を読み込む
    _image = cv2.imread('private_sample04.jpg')
    _template = cv2.imread("private_target_sample1.jpg")
    return _image, _template

def prepare_common_image_processing(image):
    # グレースケールに変換
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray Image', gray_image)

    # ノイズを除去するために、画像をしきい値処理する
    _, thresh_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh_image

# 空行を削除する
def remove_blank_lines(text):
    lines = text.split('\n')
    non_empty_lines = [line for line in lines if line.strip() != '']
    return '\n'.join(non_empty_lines)

# 文字列から (　や [ の後ろの文字列を削除した
def remove_after_characters(text):
    import re
    modified_text = re.sub(r'\(.*', '', text)
    modified_text = re.sub(r'\[.*', '', modified_text)
    return modified_text

#  ここより下がMain 関数に当たる、最初に実行される場所
image, template = load_from_file() # イメージファイルを取得する 

thresh_image = prepare_common_image_processing(image) # 基本的な前処理をする


# 今はここを実験中
contours_image, _ = cv2.findContours(thresh_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
matching_result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.55
locations = np.where(matching_result >= threshold)   # 一致する部分の位置を取得
template_height, template_width = template.shape[:2] # template 画像の大きさを取得
for pt in zip(*locations[::-1]):
    cv2.rectangle(image, pt, (pt[0] + template_width, pt[1] + template_height), (255, 255, 255), -1)

# cv2.imshow('Detected', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Tesseractで画像からテキストを抽出
text = pytesseract.image_to_string(image, lang='jpn')

from string import digits
table = str.maketrans("", "", digits)
non_digits_text = text.translate(table)
non_empty_lines = remove_blank_lines(non_digits_text)
removed_texts = remove_after_characters(non_empty_lines)
non_empty_lines = remove_blank_lines(removed_texts)


print("Extracted Text:")
print(non_empty_lines)
