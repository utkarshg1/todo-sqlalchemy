from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Setup SQLite engine
def get_engine():
    return create_engine('sqlite:///database.db')

# Create a session maker object to use across the app
Session = sessionmaker(bind=get_engine())
