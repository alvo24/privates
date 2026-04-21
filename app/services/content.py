class ContentService:
    def generate_post(self, product: dict, custom_message: str | None = None) -> str:
        base = custom_message or f"🔥 {product['title']}\n{product['description']}"
        price = f"\n💵 Price: {product['price']}" if product.get("price") else ""
        hashtags = "\n#Affiliate #Deals #ShopNow"
        return f"{base}{price}{hashtags}"
