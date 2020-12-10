FROM python:3.9

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY aoc-solve-bot-discord ./

CMD ["python", "-u", "main.py"]
