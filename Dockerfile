FROM python

WORKDIR /usr/src/app
COPY . .

RUN pip install discord 

CMD ["python", "botzin.py"]
