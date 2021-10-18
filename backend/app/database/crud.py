
from re import S
from sqlalchemy.orm import Session

from . import models, schemas
from datetime import date
import bcrypt

from AI import validate


def get_user(db: Session, user_id: int):
    return db.query(models.Client).filter(models.Client.cid == user_id).first()


def get_user_by_userid(db: Session, user_id: str):
    return db.query(models.Client).filter(models.Client.user_id == user_id).first()


def get_user_info_by_cid(db: Session, cid: int):
    return db.query(models.Client).filter(models.Client.cid == cid).first()


def get_user_files_by_cid(db: Session, cid: int):
    return db.query(models.ClientFile).filter(models.ClientFile.cid == cid).all()


def get_user_loan_by_cid(db: Session, cid: int):
    return db.query(models.UserLoan).filter(models.UserLoan.cid == cid).all()


def get_loan_by_lid(db: Session, lid: int):
    return db.query(models.LoanProduct).filter(models.LoanProduct.lid == lid).first()


def get_loan_name_by_lid(db: Session, lid: int):
    return (
        db.query(models.LoanProduct.loan_name)
        .filter(models.LoanProduct.lid == lid)
        .first()
    )


def get_is_already_exist(db: Session, cid: int, lid: int):
    if (
        db.query(models.UserLoan)
        .filter(models.UserLoan.cid == cid, models.UserLoan.lid == lid)
        .first()
    ):
        return True
    return False


def get_loan_info_by_cli_lid(db: Session, cid: int, lid: int):
    return (
        db.query(models.UserLoan)
        .filter(models.UserLoan.lid == lid, models.UserLoan.cid == cid)
        .first()
    )


def get_loan_files_by_cli_lid(db: Session, cid: int, lid: int):
    return (
        db.query(models.UserLoanFiles)
        .filter(models.UserLoanFiles.lid == lid, models.UserLoanFiles.cid == cid)
        .all()
    )


def create_user(db: Session, user: schemas.UserCreate):
    # fake_hashed_password = user.user_pw + "notreallyhashed"
    hashed_password = bcrypt.hashpw(user.user_pw.encode("utf-8"), bcrypt.gensalt())
    # print(1234, "   ", hashed_password)
    # 현재 날짜 가져오기
    create_at = date.today()

    db_user = models.Client(
        user_id=user.user_id,
        user_pw=hashed_password,
        user_name=user.user_name,
        phone_number=user.phone_number,
        create_date=create_at,
        job=user.job,
        birth=user.birth,
        sex=user.sex,
        salary=user.salary,
        address="",
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_loan(db: Session):
    # print(f"db.query(models.LoanProduct).all() = {db.query(models.LoanProduct).all()}")
    return db.query(models.LoanProduct).all()


def get_loan_by_user(db: Session, user_id: str):
    return db.query(models.LoanProduct).filter()


def get_user_loan(db: Session, user: schemas.User):
    # return db.query(models.LoanProduct).all()
    return (
        db.query(models.LoanProduct)
        .filter(
            models.LoanProduct.loan_age <= date.today().year - int(user.birth[0:4]),
            models.LoanProduct.loan_salary <= int(user.salary),
        )
        .all()
    )


def get_banker(db: Session):
    return db.query(models.Banker).all()


# 대출 상품 생성
def create_loan(db: Session, loan: schemas.LoanCreate):
    db_loan = models.LoanProduct(
        loan_name=loan.loan_name,
        loan_age=loan.loan_age,
        loan_salary=loan.loan_salary,
        loan_address=loan.loan_address,
        loan_job=loan.loan_job,
        interest_rate=loan.interest_rate,
        loan_amount=loan.loan_amount,
        loan_about=loan.loan_about,
    )
    db.add(db_loan)
    db.commit()
    db.refresh(db_loan)
    return db_loan


# 행원 생성
def create_banker(db: Session, banker: schemas.BankerCreate):
    db_banker = models.Banker(
        banker_name=banker.banker_name,
        lid=banker.lid,
        banker_id=banker.banker_id,
        banker_pw=banker.banker_pw,
        local=banker.local,
    )
    db.add(db_banker)
    db.commit()
    db.refresh(db_banker)
    return db_banker


# 고객 <-> 대출 상품 관계 생성
def create_user_loan(db: Session, user_loan: dict):
    db_user_loan = models.UserLoan(cid=user_loan["cid"], lid=user_loan["lid"])

    db.add(db_user_loan)
    db.commit()
    db.refresh(db_user_loan)
    return db_user_loan


# 고객 <-> 대출 상품 관계 생성(서류 정보)
def create_user_loan_request(db: Session, user_loan: dict):
    db_user_loan_request = models.UserLoanFiles(
        cid=user_loan["cid"],
        lid=user_loan["lid"],
        file_name=user_loan["file_name"],
        file_url=user_loan["file_url"],
    )

    db.add(db_user_loan_request)
    db.commit()
    db.refresh(db_user_loan_request)
    return db_user_loan_request


# 고객 파일 저장
def create_user_files(db: Session, cid: int, file_url: str):
    file_result = dict(validate.check(file_url))
    file_name = file_result["file_name"]
    db_user_file = models.ClientFile(cid=cid, file_url=file_url,file_name=file_name)
    db.add(db_user_file)
    db.commit()
    db.refresh(db_user_file)
    return db_user_file


# 고객 데이터 반환
def get_user_data(file_url: str):
    return dict(validate.check(file_url))


# 고객 파일 수정
def update_user_files(db: Session, user_file: schemas.UserFile):
    file_data = (
        db.query(models.ClientFile)
        .filter(
            models.ClientFile.cid == user_file.cid,
            models.ClientFile.file_url == user_file.file_url,
        )
        .first()
    )
    req_dict = user_file.dict()
    req_dict["cid"] = user_file.cid
    req = {k: v for k, v in req_dict.items()}
    for key, value in req.items():
        setattr(file_data, key, value)
    db.commit()
    return file_data
    # print(file_data.cid,file_data.file_name,file_data.file_url)
    # return file_data.update(auto_commit=True, **user_file.dict())

# 고객 파일 수정
def update_user_files(db: Session, cid: int, file_url: str, file_name: str):
    file_data = (
        db.query(models.ClientFile)
        .filter(
            models.ClientFile.cid == cid,
            models.ClientFile.file_url == file_url,
        )
        .first()
    )
    user_file = schemas.UserFile(
        cid=cid,
        file_name=file_name,
        file_url=file_url
    )
    req_dict = user_file.dict()
    req_dict["cid"] = user_file.cid
    req = {k: v for k, v in req_dict.items()}
    for key, value in req.items():
        setattr(file_data, key, value)
    db.commit()
    return file_data


# 고객 <-> 행원 관계 생성
def create_banker_client(db: Session, id_info: schemas.CombineID):
    db_banker_client = models.BankerClient(
        bid=id_info.bid,
        cid=id_info.cid,
    )
    db.add(db_banker_client)
    db.commit()
    db.refresh(db_banker_client)
    return db_banker_client


# Combine create_user_loan, cretae_banker_client
def create_relation(
    db: Session,
    client: schemas.ClientID,
    banker: schemas.BankerID,
    loan: schemas.LoanID,
):
    create_info = []
    create_info.append(create_user_loan(db, client, loan))
    create_info.append(create_banker_client(db, client, banker))

    return create_info


# 고객 대출 적부판정 수정
def update_user_status(db: Session, status_info: schemas.UserLoan):
    loan_data = (
        db.query(models.UserLoan)
        .filter(
            models.UserLoan.cid == status_info.cid,
            models.UserLoan.lid == status_info.lid,
        )
        .first()
    )
    req_dict = status_info.dict()
    req_dict["cid"] = status_info.cid
    req = {k: v for k, v in req_dict.items()}
    for key, value in req.items():
        setattr(loan_data, key, value)
    db.commit()
    return loan_data


# 고객 대출 신청 리스트
def get_loan_list(db: Session):
    loan_list_data = db.query(models.UserLoan).all()
    loan_list = []
    for data in loan_list_data:
        client = get_user_info_by_cid(db=db, cid=data.cid)
        loan = get_loan_by_lid(db=db, lid=data.lid)
        is_suitable = get_loan_info_by_cli_lid(db=db, cid=data.cid, lid=data.lid)

        db_loan_info = schemas.UserLoanInfo(
            cid=data.cid,
            lid=data.lid,
            user_name=client.user_name,
            loan_name=loan.loan_name,
            is_suitable=is_suitable.is_suitable,
        )
        loan_list.append(db_loan_info)

    return loan_list


# 고객 대출 신청 세부정보
def get_user_loan_detail(db: Session, cid: int, lid: int):
    user_info = get_user_info_by_cid(db=db, cid=cid)
    loan = get_loan_by_lid(db=db, lid=lid)
    user_loan = get_loan_info_by_cli_lid(db=db, cid=cid, lid=lid)

    detail = schemas.UserLoanDetail(
        cid=cid,
        lid=lid,
        loan_name=loan.loan_name,
        user_name=user_info.user_name,
        phone_number=user_info.phone_number,
        address=user_info.address,
        job=user_info.job,
        birth=user_info.birth,
        sex=user_info.sex,
        salary=user_info.salary,
        is_suitable=user_loan.is_suitable,
    )

    return detail


# 고객이 신청한 상품에 맞는 서류
def get_user_loan_files(db: Session, cid: int, lid: int):
    return get_loan_files_by_cli_lid(db=db, cid=cid, lid=lid)
