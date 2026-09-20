from decimal import Decimal

from sqlalchemy import select

from app.database import SessionLocal
from app.models.offer import Offer
from app.models.product import Product


def seed_sample_data() -> None:
    session = SessionLocal()

    try:
        product = session.scalar(
            select(Product).where(
                Product.brand == "Apple",
                Product.name == "iPhone 17 Pro",
                Product.storage_gb == 256,
            )
        )

        if product is None:
            product = Product(
                brand="Apple",
                name="iPhone 17 Pro",
                storage_gb=256,
                ram_gb=12,
                screen_inches=6.3,
                battery_mah=3500,
                main_camera_mp=48,
                has_5g=True,
            )
            session.add(product)
            session.flush()

        offer = session.scalar(
            select(Offer).where(
                Offer.product_id == product.id,
                Offer.marketplace == "Trendyol",
                Offer.seller_name == "Örnek Teknoloji Mağazası",
            )
        )

        if offer is None:
            offer = Offer(
                product_id=product.id,
                marketplace="Trendyol",
                seller_name="Örnek Teknoloji Mağazası",
                price=Decimal("74999.00"),
                seller_rating=4.7,
                url="https://example.com/urunpusula-ornek-teklif",
            )
            session.add(offer)

        session.commit()
        print("Sample product and offer are ready.")

    finally:
        session.close()


if __name__ == "__main__":
    seed_sample_data()