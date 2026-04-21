from bs4 import BeautifulSoup
import requests


class AffiliateService:
    def extract_product_details(self, url: str) -> dict:
        response = requests.get(url, timeout=8)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        title = self._content(soup, "meta[property='og:title']") or (soup.title.string.strip() if soup.title else "Product")
        description = self._content(soup, "meta[property='og:description']") or "Check out this product."
        image = self._content(soup, "meta[property='og:image']")
        price = self._content(soup, "meta[property='product:price:amount']")

        return {
            "title": title,
            "description": description,
            "image_url": image,
            "price": price,
        }

    @staticmethod
    def _content(soup: BeautifulSoup, selector: str) -> str | None:
        tag = soup.select_one(selector)
        return tag.get("content") if tag and tag.get("content") else None
