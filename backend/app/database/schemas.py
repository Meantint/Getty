from datetime import date
from typing import List, Optional
from enum import Enum
from pydantic import BaseModel


class User(BaseModel):
    user_id: str
    user_name: str
    phone_number: str
    create_date: date
    address: str
    job: str
    birth: str
    sex: int
    salary: int

    class Config:
        orm_mode = True


# 회원가입
class UserCreate(BaseModel):
    user_id: str
    user_pw: str
    user_name: str
    phone_number: str
    job: str
    birth: str
    sex: int
    salary: int


# 로그인
class UserLogin(BaseModel):
    user_id: str
    user_pw: str


class Token(BaseModel):
    Authorization: str


class UserToken(BaseModel):
    cid: int
    user_id: str
    # user_pw: str
    user_name: str
    phone_number: str
    # create_date: date

    class Config:
        orm_mode = True


# 대출 상품 리스트
class LoanCreate(BaseModel):
    loan_name: str
    loan_age: str
    loan_salary: str
    loan_address: str
    loan_job: str
    interest_rate: str
    loan_amount: int
    loan_about: str
    loan_img: str

    class Config:
        orm_mode = True


# 행원
class BankerCreate(BaseModel):
    banker_name: str
    lid: int
    banker_id: str
    banker_pw: str
    local: str

    class Config:
        orm_mode = True


# Combine loan_id, client_id, banker_id
class CombineID(BaseModel):
    lid: int
    cid: int
    bid: int

    class Config:
        orm_mode = True


# loan_id
class LoanID(BaseModel):
    lid: int


# client_id
class ClientID(BaseModel):
    cid: int


# banker_id
class BankerID(BaseModel):
    bid: int


# 고객 개인 파일 업로드
class UserUploadFile(BaseModel):
    cid: int
    file_url: str


# 고객 개인 파일
class UserFile(BaseModel):
    cid: Optional[int]
    file_name: Optional[str]
    file_url: Optional[str]


# 고객 신청 상품 정보
class UserLoanInfo(BaseModel):
    cid: int
    lid: int
    user_name: str
    loan_name: str
    is_suitable: str


# 고객이 신청한 대출
class UserLoan(BaseModel):
    cid: int
    lid: int
    is_suitable: str


# 고객이 신청한 대출 리스트
class UserLoanInfo(BaseModel):
    cid: int
    lid: int
    loan_name: str
    user_name: str
    is_suitable: str


# 고객 신청 상품 세부정보
class UserLoanDetail(BaseModel):
    cid: int
    lid: int
    loan_name: str

    user_name: str
    phone_number: str
    address: str
    job: str
    birth: str
    sex: int
    salary: int

    is_suitable: str

    
# 고객 파일 정보
class ReadUserFile(BaseModel):
    data_list: list

# 고객 파일 URL
class UserFileURL(BaseModel):
    file_url: str

