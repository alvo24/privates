# Affiliate Link Posting System (with Key Validation)

This repository contains a production-oriented **starter implementation** for an automated affiliate marketing workflow.

## What it does

- Securely stores third-party API credentials (encrypted at rest).
- Validates API credentials by making lightweight verification calls.
- Fetches affiliate product metadata from a URL (title/description/price/image).
- Generates social post copy + hashtags.
- Schedules or immediately dispatches posts to multiple social channels.
- Collects post analytics through provider adapters.

## Architecture

- **FastAPI** service layer for key management and workflow orchestration.
- **Adapter interfaces** for social networks and affiliate data providers.
- **Encryption service** (`Fernet`) for credential protection.
- **Background scheduler** (`APScheduler`) for delayed publishing jobs.
- **Analytics service** for provider metric normalization.

## How to run

### 1) Setup

```bash
make setup
```

If you prefer manual setup:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Start API server

```bash
make run
```

Or manually:

```bash
source .venv/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 3) Open docs

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Quick API examples

### Health check

```bash
curl http://127.0.0.1:8000/health
```

### Validate/store a platform key

```bash
curl -X POST http://127.0.0.1:8000/api/keys/validate \
  -H "Content-Type: application/json" \
  -d '{
    "platform": "facebook",
    "account_id": "acct-1",
    "api_key": "12345678_valid_example",
    "api_secret": "secret-value",
    "access_token": "token-value"
  }'
```

### Preview affiliate product metadata

```bash
curl -X POST http://127.0.0.1:8000/api/affiliate/preview \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/product"}'
```

### Post immediately

```bash
curl -X POST http://127.0.0.1:8000/api/posts/dispatch \
  -H "Content-Type: application/json" \
  -d '{
    "platforms": ["facebook", "linkedin"],
    "affiliate_url": "https://example.com/product",
    "message": "Limited-time deal!"
  }'
```

### Run tests

```bash
make test
```

## Security Notes

- Set a strong `APP_MASTER_KEY` in environment variables.
- Never hardcode credentials.
- Rotate keys regularly.
- Use platform OAuth flows in production where possible.

## Important Disclaimer

Some platforms (especially Instagram/Facebook/LinkedIn/X) have strict API and automation policies.
You must comply with each platform's terms of service and affiliate disclosure requirements.
