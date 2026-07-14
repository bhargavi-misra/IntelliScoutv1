from urllib.parse import urljoin

from bs4 import BeautifulSoup


class Extractor:

    def extract(
        self,
        html: str,
        plan: dict,
    ):

        soup = BeautifulSoup(html, "html.parser")

        results = []

        container_selector = plan.get("container")

        if not container_selector:
            raise ValueError("Planner did not return a container selector.")

        containers = soup.select(container_selector)

        limit = plan.get("limit")

        if limit is not None:
            containers = containers[:limit]

        fields = plan.get("fields", {})

        for container in containers:

            item = {}

            for field, selector in fields.items():

                if not selector:
                    item[field] = None
                    continue

                element = container.select_one(selector)

                if element is None:
                    item[field] = None
                    continue

                value = None

                field_lower = field.lower()

                # -----------------------------
                # URL fields
                # -----------------------------
                if (
                    "url" in field_lower
                    or "link" in field_lower
                    or field_lower.endswith("_href")
                ):

                    href = element.get("href")

                    if href:
                        value = urljoin("", href)

                # -----------------------------
                # Image fields
                # -----------------------------
                elif (
                    "image" in field_lower
                    or "thumbnail" in field_lower
                    or field_lower.endswith("_src")
                ):

                    src = (
                        element.get("src")
                        or element.get("data-src")
                        or element.get("data-lazy-src")
                    )

                    if src:
                        value = urljoin("", src)

                # -----------------------------
                # Default: text
                # -----------------------------
                else:

                    value = " ".join(
                        element.get_text(
                            separator=" ",
                            strip=True,
                        ).split()
                    )

                item[field] = value

            # Skip completely empty rows
            if any(v is not None and v != "" for v in item.values()):
                results.append(item)

        return results