from dataclasses import dataclass

import requests


@dataclass
class ValidationResult:
    valid: bool
    status: str
    detail: str


class SocialAdapter:
    def validate_credentials(self, api_key: str, access_token: str | None = None) -> ValidationResult:
        raise NotImplementedError

    def publish_post(self, content: str, affiliate_url: str) -> dict:
        raise NotImplementedError

    def fetch_metrics(self, post_id: str) -> dict:
        raise NotImplementedError


class DemoSocialAdapter(SocialAdapter):
    """Demo adapter for API-key verification and posting flow.

    Replace this with native SDK/API implementations per provider.
    """

    def validate_credentials(self, api_key: str, access_token: str | None = None) -> ValidationResult:
        if len(api_key.strip()) < 8:
            return ValidationResult(valid=False, status="invalid", detail="API key is too short")

        # Lightweight online check to ensure network reachability.
        resp = requests.get("https://httpbin.org/status/200", timeout=5)
        if resp.status_code != 200:
            return ValidationResult(valid=False, status="offline", detail="Could not reach validation endpoint")

        return ValidationResult(valid=True, status="active", detail="Key format and connectivity checks passed")

    def publish_post(self, content: str, affiliate_url: str) -> dict:
        return {
            "post_id": "demo-post-123",
            "status": "published",
            "content": content,
            "affiliate_url": affiliate_url,
        }

    def fetch_metrics(self, post_id: str) -> dict:
        return {
            "post_id": post_id,
            "impressions": 1240,
            "engagements": 133,
            "clicks": 57,
            "ctr": 0.046,
        }


def get_adapter(platform: str) -> SocialAdapter:
    # Map provider -> adapter instance. For now, use demo adapter for all.
    return DemoSocialAdapter()
