from sqlalchemy import Boolean, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    brand: Mapped[str] = mapped_column(String(100), nullable=False)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    storage_gb: Mapped[int] = mapped_column(Integer, nullable=False)
    ram_gb: Mapped[int] = mapped_column(Integer, nullable=False)
    screen_inches: Mapped[float] = mapped_column(Float, nullable=False)
    battery_mah: Mapped[int] = mapped_column(Integer, nullable=False)
    main_camera_mp: Mapped[int] = mapped_column(Integer, nullable=False)
    has_5g: Mapped[bool] = mapped_column(Boolean, nullable=False)