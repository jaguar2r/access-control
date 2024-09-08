FROM python:3.10.13-slim-bookworm

ENV TZ=America/Sao_Paulo

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /app

COPY ./requirements.txt .

RUN apt update && apt upgrade -y \
    && apt install tree -y \
    && apt install pip -y \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

RUN pip install gunicorn

COPY . .

EXPOSE 5000

# Definindo o comando de entrada para rodar o Flask com gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app.app:app"]
