# study-opencv
This project is just my experience to use python and opencv. I am not sure what i will be able to do, now

# まずはやること

```bash 
$ python3 -m venv ./env

# まいかいやること
$ source ./env/bin/activate
# 作業環境ができた

# 一回だけで良い
$ pip install opencv-python
```

# 画像をグレースケールに変換して表示する　: converting and display gray scale image from color based image

source : test1.py

```shell
$ python test1.py

```

# OCR
最初に１度だけ必要

ここでは、前提として、Mac を使っている事とします。Windows の場合は、ちょっとわからないです。

おそらく、Linux なら、ほぼ同じ様にできると思います。（最近Linux 使っていないから正確にはわからないですが）

mac の場合 

もし、ｂhomebrew をインストールしていない場合は、そこからやってみましょう

```shell
$ brew install tesseract
$ brew install tesseract-lang   # 日本語を使うのに必要。英語でいい場合は不要かも？
```


```shell
$ pip install opencv-python   # i already execute this command on gray scale converter
$ pip install pytesseract

```