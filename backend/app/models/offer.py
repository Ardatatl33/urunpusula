from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, Numeric, String, Float
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Offer(Base):
    __tablename__ = "offers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id"),
        nullable=False,
    )
    marketplace: Mapped[str] = mapped_column(String(100), nullable=False)
    seller_name: Mapped[str] = mapped_column(String(150), nullable=False)
    price: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    seller_rating: Mapped[float] = mapped_column(Float, nullable=False)
    url: Mapped[str] = mapped_column(String(500), nullable=False)