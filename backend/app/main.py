from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.db.session import Base, engine
from app.models import item, user  # noqa: F401 - import so tables get registered
from app.routers import auth, items

app = FastAPI(title="Hackathon API")

# Without this, your React app (different port) gets silently blocked by the brow
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    # Hackathon-speed shortcut: auto-creates tables instead of writing migrations.
    # Fine for an 8-hour sprint; use Alembic if you ever take this to production.
    Base.metadata.create_all(bind=engine)


app.include_router(auth.router)
app.include_router(items.router)


@app.get("/")
def root():
    return {"status": "ok"}
