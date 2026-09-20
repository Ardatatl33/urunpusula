from app.database import Base, engine
from app.models.offer import Offer
from app.models.product import Product

Base.metadata.create_all(bind=engine)

print("Tables created or already existed.")