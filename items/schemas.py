from pydantic import BaseModel


class ItemBase(BaseModel):
    value: str


class ItemDetail(ItemBase):
    id: int

    class Config:
        orm_mode = True


class ItemCreate(ItemBase):
    pass
