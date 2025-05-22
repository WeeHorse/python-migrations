from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, CheckConstraint, TIMESTAMP, func, Boolean
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import expression

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    ssn = Column(String, nullable=False, unique=True)
    accounts = relationship('Account', back_populates='customer')
    email = Column(String)
    approved = Column(Boolean, nullable=False, default=False)

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    number = Column(String, unique=True)
    balance = Column(Numeric, insert_default=0, nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    __table_args__ = (
        CheckConstraint('balance >= 0', name='non_negative_balance'),
    )
    customer = relationship("Customer", back_populates="accounts")

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    amount = Column(Integer, nullable=False, server_default="0")
    account_nr = Column(String, nullable=False)
    time = Column(TIMESTAMP, server_default=func.now())