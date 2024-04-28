FROM python:3.10.14-slim

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY insurance_system /insurance_system/
WORKDIR /insurance_system

