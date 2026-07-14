from bs4 import BeautifulSoup


class DOMCleaner:

    REMOVE_TAGS = [
        "script",
        "style",
        "noscript",
        "svg",
        "canvas",
        "footer",
        "header",
        "nav",
        "iframe",
    ]

    def clean(self, html: str) -> str:

        soup = BeautifulSoup(html, "html.parser")

        for tag in self.REMOVE_TAGS:
            for node in soup.find_all(tag):
                node.decompose()

        return soup.prettify()