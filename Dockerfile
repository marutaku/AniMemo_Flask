FROM python:3.5
MAINTAINER Takumi Maruyama

RUN pip3 install pipenv
RUN mkdir code
WORKDIR ./code
COPY . .
RUN pipenv install --system
#RUN pipenv shell

CMD ['python']


