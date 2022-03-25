# Use latest mongodb image
FROM mongo:4.4.6

COPY ./mongodb-config/a-mongo-user-init.sh /docker-entrypoint-initdb.d/a-mongo-user-init.sh
COPY ./mongodb-config/z-mongo-database-init.js /docker-entrypoint-initdb.d/z-mongo-database-init.js

EXPOSE 27017
