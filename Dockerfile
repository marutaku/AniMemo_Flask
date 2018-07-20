FROM python:3.5
MAINTAINER Takumi Maruyama

RUN pip3 install pipenv
RUN mkdir code
WORKDIR ./code
RUN echo 'dummy'
COPY . .

RUN set -ex && pipenv install --system --deploy
#RUN pipenv shell

CMD ['python']


