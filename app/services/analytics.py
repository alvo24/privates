from app.adapters.social import get_adapter


class AnalyticsService:
    def fetch_metrics(self, platform: str, post_id: str) -> dict:
        adapter = get_adapter(platform)
        metrics = adapter.fetch_metrics(post_id)
        return {
            "platform": platform,
            "metrics": metrics,
        }
