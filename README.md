# Library API - a dockerized FastAPI sample project 📖

The following is a test project that uses FastAPI and SQLAlchemy to develop a backend for a fictional library website. 

It is used as a sample repository for this [Docker tutorial](https://luisgc93.medium.com/docker-for-newbies-24601dfd1e6c) and is also deployed on heroku at: https://book-api-fastapi-project.herokuapp.com/.

## Usage
Start the project containers with the `make start` command. You can then create a user...


````
curl --location --request POST '0.0.0.0:8000/users/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "user123",
    "password": "password"
}'
````

...and login to receive an auth token:
````
curl --location --request POST '0.0.0.0:8000/login/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "user123",
    "password": "password"
}'
````

Response format:

````
{
    "access_token": your token,
    "token_type": "bearer"
}
````

You can then use the other endpoints passing your access token as a request header:

````
curl --location --request POST '0.0.0.0:8000/books/' \
--header 'Authorization: Bearer {your token}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title": "Harry Potter and the Philosopher'\''s Stone",
    "author": "J. K. Rowling"
}'
````

Full API spec can be found at:
https://book-api-fastapi-project.herokuapp.com/docs/

