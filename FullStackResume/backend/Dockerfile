# Use Python base image
FROM python:3.11-slim

RUN pip install --no-cache-dir --upgrade pip setuptools

RUN apt-get update && apt-get install -y \
    texlive-latex-base \
    texlive-fonts-recommended \
    texlive-fonts-extra \
    texlive-latex-extra \
    && apt-get clean

WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose Flask default port
EXPOSE 5000

# Command to start the Flask app
CMD ["python", "app.py"]
