from backend.db import Base, engine

def create_db_tables():
    """Create database tables if they do not exist."""
    Base.metadata.create_all(bind=engine)


def startup_service():
    """Service to run at startup."""
    create_db_tables()
    