from database.config import base
from sqlalchemy import Integer, Float, String, Column, ForeignKey

class Wallet(base):

    __tablename__ = 'wallet'

    id = Column(Integer, primary_key = True)
    public_key = Column(String(255))
    private_key = Column(String(255))
    matic_balance = Column(Float)
    ruble_balance = Column(Float)
    nft_balance = Column(Float)
    user_id = Column(Integer, ForeignKey('user.id'))