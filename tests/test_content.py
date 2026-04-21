from app.services.content import ContentService


def test_generate_post_contains_hashtags():
    service = ContentService()
    post = service.generate_post(
        {
            "title": "USB-C Hub",
            "description": "7-in-1 hub for laptops",
            "price": "$29.99",
        }
    )
    assert "#Affiliate" in post
