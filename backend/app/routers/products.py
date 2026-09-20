from collections.abc import Generator

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.product import Product
from app.schemas.product import ProductResponse


router = APIRouter(prefix="/products", tags=["Products"])


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.get("", response_model=list[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    statement = select(Product).order_by(Product.id)
    return db.scalars(statement).all()