FROM python:3.12-slim-bookworm

WORKDIR /app
COPY . /app

RUN apt update -y && apt upgrade -y && apt install -y curl && \
    curl -LsSf https://astral.sh/uv/install.sh | sh && \
    apt remove -y curl && apt autoremove -y && apt clean && rm -rf /var/lib/apt/lists/*

ENV PATH="/root/.local/bin:$PATH"

RUN uv pip install --system -r requirements.txt awscli

EXPOSE 8000

CMD ["python", "app.py"]