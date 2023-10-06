from sqlalchemy.orm import Session
from db import models
import schemas


def get_all_cheese_types(db: Session):
    return db.query(models.DBCheeseType).all()


def create_cheese_type(db: Session, cheese_type: schemas.CheeseTypeCreate):
    db_cheese_type = models.DBCheeseType(name=cheese_type.name, description=cheese_type.description)
    db.add(db_cheese_type)
    db.commit()
    db.refresh(db_cheese_type)

    return db_cheese_type


