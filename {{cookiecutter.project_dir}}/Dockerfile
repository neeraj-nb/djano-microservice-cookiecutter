FROM python:3.11-slim as builder

RUN apt-get update \
  && apt-get install -y --no-install-recommends --no-install-suggests \
  && pip install --no-cache-dir --upgrade pip

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY . .

EXPOSE 8000
COPY entrypoint /entrypoint
RUN chmod +x /entrypoint

COPY start.dev.sh /start.dev.sh
RUN chmod +x /start.dev.sh

COPY start.prod.sh /start.prod.sh
RUN chmod +x /start.prod.sh

RUN adduser --disabled-password --gecos '' django
USER django

# CMD ["gunicorn", "user_service.wsgi:application", "--bind", "0.0.0.0:8000"]
ENTRYPOINT [ "/entrypoint" ]
