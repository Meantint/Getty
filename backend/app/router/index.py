from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import Response

# from database.conn import db
# from database.schema import Users

router = APIRouter()

# @router.get("/")
# async def index(session: Session = Depends(db.session),):
