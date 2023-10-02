FROM paddlecloud/paddleocr:2.6-cpu-latest

RUN pip install gunicorn -i https://mirrors.aliyun.com/pypi/simple/
COPY ./ppocr_server.py /home/PaddleOCR/


CMD gunicorn -w 1 -b 0.0.0.0 "ppocr_server:app"