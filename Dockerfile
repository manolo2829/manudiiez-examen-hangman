FROM python:3

RUN git clone 

WORKDIR /REPO

RUN requirements.txt

CMD ["python3", "-m", "unittest"]