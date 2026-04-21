from app.adapters.social import get_adapter
from app.schemas.models import KeyValidationRequest
from app.storage.key_store import KeyStore
from app.utils.security import EncryptionManager


class CredentialService:
    def __init__(self) -> None:
        self.encryption = EncryptionManager()
        self.store = KeyStore()

    def validate_and_store_key(self, request: KeyValidationRequest) -> dict:
        adapter = get_adapter(request.platform.value)
        result = adapter.validate_credentials(request.api_key, request.access_token)

        if result.valid:
            encrypted = {
                "api_key": self.encryption.encrypt(request.api_key),
                "api_secret": self.encryption.encrypt(request.api_secret) if request.api_secret else None,
                "access_token": self.encryption.encrypt(request.access_token) if request.access_token else None,
            }
            self.store.save(request.platform.value, request.account_id, encrypted)

        return {
            "platform": request.platform,
            "account_id": request.account_id,
            "status": result.status,
            "valid": result.valid,
            "detail": result.detail,
        }
