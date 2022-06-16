# pull official base image
FROM node:lts-buster-slim

# set working directory
WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH
RUN npm install -g npm@latest

COPY ./app/package.json .
RUN npm install --silent
RUN npm install react-scripts@3.4.1 -g

COPY ./app /app
