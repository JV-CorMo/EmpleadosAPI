FROM python:3.12.9-slim

WORKDIR /code

COPY app/requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app/.env /code/.env
COPY ./app /code/app

# VOLUME /code/app/media


EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]