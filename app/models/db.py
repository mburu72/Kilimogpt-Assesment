from sqlmodel import create_engine, SQLModel

sqlite_file_name = "chat_history.db"
engine = create_engine(f"sqlite:///{sqlite_file_name}")

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
