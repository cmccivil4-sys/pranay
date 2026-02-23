from fastapi import APIRouter

from app.services.ai_orchestrator import ai_orchestrator

router = APIRouter(prefix='/notebook', tags=['notebook'])


@router.get('/{note_id}/explain')
async def explain_note(note_id: str) -> dict:
    return await ai_orchestrator.explain_note(f'note_id={note_id}')
