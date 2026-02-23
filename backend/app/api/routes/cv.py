from fastapi import APIRouter, UploadFile

from app.services.cv_pipeline import cv_pipeline

router = APIRouter(prefix='/cv', tags=['cv'])


@router.post('/scan-circuit')
async def scan_circuit(image: UploadFile) -> dict:
    return await cv_pipeline.scan(image.filename)
