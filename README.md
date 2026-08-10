<div align="center">

# SwipeBot

**Telegram client for a commercial real-estate platform — browse, publish and manage apartment rental announcements from Telegram.**

![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python&logoColor=white)
![aiogram](https://img.shields.io/badge/aiogram-3.21-blue?style=flat-square)
![MongoDB](https://img.shields.io/badge/MongoDB-4.14-green?style=flat-square&logo=mongodb&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-6.4-red?style=flat-square&logo=redis&logoColor=white)
![HTTPX](https://img.shields.io/badge/HTTPX-0.28-purple?style=flat-square)
![Docker](https://img.shields.io/badge/Docker-ready-blue?style=flat-square&logo=docker&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active_Development-brightgreen?style=flat-square)

</div>

---

## About The Project

SwipeBot is an enterprise-grade Telegram bot that acts as the messaging front-end of an existing apartment-rental REST API. It lets real-estate agents and clients register and log in, browse a paginated announcements feed, view geolocation on a map, and publish fully-detailed apartment listings — all without leaving Telegram.

The target audience is a commercial real-estate platform's end users (clients, renters and agents) who want a low-friction, mobile-first way to interact with the service. SwipeBot solves the discovery and publishing problem by moving the entire user journey into Telegram, removing the need for a dedicated mobile app.

## Key Tech Stack

| Layer | Technologies |
|-------|--------------|
| **Backend / Bot Framework** | Python 3.12, aiogram 3.21 (async) |
| **Database** | MongoDB via PyMongo 4.14 (async driver) |
| **Caching / State** | Redis 6.4 (async — FSM storage) |
| **API Integration** | HTTPX 0.28 (async HTTP client) |
| **Localization** | Babel 2.17 / gettext (EN, UK) |
| **Tooling & Deployment** | Poetry, Docker (multi-stage, `python:3.12-slim`) |

## Core Features

- **Authentication & Registration** — FSM-driven email/password registration and login with strict field validation (name, email, Ukrainian phone `+380…`, password strength); registration summary with per-field editing before submit.
- **JWT Session Management** — access/refresh tokens stored per user in MongoDB with automatic refresh-token rotation on `400/401` responses.
- **Announcements Feed** — paginated listing feed with photo, price/area/floor details, inline navigation and one-tap geolocation (shared location on a map).
- **Announcement Creation Wizard** — a 28-step guided form: viewing time, address, district, shared geolocation, construction/ownership/property attributes, kitchen area, heating, mortgage/balcony options, agent commission, condition, finishing, call method, description, price, floor-plan scheme and a photo gallery (with Telegram album/media-group support).
- **User Profile** — full account screen with contact info, agent contact, balance, subscription (with formatted expiry date) and notification settings.
- **My Announcements** — user's own listings with paginated browsing.
- **Multi-language UI** — English and Ukrainian via Babel/gettext, with per-user locale persisted in the database.
- **Session Middleware** — automatic user provisioning on first contact and a global auth gate that redirects unauthenticated users to the start menu.
- **Centralized Error Handling** — unified API error formatting into localized user-facing messages; session invalidation on auth failures.

## Architecture & Engineering Highlights

- **Layered, modular monolith** — clear separation of concerns: `handlers/` (Routers), `middlewares/`, `keyboards/`, `states/` (FSM), `callbacks/`, `api/` (API client), `database/` (repository), `utilities/`, `filters/`.
- **Repository pattern over async MongoDB** — a single `Repository` abstraction (`bot/database/repository.py`) centralizes all persistence; `TypedDict`/`dataclass` schemas keep documents typed, and a custom `dict_factory` excludes `None` values from partial updates.
- **Redis-backed FSM storage** — every multi-step flow (registration, login, announcement creation) runs on aiogram's `RedisStorage`, making wizard state durable and bot instances horizontally stateless.
- **Automatic token rotation** — a single authorized-request path in the `APIClient` retries any `400/401` once after refreshing the JWT pair, transparent to the caller.
- **`RequestContext` async context manager** — scopes an `httpx.AsyncClient` to a single handler invocation and centralizes error translation: `400–404` log the user out and reset state, other errors are formatted from the API's error schema into localized messages.
- **Middleware chain** — `AuthMiddleware` (auth gate + auto-provisioning), `CustomI18nMiddleware` (DB-driven locale selection), and `AlbumMiddleware` (debounced media-group coalescing so multi-photo uploads arrive as one album).
- **i18n-first UI** — all strings use `gettext`/`lazy_gettext` with per-user locale lookup, compiled to `.mo` catalogs at build time.
- **Engineering details** — cache-busting query params on Telegram media URLs to avoid stale previews, typed callback-data filters for inline navigation, and consistent async I/O throughout.

## Quick Start

### Prerequisites

- Python **3.12+**
- [Poetry](https://python-poetry.org/) (dependency management)
- A running **MongoDB** instance and a **Redis** instance
- A Telegram **Bot Token** from [@BotFather](https://t.me/BotFather)
- The base URL of the **real-estate REST API** this bot integrates with

### Local setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/SwipeBot.git
   cd SwipeBot
   ```

2. **Configure environment variables**

   Copy the template and fill in your values:

   ```bash
   cp .env.example .env
   ```

   | Variable | Description |
   |----------|-------------|
   | `BOT_TOKEN` | Telegram bot token from BotFather |
   | `REDIS_URI` | Redis connection URI (e.g. `redis://localhost:6379/0`) |
   | `MONGO_URI` | MongoDB connection URI (e.g. `mongodb://localhost:27017`) |
   | `API_URI` | Base URL of the backend REST API |

3. **Install dependencies and run**

   ```bash
   poetry install
   poetry run python -m bot
   ```

   Alternatively, with a classic virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r <(poetry export -f requirements.txt --without-hashes)
   python -m bot
   ```

### Docker deployment

The repository ships a multi-stage `Dockerfile` (`python:3.12-slim`) that exports dependencies with Poetry, installs them, compiles the locale catalogs and runs the bot:

```bash
docker build -t swipebot .
docker run --env-file .env swipebot
```

For a one-command local environment, a `docker-compose.yml` is expected to orchestrate the bot along with its MongoDB and Redis services:

```bash
docker-compose up --build
```

## API Endpoints Overview

The bot consumes the following REST API (base URL from `API_URI`):

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/auth/user/register` | Create a new user account, returns JWT pair |
| `POST` | `/auth/user/login` | Authenticate and receive a JWT pair |
| `POST` | `/auth/tokens/refresh` | Rotate an expired access token using the refresh token |
| `GET` | `/announcements` | Paginated announcements feed (`limit`, `offset`) |
| `GET` | `/user/announcements` | Paginated list of the user's own announcements |
| `GET` | `/user/profile` | Current user profile, balance, subscription and contacts |
| `POST` | `/user/apartments` | Create an apartment (with gallery base64 payload) |
| `POST` | `/user/announcements` | Publish an announcement for an apartment |

All endpoints except `/auth/*` are called with a `Bearer` access token; the client transparently handles refresh-token rotation.

## Future Roadmap

- **Docker Compose orchestration** — ship a `docker-compose.yml` defining `bot`, `mongodb` and `redis` services for truly one-command local development and staging deployments.
- **Connection pooling & client reuse** — replace per-request `httpx.AsyncClient` creation with a shared, long-lived connection pool to reduce handshake overhead, and introduce a Redis cache layer for the announcements feed and profile data.
- **Automated test suite** — add unit and integration tests (mock API responses, repository fixtures, FSM flow tests) to lock in the registration, login and announcement-creation flows.
