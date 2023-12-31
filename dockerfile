FROM python:3.9

WORKDIR /app

COPY . ./

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "main.py", "--server.port=8080", "--server.address=0.0.0.0"]
