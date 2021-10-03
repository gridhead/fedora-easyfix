FROM python:3.9-alpine

COPY . /opt/easyfix/.

LABEL maintainer "khallnayak <mahijmomin@gmail.com>"

WORKDIR /opt/easyfix

RUN pip3 install -r requirements.txt && \
    python3 setup.py install

EXPOSE 9696

ENTRYPOINT ["start-easyfix-server"]

CMD ["-4","-p","9696"]
