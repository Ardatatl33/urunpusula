from pydantic import BaseModel, ConfigDict


class ProductResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    brand: str
    name: str
    storage_gb: int
    ram_gb: int
    screen_inches: float
    battery_mah: int
    main_camera_mp: int
    has_5g: bool