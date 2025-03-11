import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from dotenv import load_dotenv
load_dotenv()


DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_NAME = os.getenv("DATABASE_NAME")

SQLALCHEMY_DATABASE_URI_LOCAL = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
SQLALCHEMY_DATABASE_URI_TEMBO = "postgresql://postgres:w7btnRbeBgfkncQ4@lecherously-rested-halibut.data-1.use1.tembo.io:5432/postgres"

SQLALCHEMY_TRACK_MODIFICATIONS = False