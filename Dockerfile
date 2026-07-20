FROM python:3.12 
ENV TZ=Europe/Moscow
WORKDIR /app
COPY . .
RUN pip install requests
CMD ["python","checker.py"]