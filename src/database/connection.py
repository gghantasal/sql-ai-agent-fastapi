# src/database/connection.py
import os
from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine
from src.utils.logger import logger

_db_instance = None # To store the singleton DB connection

def get_db_connection():
    global _db_instance
    if _db_instance is None:
        database_url = os.getenv("DATABASE_URL")
        if not database_url:
            logger.error("DATABASE_URL environment variable not set.")
            raise ValueError("DATABASE_URL environment variable not set.")
        try:
            # LangChain's SQLDatabase expects a SQLAlchemy engine
            # It handles the underlying connection pooling.
            engine = create_engine(database_url)
            _db_instance = SQLDatabase(engine=engine)
            logger.info(f"Successfully connected to database: {_db_instance.dialect}")
        except Exception as e:
            logger.exception(f"Failed to connect to database at {database_url}: {e}")
            raise
    return _db_instance

# Example of how to use it for schema info (optional)
def get_db_schema_info():
    db = get_db_connection()
    # You might want to filter tables or add descriptions here
    # For a small DB, db.get_table_info() is fine.
    # For large DBs, consider fetching schema only for relevant tables
    return db.get_table_info()