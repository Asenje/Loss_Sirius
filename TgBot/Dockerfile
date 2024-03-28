FROM python:3.8

RUN pip install telebot transformers trl datasets

COPY bot.py /app/bot.py

WORKDIR /app

CMD ["python", "bot.py"]
