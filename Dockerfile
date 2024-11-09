FROM python:3.11-slim

RUN apt-get update
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential python3-venv python3-pip ffmpeg && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt

COPY . /code
WORKDIR /code

ENV ALLOWED_TELEGRAM_USERNAMES=${ALLOWED_TELEGRAM_USERNAMES} \
    BOT_ADMIN_ID=${BOT_ADMIN_ID} \
    NEW_DIALOG_TIMEOUT=${NEW_DIALOG_TIMEOUT} \
    LOG_LEVEL=${LOG_LEVEL} \
    TELEGRAM_TOKEN=${TELEGRAM_TOKEN} \
    OPENAI_API_KEY=${OPENAI_API_KEY} \
    FIREBASE_CREDENTIALS=${FIREBASE_CREDENTIALS} \
    BASE_URL=${BASE_URL}

CMD ["python3", "bot/bot.py"]
