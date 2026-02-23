from pydantic import BaseModel


class OfflineLicenseRequest(BaseModel):
    campus_code: str
    device_hash: str
    signature: str


class OfflineLicenseResponse(BaseModel):
    valid: bool
    expires_at: str | None = None
    seat_limit: int | None = None
