from fastapi import FastAPI

from app.routers.products import router as products_router


app = FastAPI()

app.include_router(products_router)


@app.get("/health")
def health():
    return {"status": "ok"}