from fastapi import FastAPI

from app.schemas.models import (
    AffiliateLinkRequest,
    KeyValidationRequest,
    PostDispatchRequest,
)
from app.services.affiliate import AffiliateService
from app.services.analytics import AnalyticsService
from app.services.credentials import CredentialService
from app.services.dispatcher import DispatcherService
from app.services.scheduler import JobScheduler

app = FastAPI(title="Affiliate Link Posting System", version="0.1.0")

credential_service = CredentialService()
affiliate_service = AffiliateService()
dispatcher_service = DispatcherService()
analytics_service = AnalyticsService()
job_scheduler = JobScheduler(dispatcher_service)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/keys/validate")
def validate_key(request: KeyValidationRequest) -> dict:
    result = credential_service.validate_and_store_key(request)
    return result


@app.post("/api/affiliate/preview")
def affiliate_preview(request: AffiliateLinkRequest) -> dict:
    return affiliate_service.extract_product_details(request.url)


@app.post("/api/posts/dispatch")
def dispatch_post(request: PostDispatchRequest) -> dict:
    if request.schedule_at:
        job_id = job_scheduler.schedule_post(request)
        return {"status": "scheduled", "job_id": job_id}

    published = dispatcher_service.publish_now(request)
    return {"status": "posted", "results": published}


@app.get("/api/analytics/{platform}/{post_id}")
def get_analytics(platform: str, post_id: str) -> dict:
    return analytics_service.fetch_metrics(platform, post_id)
