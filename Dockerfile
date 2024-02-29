FROM python:3.10.12-slim

WORKDIR /workspace

RUN apt-get update && apt-get install -y \
    ffmpeg \
    tesseract-ocr \
    git

RUN pip install git+https://github.com/hc-sc-ocdo-bdpd/file-processing-tools.git


