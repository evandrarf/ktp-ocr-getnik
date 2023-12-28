FROM python:3.8

RUN apt-get update -y && apt-get install -y tesseract-ocr tesseract-ocr-ind  libtesseract-dev libgl1-mesa-glx 

RUN pip install requests flask Werkzeug opencv-python pytesseract

WORKDIR /app
COPY ./app .

EXPOSE 3000

CMD [ "python", "main.py" ]
