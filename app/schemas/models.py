from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, HttpUrl


class Platform(str, Enum):
    facebook = "facebook"
    instagram = "instagram"
    x = "x"
    linkedin = "linkedin"


class KeyValidationRequest(BaseModel):
    platform: Platform
    account_id: str = Field(..., min_length=1)
    api_key: str = Field(..., min_length=8)
    api_secret: str | None = None
    access_token: str | None = None


class AffiliateLinkRequest(BaseModel):
    url: HttpUrl


class PostDispatchRequest(BaseModel):
    platforms: list[Platform]
    affiliate_url: HttpUrl
    message: str | None = None
    schedule_at: datetime | None = None


class ProductDetails(BaseModel):
    title: str
    description: str
    image_url: str | None = None
    price: str | None = None
