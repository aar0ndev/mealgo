FROM python:3.8
COPY requirements.txt /
RUN pip install -r requirements.txt
COPY src /app
WORKDIR /app
ENV FLASK_APP=/app/app.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
EXPOSE 5000
# RUN pip install inotify
# RUN pip install --upgrade --force-reinstall gunicorn
ENTRYPOINT ["gunicorn", "-k", "flask_sockets.worker", "-b", "0.0.0.0:5000", "--reload", "--max-requests", "1", "app:app"]
#ENTRYPOINT ["python", "app.py"]