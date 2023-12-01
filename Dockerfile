FROM python:3.10.13-slim-bullseye
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
ENV FLASK_APP wsgi.py
CMD ["flask", "run", "--host=0.0.0.0"]
