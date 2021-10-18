from datetime import datetime, timedelta

import bcrypt
import jwt
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import schema

# TODO:
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

# from app.common.consts import JWT_SECRET, JWT_ALGORITHM
from app.database.database import SessionLocal
from app.database.models import Client
from app.database.schemas import Token, UserToken, User, UserCreate
from app.database import crud, schemas
# from ..main import get_db

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup", status_code=200, response_model=User)
async def signup(reg_info: UserCreate, db: Session = Depends(get_db)):
    """
    `회원가입 API`\n
    :param reg_info:
    :param db:
    :return:
    """
    db_user = crud.get_user_by_userid(db, email=reg_info.user_id)
    if db_user:
        raise HTTPException(status_code=400, detail="user_id already registered")
    return crud.create_user(db=db, user=reg_info)


'''
def create_access_token(*, data: dict = None, expires_delta: int = None):
    to_encode = data.copy()
    if expires_delta:
        to_encode.update({"exp": datetime.utcnow() + timedelta(hours=expires_delta)})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return encoded_jwt
'''

