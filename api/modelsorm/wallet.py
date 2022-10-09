from pydantic import BaseModel

class WalletORM(BaseModel):
    public_key: str
    private_key: str
    matic_balance: float
    ruble_balance: float
    nft_balance: float
    user_id: int