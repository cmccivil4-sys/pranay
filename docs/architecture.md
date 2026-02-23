# AI Circuit Mentor — Production Architecture

## 1) Complete Folder Architecture

```text
.
├── backend/
│   ├── app/
│   │   ├── api/routes/           # FastAPI route modules
│   │   ├── core/                 # settings, auth, security
│   │   ├── db/                   # session + base
│   │   ├── models/               # SQLAlchemy models
│   │   ├── schemas/              # Pydantic schemas
│   │   ├── services/             # AI, cache, CV, voice, billing
│   │   ├── workers/              # background jobs, RL feedback loop
│   │   └── main.py               # API entrypoint
│   ├── tests/                    # backend tests
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── app/                  # Next.js app router
│   │   ├── components/           # UI and feature components
│   │   ├── hooks/                # socket, offline, stream hooks
│   │   ├── lib/                  # api clients, idb cache, auth
│   │   ├── stores/               # state stores (zustand)
│   │   └── workers/              # service worker registration
│   ├── package.json
│   ├── next.config.mjs
│   └── Dockerfile
├── infra/
│   ├── docker/docker-compose.yml # local + offline campus deployment
│   └── k8s/                      # cloud SaaS deployment manifests
├── sql/schema.sql                # PostgreSQL schema bootstrap
└── docs/architecture.md
```

## 2) Backend API Structure

- `POST /api/v1/auth/login` — JWT issue.
- `GET /api/v1/notebook/{note_id}/explain` — AI concept expansion from notes.
- `POST /api/v1/solver/solve` — numerical solving with explanation and steps.
- `POST /api/v1/cv/scan-circuit` — handwritten circuit scanner pipeline entry.
- `WS /api/v1/lab/ws/{room_id}` — multiplayer virtual lab stream.
- `GET /api/v1/analytics/weak-topics/{student_id}` — weak concept detector.
- `POST /api/v1/licensing/verify-offline-key` — college offline activation.
- `POST /api/v1/billing/consume-credits` — monetization credit usage.

## 3) Frontend Component Structure

- `NotebookPlus.tsx` — Smart Notebook++ editor + note-to-cards.
- `VoiceTutorPanel.tsx` — streaming voice tutor controls.
- `NumericalSolver.tsx` — step-by-step numerical solver UI.
- `CircuitScanner.tsx` — upload and scan handwritten circuit.
- `VirtualLabCanvas.tsx` — low-latency real-time lab session.
- `WeakConceptInsights.tsx` — analytics and adaptive recommendations.

## 4) Database Schema

- Multi-tenant users/roles/organizations.
- Notes, revision cards, attempts, mistakes, sessions.
- Subscriptions + credits + offline licenses.
- AI feedback/events for reinforcement loop.

## 5) AI Service Pipeline

- **LLM Orchestrator**: RAG + prompt templates + streaming tokens.
- **Speech Pipeline**: STT -> tutor prompt -> streamed TTS.
- **CV Circuit Pipeline**: image -> component detection -> netlist -> simulation report.
- **RL Feedback Loop**: failures + latency + user feedback -> vector memory updates -> content policy changes.

## 6) Offline Licensing Mechanism

- Campus admin receives signed activation payload (`campus_id`, `device_hash`, `expiry`, `seat_limit`).
- Offline node verifies signature via bundled public key.
- Local issuance tokens cached and rotated with revocation grace window.
- Audit logs encrypted before sync.

## 7) Monetization Logic

- Free tier uses daily request limit + feature flags.
- Paid plans unlock premium modules.
- Credit wallet decremented for expensive inference workloads.
- Campus license bypasses per-student payments but enforces seat limits.

## 8) Performance Strategy

- Redis pub/sub + websocket fanout for instant collaboration.
- IndexedDB write-through cache for offline-first UX.
- Background workers process heavy CV/simulation tasks.
- Streaming LLM/TTS for zero spinner interaction design.
