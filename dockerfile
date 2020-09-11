FROM python:3.6 − alpine
WORKDIR /everis_test
COPY . /everis_test
RUN pip install −r requirements.txt

CMD ["python" , "core.py" , 12254943]