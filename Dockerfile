FROM ubuntu:latest

RUN mkdir /mydata
COPY test.sh /mydata/test.sh

ENTRYPOINT /mydata/test.sh