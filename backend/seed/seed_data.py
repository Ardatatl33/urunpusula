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
        pro_max = session.scalar(
            select(Product).where(
                Product.brand == "Apple",
                Product.name == "iPhone 17 Pro Max",
                Product.storage_gb == 256,
            )
        )

        if pro_max is None:
            pro_max = Product(
                brand="Apple",
                name="iPhone 17 Pro Max",
                storage_gb=256,
                ram_gb=12,
                screen_inches=6.9,
                battery_mah=4500,
                main_camera_mp=48,
                has_5g=True,
            )
            session.add(pro_max)
            session.flush()

        pro_max_offer = session.scalar(
            select(Offer).where(
                Offer.product_id == pro_max.id,
                Offer.marketplace == "Hepsiburada",
                Offer.seller_name == "Örnek Mobil Mağazası",
            )
        )

        if pro_max_offer is None:
            pro_max_offer = Offer(
                product_id=pro_max.id,
                marketplace="Hepsiburada",
                seller_name="Örnek Mobil Mağazası",
                price=Decimal("89999.00"),
                seller_rating=4.6,
                url="https://example.com/urunpusula-iphone-17-pro-max",
            )
            session.add(pro_max_offer)

        iphone_17 = session.scalar(
            select(Product).where(
                Product.brand == "Apple",
                Product.name == "iPhone 17",
                Product.storage_gb == 128,
            )
        )

        if iphone_17 is None:
            iphone_17 = Product(
                brand="Apple",
                name="iPhone 17",
                storage_gb=128,
                ram_gb=8,
                screen_inches=6.3,
                battery_mah=3600,
                main_camera_mp=48,
                has_5g=True,
            )
            session.add(iphone_17)
            session.flush()

        iphone_17_offer = session.scalar(
            select(Offer).where(
                Offer.product_id == iphone_17.id,
                Offer.marketplace == "n11",
                Offer.seller_name == "Örnek Telefon Mağazası",
            )
        )

        if iphone_17_offer is None:
            iphone_17_offer = Offer(
                product_id=iphone_17.id,
                marketplace="n11",
                seller_name="Örnek Telefon Mağazası",
                price=Decimal("59999.00"),
                seller_rating=4.5,
                url="https://example.com/urunpusula-iphone-17",
            )
            session.add(iphone_17_offer)

        samsung_s23 = session.scalar(
            select(Product).where(
                Product.brand == "Samsung",
                Product.name == "Galaxy S23",
                Product.storage_gb == 128,
            )
        )

        if samsung_s23 is None:
            samsung_s23 = Product(
                brand="Samsung",
                name="Galaxy S23",
                storage_gb=128,
                ram_gb=8,
                screen_inches=6.1,
                battery_mah=3900,
                main_camera_mp=50,
                has_5g=True,
            )
            session.add(samsung_s23)
            session.flush()

        samsung_s23_offer = session.scalar(
            select(Offer).where(
                Offer.product_id == samsung_s23.id,
                Offer.marketplace == "Pazarama",
                Offer.seller_name == "Örnek Elektronik Mağazası",
            )
        )

        if samsung_s23_offer is None:
            samsung_s23_offer = Offer(
                product_id=samsung_s23.id,
                marketplace="Pazarama",
                seller_name="Örnek Elektronik Mağazası",
                price=Decimal("31999.00"),
                seller_rating=4.4,
                url="https://example.com/urunpusula-galaxy-s23",
            )
            session.add(samsung_s23_offer)

        session.commit()
        print("Sample product and offer are ready.")

    finally:
        session.close()


if __name__ == "__main__":
    seed_sample_data()
