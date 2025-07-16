FROM python:3.8-slim
WORKDIR /app
COPY . /app

RUN apt update -y && apt install awscli -y

RUN apt-get clean && rm -rf /var/lib/apt/lists/*

COPY artifacts/ /app/artifacts/

RUN pip install -r requirements.txt
CMD ["python3", "application.py"]

