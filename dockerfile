FROM python:3.8-slim
WORKDIR /everis_test
COPY . /everis_test

RUN pip install -r requirements.txt

CMD ["python","core.py","12254943"]
