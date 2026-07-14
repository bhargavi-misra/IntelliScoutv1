FROM python:3.11-slim

# Prevent Python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install Linux libraries required by Playwright
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    git \
    libnss3 \
    libatk-bridge2.0-0 \
    libdrm2 \
    libxkbcommon0 \
    libgtk-3-0 \
    libgbm1 \
    libasound2 \
    libxshmfence1 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libx11-xcb1 \
    libxcb1 \
    libxcursor1 \
    libxi6 \
    libxtst6 \
    fonts-liberation \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browser
RUN playwright install chromium
RUN playwright install-deps chromium

# Copy project
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "8000"]