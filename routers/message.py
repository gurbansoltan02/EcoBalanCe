from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session 
from db import get_db
import crud 
from models import messageSchema

message_router = APIRouter()

@message_router.post('/add-message')
def add_message(req: messageSchema, db: Session = Depends(get_db)):
    try:
        result = crud.create_message(req, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong!!!')

@message_router.get('/get-message')
def get_message(db: Session = Depends(get_db)):
    try: 
        result = crud.read_message(db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Something went wrong!!!')
        