from pydantic import BaseModel

class loginSchema(BaseModel):
    email: str 
    password: str 

class registerSchema(loginSchema):
    username: str 

class messageSchema(BaseModel):
    fullname: str 
    phone_number: str 
    email: str
    message: str 