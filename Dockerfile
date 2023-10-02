FROM paddlecloud/paddleocr:2.6-cpu-latest

RUN pip install gunicorn -i http://mirrors.aliyun.com/pypi/simple/
COPY ./ppocr_server.py /home/PaddleOCR/


CMD gunicorn -w 2 "ppocr_server:app"