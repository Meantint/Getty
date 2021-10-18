from sqlalchemy import Boolean, Column, ForeignKey, String, Integer, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.sqltypes import DateTime

from .database import Base


class Client(Base):
    __tablename__ = "client"

    cid = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        comment="고객 고유 ID",
    )
    user_name = Column(String(45), nullable=True, comment="고객 이름")
    user_id = Column(String(45), nullable=True, comment="고객 ID")
    user_pw = Column(String(45), nullable=True, comment="고객 PW")
    create_date = Column(Date, nullable=True, comment="생성 날짜")
    phone_number = Column(String(45), nullable=True, comment="전화 번호")

    address = Column(String(45), nullable=True, comment="주소")
    job = Column(String(45), nullable=False, comment="직업")
    birth = Column(String(45), nullable=False, comment="생년월일")
    sex = Column(Integer, nullable=False, comment="성별")
    salary = Column(Integer, nullable=False, comment="연봉")

    # items = relationship("UserInfomation", back_populates="owner")


# client files
class ClientFile(Base):
    __tablename__ = "client_file"

    fid = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        comment="파일 고유 ID",
    )
    cid = Column(
        Integer,
        ForeignKey("client.cid", ondelete="RESTRICT", onupdate="RESTRICT"),
        nullable=False,
        comment="고객 고유 ID",
    )
    file_name = Column(String(45), nullable=True, default="", comment="파일 이름")
    file_url = Column(String(100), nullable=False, comment="파일 저장소 URL")


class LoanProduct(Base):
    __tablename__ = "loan_product"

    lid = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        comment="대출 식별 ID",
    )
    loan_name = Column(String(45), nullable=False, comment="상품 이름")
    loan_age = Column(String(45), nullable=True, comment="나이 조건")
    loan_salary = Column(String(45), nullable=True, comment="연봉 조건")
    loan_address = Column(String(500), nullable=True, comment="상품 주소")
    loan_job = Column(String(45), nullable=True, comment="직업 조건")
    interest_rate = Column(String(45), nullable=True, comment="금리")
    loan_amount = Column(Integer, nullable=True, comment="대출 가능 금액")
    loan_about = Column(String(500), nullable=True, comment="상품 설명")
    loan_img = Column(String(100), nullable=True, comment="대출 이미지 링크")


class Banker(Base):
    __tablename__ = "banker"

    bid = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        comment="행원 고유 ID",
    )
    banker_name = Column(String(45), nullable=True, comment="행원 이름")
    lid = Column(Integer, nullable=True, comment="행원 담당 대출")
    banker_id = Column(String(45), nullable=True, comment="행원 ID")
    banker_pw = Column(String(45), nullable=True, comment="행원 PW")
    local = Column(String(45), nullable=True, comment="담당 지역")


class UserLoan(Base):
    __tablename__ = "user_loan"

    ulid = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        comment="고객 상품 가입 고유 ID",
    )
    cid = Column(
        Integer,
        ForeignKey("client.cid", ondelete="RESTRICT", onupdate="RESTRICT"),
        nullable=False,
        comment="고객 고유 ID",
    )
    lid = Column(
        Integer,
        ForeignKey("loan_product.lid", ondelete="RESTRICT", onupdate="RESTRICT"),
        nullable=True,
        comment="고객 대출 상품 ID",
    )

    is_suitable = Column(
        String(45), nullable=True, default="확인중", comment="대출 가입 적합/부적합"
    )


class UserLoanFiles(Base):
    __tablename__ = "user_loan_files"

    sid = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        comment="유저 파일 고유 ID",
    )
    cid = Column(
        Integer,
        ForeignKey("client.cid", ondelete="RESTRICT", onupdate="RESTRICT"),
        nullable=False,
        comment="고객 고유 ID",
    )
    lid = Column(
        Integer,
        ForeignKey("loan_product.lid", ondelete="RESTRICT", onupdate="RESTRICT"),
        nullable=False,
        comment="고객 대출 상품 ID",
    )

    file_name = Column(String(45), nullable=True, comment="파일 이름")
    file_url = Column(String(100), nullable=False, comment="파일 저장소 URL")


class BankerClient(Base):
    __tablename__ = "banker_client"

    bcid = Column(Integer, nullable=False, primary_key=True)
    bid = Column(
        Integer,
        ForeignKey("banker.bid", ondelete="RESTRICT", onupdate="RESTRICT"),
        nullable=False,
        comment="행원 고유 ID",
    )
    cid = Column(
        Integer,
        ForeignKey("user_loan.cid", ondelete="RESTRICT", onupdate="RESTRICT"),
        nullable=True,
        comment="고객 고유 ID",
    )
