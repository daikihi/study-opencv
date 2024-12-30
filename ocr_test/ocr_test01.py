# I target to japanese in this project. 
# I just want to make database of flower name from my own book.
# このプロジェクトでは、日本語にだけ対応すればいいと思ってます。
# I can not upload my sample photo because I dont have license to that documents.
# please use your own images.



import os
import cv2
import pytesseract

def load_from_file():
    # Tesseractの実行ファイルのパスを指定
    pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

    # TESSDATA_PREFIX環境変数を設定
    os.environ['TESSDATA_PREFIX'] = '/opt/homebrew/share/tessdata/'


    # 画像を読み込む
    _image = cv2.imread('private_sample04.jpg')
    return _image

def prepare_common_image_processing(image):
    # グレースケールに変換
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray Image', gray_image)

    # ノイズを除去するために、画像をしきい値処理する
    _, thresh_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh_image


#  ここより下がMain 関数に当たる、最初に実行される場所
image = load_from_file() # イメージファイルを取得する 

thresh_image = prepare_common_image_processing(image) # 基本的な前処理をする


# 今はここを実験中
contours_image, _ = cv2.findContours(thresh_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


# Tesseractで画像からテキストを抽出
text = pytesseract.image_to_string(thresh_image, lang='jpn')

print("Extracted Text:")
print(text)
