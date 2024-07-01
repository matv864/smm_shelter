FROM node:22 as build

WORKDIR /frontend

COPY . .

RUN npm install && npm run build && rm -rf node_module