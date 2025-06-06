import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:exemplo@localhost:5433/vitivinicultura"
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)
