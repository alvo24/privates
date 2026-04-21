from app.adapters.social import get_adapter
from app.schemas.models import PostDispatchRequest
from app.services.affiliate import AffiliateService
from app.services.content import ContentService


class DispatcherService:
    def __init__(self) -> None:
        self.affiliate_service = AffiliateService()
        self.content_service = ContentService()

    def publish_now(self, request: PostDispatchRequest) -> dict:
        product = self.affiliate_service.extract_product_details(str(request.affiliate_url))
        content = self.content_service.generate_post(product, request.message)

        results: dict[str, dict] = {}
        for platform in request.platforms:
            adapter = get_adapter(platform.value)
            results[platform.value] = adapter.publish_post(content, str(request.affiliate_url))

        return {
            "product": product,
            "generated_content": content,
            "platform_results": results,
        }
