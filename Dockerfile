FROM python:3.10

COPY requirements.txt .

RUN apt update
# RUN apt install dbus-python
# RUN apt install libsystemd
# RUN apt install libsystemd-journal

RUN pip install llama-index
RUN pip install python-dotenv
RUN pip install beautifulsoup4
RUN pip install requests
RUN pip install flask

COPY . .

EXPOSE 5000

CMD ["python3", "app.py", "--host=0.0.0.0", "--port=5000"]