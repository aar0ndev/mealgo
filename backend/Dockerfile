FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV FLASK_APP=/app/index.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
EXPOSE 5000
#ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "index:index"]
ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0"]