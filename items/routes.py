from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi_pagination import LimitOffsetPage, add_pagination, paginate
from sqlalchemy.orm import Session

from core.utils import get_db

from . import crud
from .schemas import ItemCreate, ItemDetail

router = APIRouter()


@router.get("/", response_model=LimitOffsetPage[ItemDetail])
def item_list(
    db: Session = Depends(get_db),
    value: Optional[str] = Query(None),
    id: Optional[int] = Query(None),
):
    return paginate(crud.get_item_list(db, value, id))


@router.post("/")
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, item)


@router.put("/", response_model=ItemDetail)
def update_item(item: ItemDetail, db: Session = Depends(get_db)):
    upd_item = crud.update_item(db, item)
    if not upd_item:
        raise HTTPException(status_code=404, detail="Not Found")
    return upd_item


add_pagination(router)
