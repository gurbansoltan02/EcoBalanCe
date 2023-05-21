from fastapi import FastAPI
from db import Base, engine
from routers import authentication_router, message_router

app = FastAPI()

Base.metadata.create_all(engine)

app.include_router(authentication_router, tags=['Authentication'])
app.include_router(message_router, tags=['Contact_us'])