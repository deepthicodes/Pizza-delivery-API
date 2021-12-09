from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    id:Optional[int]
    username:str
    email:str
    password:str
    is_staff:Optional[bool]
    is_active:Optional[bool]


    class Config:
        orm_mode=True
        schema_extra={
            'example':{
                "username":"jeevithachethan",
                "email":"deeptigns97@gmail.com",
                "password":"password",
                "is_staff":False,
                "is_active":True
            }
        }


            
class Settings(BaseModel):
    authjwt_secret_key:str='5fbd6036dbbaf26c9ee51f1604e203ad553b01f26ce3c40239a935a34dea0415'


class LoginModel(BaseModel):
    username:str
    password:str



class OrderModel(BaseModel):
    id:Optional[int]
    quantity:int
    order_Status:Optional[str]="PENDING",
    pizza_size:Optional[str]="SMALL"
    user_id:Optional[int]
   
    class Config:
       orm_mode=True
       schema_extra={
           "example":{
               "quantity":2,
               "pizza_size":"LARGE"
            }
        }
