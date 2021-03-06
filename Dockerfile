FROM python:3.6
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python tests.py
ENTRYPOINT ["python", "run.py"]