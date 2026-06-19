from app.db.database import engine, Base

# Import models BEFORE create_all()
from app.db.models import User, Customer

Base.metadata.create_all(bind=engine)

print("Database initialized successfully")