from fastapi import APIRouter
from pydantic import BaseModel

from app.services.billing import billing_service

router = APIRouter(prefix='/billing', tags=['billing'])


class ConsumeCreditsRequest(BaseModel):
    wallet_balance: int
    feature: str


@router.post('/consume-credits')
async def consume_credits(payload: ConsumeCreditsRequest) -> dict:
    return await billing_service.consume(payload.wallet_balance, payload.feature)
