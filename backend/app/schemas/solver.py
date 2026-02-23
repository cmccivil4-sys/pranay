from pydantic import BaseModel


class SolverRequest(BaseModel):
    question: str
    level: str = 'adaptive'


class SolverResponse(BaseModel):
    summary: str
    formulas: list[str]
    steps: list[str]
