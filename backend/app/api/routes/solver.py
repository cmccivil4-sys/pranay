from fastapi import APIRouter

from app.schemas.solver import SolverRequest, SolverResponse
from app.services.ai_orchestrator import ai_orchestrator

router = APIRouter(prefix='/solver', tags=['solver'])


@router.post('/solve', response_model=SolverResponse)
async def solve(payload: SolverRequest) -> SolverResponse:
    result = await ai_orchestrator.solve(payload.question)
    return SolverResponse(**result)
