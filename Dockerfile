FROM python

WORKDIR /usr/src/app
COPY . .

RUN pip install discord
RUN pip install random2

CMD ["python", "botzin.py"]
