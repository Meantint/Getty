from datetime import datetime, timedelta
import json
import bcrypt
import jwt
import os
from typing import List

from fastapi import Depends, FastAPI, HTTPException, Header, UploadFile, File, Body
from sqlalchemy.orm import Session

from database import crud, schemas, models, s3_utils
from common.consts import (
    JWT_SECRET,
    JWT_ALGORITHM,
    AWS_ACCESS_KEY_ID,
    AWS_REGION,
    AWS_SECRET_ACCESS_KEY,
    S3_Bucket,
)
from database.database import SessionLocal, engine

from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Cors
origins = [
    "https://localhost.tiangolo.com",
    "http://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://localhost:5000",
    "http://localhost:3000",
    "http://j5a205.p.ssafy.io:3000",
    "http://j5a205.p.ssafy.io:80",
    "http://j5a205.p.ssafy.io",
]

# Corss
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Object of S3_SERVICE Class
s3_client = s3_utils.S3_SERVICE(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION)


@app.post("/signup", status_code=200, response_model=schemas.User)
async def signup(user_info: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    `회원가입 API`\n
    :param user:s
    :param db:
    :return:
    """
    db_user = crud.get_user_by_userid(db, user_id=user_info.user_id)
    if db_user:
        raise HTTPException(status_code=400, detail="user_id already registered")
    return crud.create_user(db=db, user=user_info)


@app.post("/signin", status_code=200, response_model=schemas.Token)
async def signin(user_info: schemas.UserLogin, db: Session = Depends(get_db)):
    """
    `로그인 API`\n
    :param user_info:
    :param db:
    :return:
    """
    if not user_info.user_id or not user_info.user_pw:
        raise HTTPException(
            status_code=400, detail="user_id and user_pw must be provided"
        )
    is_exist = crud.get_user_by_userid(db, user_id=user_info.user_id)
    if not is_exist:
        raise HTTPException(status_code=400, detail="NO_MATCH_USER")
    is_verified = bcrypt.checkpw(
        user_info.user_pw.encode("utf-8"), is_exist.user_pw.encode("utf-8")
    )
    if not is_verified:
        raise HTTPException(status_code=400, detail="NO_MATCH_USER: Wrong Password")

    print(schemas.UserToken.from_orm(is_exist).dict(exclude={"user_pw", "create_date"}))
    token = dict(
        Authorization=f"{create_access_token(data=schemas.UserToken.from_orm(is_exist).dict(exclude={'user_pw','create_date'}),)}"
    )
    return token


def create_access_token(*, data: dict = None, expires_delta: int = None):
    to_encode = data.copy()
    if expires_delta:
        to_encode.update({"exp": datetime.utcnow() + timedelta(hours=expires_delta)})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return encoded_jwt


@app.get("/test/get_user", status_code=200)
async def get_user(db: Session = Depends(get_db), token: str = Header(None)):
    """
    `토큰 decode TEST API`\n
    :header token:
    :return:
    """
    if token == None:
        raise HTTPException(status_code=400, detail="Header doesn't have Auth Token")
    payload = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
    user_id = payload.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=400, detail="NO_MATCH_USER")
    user = crud.get_user_by_userid(db, user_id=user_id)
    return user


@app.post("/test/upload", status_code=200, description="Upload png asset to S3")
async def upload(fileobject: UploadFile = File(...)):
    """
    `파일 저장 TEST API`\n
    :fileobject File:
    :return:
    """
    filename = fileobject.filename
    current_time = datetime.now()

    # split the file name into two different path (string + extention)
    split_file_name = os.path.splitext(filename)

    # for realtime application you must have genertae unique name for the file
    file_name_unique = str(current_time.timestamp()).replace(".", "")

    file_extension = split_file_name[1]  # file extention

    # Converting tempfile.SpooledTemporaryFile to io.BytesIO
    data = fileobject.file._file

    uploads3 = await s3_client.upload_fileobj(
        bucket=S3_Bucket, key=file_name_unique + file_extension, fileobject=data
    )
    if uploads3:
        s3_url = f"https://{S3_Bucket}.s3.{AWS_REGION}.amazonaws.com/{file_name_unique +  file_extension}"
        return {"status": "success", "image_url": s3_url}  # response added
    else:
        raise HTTPException(status_code=400, detail="Failed to upload in S3")


@app.post("/user/file", status_code=200, description="Upload User File to S3")
async def upload(
    db: Session = Depends(get_db),
    fileobject: UploadFile = File(...),
    token: str = Header(None),
):
    """
    `고객 파일 저장 API`\n
    :header token:
    :fileobject File:
    :return:
    """
    if token == None:
        raise HTTPException(status_code=400, detail="Header doesn't have Auth Token")
    payload = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
    user_id = payload.get("cid")
    if user_id is None:
        raise HTTPException(status_code=400, detail="NO_MATCH_USER")

    filename = fileobject.filename
    current_time = datetime.now()

    # split the file name into two different path (string + extention)
    split_file_name = os.path.splitext(filename)

    # for realtime application you must have genertae unique name for the file
    file_name_unique = str(current_time.timestamp()).replace(".", "")

    file_extension = split_file_name[1]  # file extention

    # Converting tempfile.SpooledTemporaryFile to io.BytesIO
    data = fileobject.file._file

    uploads3 = await s3_client.upload_fileobj(
        bucket=S3_Bucket, key=file_name_unique + file_extension, fileobject=data
    )
    if uploads3:
        s3_url = f"https://{S3_Bucket}.s3.{AWS_REGION}.amazonaws.com/{file_name_unique +  file_extension}"
        return crud.create_user_files(db=db, cid=user_id, file_url=s3_url)
    else:
        raise HTTPException(status_code=400, detail="Failed to upload in S3")


@app.patch("/user/file", status_code=200, description="update user file")
async def update_upload(file_info: schemas.UserFile, db: Session = Depends(get_db)):
    """
    `고객 파일 이름 변경 API`\n
    :body file_info:
    :return:
    """
    if not file_info:
        raise HTTPException(status_code=400, detail="Invaild Input")
    crud.update_user_files(db=db, user_file=file_info)
    return HTTPException(status_code=200, detail="success to update")


@app.get("/user/info", status_code=200, description="get Client Information:고객 마이페이지")
async def get_user_info(db: Session = Depends(get_db), token: str = Header(None)):
    """
    `고객 정보 불러오기 API(마이페이지)`\n
    :header token:
    :return:
    """
    if token == None:
        raise HTTPException(status_code=400, detail="Header doesn't have Auth Token")
    payload = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
    user_cid = payload.get("cid")
    if user_cid is None:
        raise HTTPException(status_code=400, detail="NO_MATCH_USER")
    user_info = crud.get_user_info_by_cid(db, cid=user_cid)
    user_files = crud.get_user_files_by_cid(db, cid=user_cid)
    user_loan = crud.get_user_loan_by_cid(db, cid=user_cid)

    return {"user": user_info, "user_files": user_files, "user_loan": user_loan}


@app.get("/loan", status_code=200)
async def read_loan(db: Session = Depends(get_db)):
    """
    `대출 상품 리스트 가져오기`
    :param db:
    :return:
    """
    db_loan_list = crud.get_loan(db)
    if not db_loan_list:
        raise HTTPException(status_code=400, detail="loan error")
    return db_loan_list


@app.get("/user/loan", status_code=200)
async def read_user_loan(db: Session = Depends(get_db), token: str = Header(None)):
    """
    `고객 조건에 맞는 대출 상품 리스트 가져오기`
    :header token:
    :param db:
    :return:
    """
    if token == None:
        raise HTTPException(status_code=400, detail="Header doesn't have Auth Token")
    payload = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
    user_id = payload.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=400, detail="NO_MATCH_USER")
    user = crud.get_user_by_userid(db, user_id=user_id)

    db_user_loan_list = crud.get_user_loan(db, user)
    if not db_user_loan_list:
        raise HTTPException(status_code=400, detail="loan error")

    response_data = []
    print(f"cid = {user.cid}")
    for user_loan_list in db_user_loan_list:
        print(user_loan_list)
        res = {
            "loan_address": user_loan_list.loan_address,
            "lid": user_loan_list.lid,
            "loan_age": user_loan_list.loan_age,
            "interest_rate": user_loan_list.interest_rate,
            "loan_about": user_loan_list.loan_about,
            "loan_salary": user_loan_list.loan_salary,
            "loan_name": user_loan_list.loan_name,
            "loan_job": user_loan_list.loan_job,
            "loan_amount": user_loan_list.loan_amount,
            "loan_img": user_loan_list.loan_img,
            "is_exist": crud.get_is_already_exist(db, user.cid, user_loan_list.lid),
        }
        response_data.append(res)

    return response_data
    # return [
    #     db_user_loan_list,
    #     [
    #         crud.get_is_already_exist(db, user.cid, user_loan_list.lid)
    #         for user_loan_list in db_user_loan_list
    #     ],
    # ]


@app.get("/user/loan/list", status_code=200)
async def user_loan_list(db: Session = Depends(get_db), token: str = Header(None)):
    """
    `고객이 신청한 대출 상품 리스트`
    :header token:
    :param db:
    :return:
    """
    if token == None:
        raise HTTPException(status_code=400, detail="Header doesn't have Auth Token")
    payload = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
    user_id = payload.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=400, detail="NO_MATCH_USER")
    user = crud.get_user_by_userid(db, user_id=user_id)

    db_loan_by_user_list = crud.get_user_loan_by_cid(db, user.cid)
    if not db_loan_by_user_list:
        raise HTTPException(status_code=400, detail="user_loan_list error")

    return [
        db_loan_by_user_list,
        [
            crud.get_loan_by_lid(db, lid=loan_by_user.lid)
            for loan_by_user in db_loan_by_user_list
        ],
    ]


@app.post("/user/loan/request/{lid}", status_code=200)
async def user_loan_request(
    db: Session = Depends(get_db), token: str = Header(None), lid: int = None
):
    """
    `대출 상품 리스트 신청`
    :header token:
    :param db:
    :param lid:
    :return:
    """
    if token == None:
        raise HTTPException(status_code=400, detail="Header doesn't have Auth Token")
    payload = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
    user_cid = payload.get("cid")
    if user_cid is None:
        raise HTTPException(status_code=400, detail="NO_MATCH_USER")

    db_user_files_by_cid = crud.get_user_files_by_cid(db, cid=user_cid)
    if db_user_files_by_cid is None:
        raise HTTPException(status_code=400, detail="This user doesn't have file")
    user_loan = crud.get_user_loan_by_cid(db, cid=user_cid)
    for cur in user_loan:
        if cur.lid == lid and cur.is_suitable == "확인중":
            return HTTPException(status_code=400, detail="Already checking")

    return [
        crud.create_user_loan(db=db, user_loan={"cid": int(user_cid), "lid": lid}),
        [
            crud.create_user_loan_request(
                db,
                user_loan={
                    "cid": user_cid,
                    "lid": lid,
                    "file_name": db_user_files_by_cid[idx].file_name,
                    "file_url": db_user_files_by_cid[idx].file_url,
                },
            )
            for idx in range(len(db_user_files_by_cid))
        ],
    ]

    # return db_user_files_by_cid


@app.post("/test/loan", status_code=200, response_model=schemas.LoanCreate)
async def create_loan(req_info: schemas.LoanCreate, db: Session = Depends(get_db)):
    """
    `대출 상품 리스트 추가`
    :param req_info:
    :param db:
    :return:
    """
    return crud.create_loan(db=db, loan=req_info)


@app.get("/banker", status_code=200)
async def read_banker(db: Session = Depends(get_db)):
    """
    `행원 리스트 보기`
    :param db:
    :return:
    """
    db_banker_list = crud.get_banker(db)
    # if not db_banker_list:
    #     raise HTTPException(status_code=400, detail="banker error")
    return db_banker_list


@app.post("/test/banker", status_code=200, response_model=schemas.BankerCreate)
async def create_banker(req_info: schemas.BankerCreate, db: Session = Depends(get_db)):
    """
    `행원 추가`
    :param req_info:
    :param db:
    :return:
    """
    return crud.create_banker(db=db, banker=req_info)


@app.post("/test/relation", status_code=200, response_model=schemas.CombineID)
async def create_relation(
    combine_info: schemas.CombineID, db: Session = Depends(get_db)
):
    """
    `고객 <-> 대출 상품 연결`
    `고객 <-> 행원 연결`
    :param req_info:
    :param db:
    :return:
    """
    return [
        crud.create_user_loan(db=db, id_info=combine_info),
        crud.create_banker_client(db=db, id_info=combine_info),
    ]


@app.patch("/user/loan/status", status_code=200)
async def update_status(status_info: schemas.UserLoan, db: Session = Depends(get_db)):
    """
    `신청한 대출 상품 상태 변경 API`\n
    :param is_suitable:
    :param db:
    :return:
    """
    if not status_info:
        raise HTTPException(status_code=400, detail="Invaild Input")
    crud.update_user_status(db=db, status_info=status_info)
    return HTTPException(status_code=200, detail="success to update")


@app.get("/loan/user/list", status_code=200)
async def get_user_loan_list(db: Session = Depends(get_db)):
    """
    `고객이 신청한 대출 상품 리스트 API`\n
    :param db:
    :return:
    """
    return crud.get_loan_list(db=db)


@app.get("/detail/user/{cid}/loan/{lid}", status_code=200)
async def get_user_loan_detail(cid: int, lid: int, db: Session = Depends(get_db)):
    """
    `고객이 신청한 대출 세부정보`\n
    :param db:
    :return:
    """
    user_detail = crud.get_user_loan_detail(db=db, cid=cid, lid=lid)
    user_files = crud.get_user_loan_files(db=db, cid=cid, lid=lid)

    return {"user_detail": user_detail, "user_files": user_files}


@app.get("/data/file_url", status_code=200)
async def get_user_file_data(fileurl: str = Header(None)):
    return crud.get_user_data(file_url=fileurl)
