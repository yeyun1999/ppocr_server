from paddleocr import PaddleOCR
from flask import Flask
from base64 import b64decode


# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
ocr = PaddleOCR(use_angle_cls=True, lang="ch",use_gpu=False,cpu_threads=2,enable_mkldnn=True)  # need to run only once to download and load model into memory
# ocr = PaddleOCR(use_angle_cls=True, lang="ch",use_gpu=False)  # need to run only once to download and load model into memory

app = Flask(__name__)

@app.route("/ocr", methods=["POST"])
def ppocr():
    data = request.get_json()
    img = b64decode(data["img"])
    global ocr
    result = ocr.ocr(img, cls=True)
    return result