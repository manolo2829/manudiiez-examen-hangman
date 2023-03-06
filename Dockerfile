FROM python:3

RUN git clone https://github.com/manolo2829/manudiiez-examen-hangman.git

WORKDIR /manudiiez-examen-hangman

RUN requirements.txt

CMD ["python3", "-m", "unittest"]