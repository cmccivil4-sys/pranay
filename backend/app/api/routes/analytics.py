from fastapi import APIRouter

router = APIRouter(prefix='/analytics', tags=['analytics'])


@router.get('/weak-topics/{student_id}')
async def weak_topics(student_id: str) -> dict:
    return {
        'student_id': student_id,
        'weak_topics': [
            {'topic': 'Nodal Analysis', 'confidence': 0.45, 'recommended_set': 'set_12'},
            {'topic': 'Transient RC Response', 'confidence': 0.38, 'recommended_set': 'set_19'},
        ],
    }
