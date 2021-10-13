from sqlalchemy.orm import Session

from .models import Item


def get_item_list(db: Session, value: str, id: int):
    """
    Get item list and filter by query params if it exists
    """
    items = db.query(Item)
    filter_list = []
    if value:
        items = items.filter(Item.value.contains(value))
        if items.first():
            filter_list.append(*items.all())
    if id:
        items = db.query(Item).filter(Item.id == id)
        if items.first():
            filter_list.append(*items.all())
    if filter_list:
        return filter_list

    return items.all()


def create_item(db: Session, item: Item):
    item = Item(**item.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update_item(db: Session, item: Item):
    """ Update value field """
    item_upd = db.query(Item).filter(Item.id == item.id).first()
    if item_upd:
        item_upd.value = item.value
        db.commit()
        db.refresh(item_upd)
    return item_upd
