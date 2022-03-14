# Use latest python
FROM node:latest as build

# Set up working directory at /app
WORKDIR /app

COPY ./angular/ /app

RUN npm install
RUN npm run build

FROM nginx:latest

COPY --from=build /app/dist/getting-started /usr/share/nginx/html

# Container setup
EXPOSE 80
