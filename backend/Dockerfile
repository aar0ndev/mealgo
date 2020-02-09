FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
ENV FLASK_APP=/app/app.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
EXPOSE 5000
#ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "index:index"]
ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0"]