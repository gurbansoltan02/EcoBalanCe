from sqlalchemy import or_, and_
from sqlalchemy.orm import Session, joinedload
from models import Users, Message

def signUp(req, db: Session):
    user = db.query(Users).filter(
        or_(
            Users.email == req.email,
            Users.username == req.username
        )
    ).first()
    if user:
        return False
    new_add = Users(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return True 


def signIn(req, db: Session):
    user = db.query(Users).filter(
        and_(
            or_(
                Users.email == req.email,
                Users.username == req.email
            ),
            Users.password == req.password 
        )
    ).first()
    if user:
        return True


def read_users(db: Session):
    return db.query(Users.id, Users.email, Users.username).all()


def create_message(req, db: Session):
    new_add = Message(**req.dict())
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add

def read_message(db: Session):
    result = db.query(
        Message.fullname,
        Message.phone_number,
        Message.email,
        Message.message
    ).limit(15).all()
    return result 