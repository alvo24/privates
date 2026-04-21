import base64
import os

from cryptography.fernet import Fernet


class EncryptionManager:
    def __init__(self) -> None:
        raw = os.getenv("APP_MASTER_KEY")
        if raw is None:
            raw = base64.urlsafe_b64encode(os.urandom(32)).decode("utf-8")
        self._fernet = Fernet(raw.encode("utf-8"))

    def encrypt(self, plaintext: str) -> str:
        return self._fernet.encrypt(plaintext.encode("utf-8")).decode("utf-8")

    def decrypt(self, ciphertext: str) -> str:
        return self._fernet.decrypt(ciphertext.encode("utf-8")).decode("utf-8")
