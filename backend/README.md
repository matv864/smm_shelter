# Overview
backend is API for smm-shelter for messaging with database.

**The two main goals** of the backend are the API, which sends json with pets (including images) and allows administrations to easily access to the database.

## API
The API module is created with fastapi handlers and sqlAlchemy's async requests to the database.

## admin panel
Accessing to database - I implemented this with the sqlAdmin library, which provides a nice interface by connecting the sqlAlchemy's engine and models of the tables. 
To defence from third person, I use aunthefication from this library, and verify the right person by entering the correct login and password (I compare password with the hashed password in env)
In addition, facilitate the use of the databaser, I created custom pages to compress big images in storage with one click and create backups (archieve storage and sql dump) with one click too

## migrations
I also created migrations from Alembic for easy working with the database.

## access to storage
frontend can fetch image by requesting to <domain>/<image_full_path>, which throw nginx walk to storage folder and fetch the required image


## env file
```
# for connecting to postgres
POSTGRES_NAME_SERVICE=smm_shelter-postgres
POSTGRES_DB=pets-service
POSTGRES_USER=
POSTGRES_PASSWORD=

# paths to save backups of database and storage
PATH_TO_SAVE_DUMP=/backup/dump_pets.sql
PATH_TO_SAVE_BACKUP=/backup/storage.zip

# login system of sqlAdmin
ADMIN_USERNAME=
HASHED_PASSWORD=
```