from app.schemas.licensing import OfflineLicenseRequest, OfflineLicenseResponse


class OfflineLicenseVerifier:
    async def verify(self, payload: OfflineLicenseRequest) -> OfflineLicenseResponse:
        valid = payload.signature.startswith('sig_') and len(payload.device_hash) > 8
        return OfflineLicenseResponse(valid=valid, expires_at='2027-12-31T00:00:00Z' if valid else None, seat_limit=200 if valid else None)


license_verifier = OfflineLicenseVerifier()
