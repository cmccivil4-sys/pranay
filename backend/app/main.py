from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import analytics, auth, billing, cv, lab, licensing, notebook, solver
from app.core.config import settings

app = FastAPI(title=settings.app_name)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

api_prefix = '/api/v1'
app.include_router(auth.router, prefix=api_prefix)
app.include_router(notebook.router, prefix=api_prefix)
app.include_router(solver.router, prefix=api_prefix)
app.include_router(cv.router, prefix=api_prefix)
app.include_router(lab.router, prefix=api_prefix)
app.include_router(analytics.router, prefix=api_prefix)
app.include_router(licensing.router, prefix=api_prefix)
app.include_router(billing.router, prefix=api_prefix)


@app.get('/health')
async def health() -> dict:
    return {'status': 'ok', 'service': settings.app_name}
