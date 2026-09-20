from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class OfferResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    product_id: int
    marketplace: str
    seller_name: str
    price: Decimal
    seller_rating: float
    url: str