from bs4 import BeautifulSoup, Tag, Comment


class DOMCleaner:

    REMOVE_TAGS = [
        "script",
        "style",
        "noscript",
        "svg",
        "canvas",
        "iframe",
        "header",
        "footer",
        "nav",
        "aside",
    ]

    REMOVE_KEYWORDS = [
        "cookie",
        "consent",
        "banner",
        "popup",
        "modal",
        "newsletter",
        "advert",
        "ads",
        "sponsored",
        "social",
        "share",
        "recommend",
        "related",
        "recently-viewed",
    ]

    def clean(self, html: str) -> str:

        soup = BeautifulSoup(html, "html.parser")

        # Remove unwanted tags
        for tag in self.REMOVE_TAGS:
            for node in soup.find_all(tag):
                node.decompose()

        # Remove noisy elements
        for element in soup.find_all(True):

            if not isinstance(element, Tag):
                continue

            attrs = element.attrs or {}

            element_id = attrs.get("id", "")

            classes = attrs.get("class", [])

            if isinstance(classes, str):
                classes = [classes]

            attributes = " ".join(
                [
                    str(element_id),
                    " ".join(map(str, classes))
                ]
            ).lower()

            if any(
                keyword in attributes
                for keyword in self.REMOVE_KEYWORDS
            ):
                element.decompose()

        # Remove HTML comments
        for comment in soup.find_all(
            string=lambda text: isinstance(text, Comment)
        ):
            comment.extract()

        return soup.prettify()