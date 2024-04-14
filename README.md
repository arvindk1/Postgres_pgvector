# Postgres_pgvector

- ''' .Postgres_pgvector
        │   .env
        │   .gitignore
        │   add_test_data.py
        │   database.ini
        │   docker-compose.yml
        │   init.sql
        │   list_models.py
        │   README.md
        │   requirements.txt
        │   sentence_transformer.py
        │   test
        │   test_search.py
        │   
        └───app
            │   __init__.py
            │   
            ├───db
            │   │   config.py
            │   │   connect.py '''

- Docker Compose configuration for setting up a PostgreSQL database with pgvector extension and custom initialization script.

- The db_config function in the provided code reads database configuration parameters from a specified file using ConfigParser, with the file path provided as filename. It extracts the parameters under a specified section in the configuration file and returns them as a dictionary, raising an exception if the section is not found in the specified file.

