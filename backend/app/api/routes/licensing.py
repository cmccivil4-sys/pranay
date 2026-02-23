from fastapi import APIRouter

from app.schemas.licensing import OfflineLicenseRequest
from app.services.licensing import license_verifier

router = APIRouter(prefix='/licensing', tags=['licensing'])


@router.post('/verify-offline-key')
async def verify_offline_key(payload: OfflineLicenseRequest):
    return await license_verifier.verify(payload)
