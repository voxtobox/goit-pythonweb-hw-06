import os
from dotenv import load_dotenv
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

# load env variables
load_dotenv()

# get envs from variables
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

url_to_db = f"postgresql://postgres:123123@localhost:5432/postgres"
engine = create_engine(url_to_db)
Session = sessionmaker(bind=engine)
