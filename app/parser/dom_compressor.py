from bs4 import BeautifulSoup, Tag


class DOMCompressor:
    """
    Converts cleaned HTML into a compact tree representation
    suitable for sending to an LLM.
    """

    IMPORTANT_TAGS = {
        "body",
        "main",
        "section",
        "article",
        "div",
        "ul",
        "ol",
        "li",
        "table",
        "thead",
        "tbody",
        "tr",
        "td",
        "th",
        "span",
        "p",
        "a",
        "img",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "form",
        "input",
        "button",
    }

    IMPORTANT_ATTRIBUTES = {
        "href",
        "src",
        "alt",
        "title",
        "aria-label",
        "placeholder",
        "type",
        "name",
    }

    MAX_TEXT_LENGTH = 80

    def compress(self, html: str) -> str:

        soup = BeautifulSoup(html, "html.parser")

        root = soup.body if soup.body else soup

        lines = []

        self._walk(root, lines, 0)

        return "\n".join(lines)

    def _walk(
        self,
        node: Tag,
        lines: list[str],
        depth: int,
    ):

        if not isinstance(node, Tag):
            return

        if node.name not in self.IMPORTANT_TAGS:
            for child in node.children:
                if isinstance(child, Tag):
                    self._walk(child, lines, depth)
            return

        # Skip wrapper divs with no useful metadata
        attrs = node.attrs or {}

        if (
            node.name == "div"
            and not attrs.get("id")
            and not attrs.get("class")
        ):

            tag_children = [
                child
                for child in node.children
                if isinstance(child, Tag)
            ]

            if len(tag_children) == 1:
                self._walk(tag_children[0], lines, depth)
                return

        lines.append(
            "  " * depth + self._format_node(node)
        )

        for child in node.children:
            if isinstance(child, Tag):
                self._walk(
                    child,
                    lines,
                    depth + 1,
                )

    def _format_node(
        self,
        node: Tag,
    ) -> str:

        attrs = node.attrs or {}

        result = node.name

        # -----------------------------
        # ID
        # -----------------------------
        node_id = attrs.get("id")

        if isinstance(node_id, str) and node_id:
            result += f"#{node_id}"

        # -----------------------------
        # Classes
        # -----------------------------
        classes = attrs.get("class", [])

        if isinstance(classes, str):
            classes = [classes]

        filtered_classes = []

        for cls in classes:

            if not isinstance(cls, str):
                continue

            if (
                len(cls) < 30
                and not cls.startswith(("css-", "sc-"))
            ):
                filtered_classes.append(cls)

        if filtered_classes:
            result += "".join(
                f".{cls}"
                for cls in filtered_classes
            )

        # -----------------------------
        # Important attributes
        # -----------------------------
        for attr in self.IMPORTANT_ATTRIBUTES:

            value = attrs.get(attr)

            if isinstance(value, list):
                value = " ".join(map(str, value))

            if value is not None:

                value = str(value)

                if len(value) > 80:
                    value = value[:80] + "..."

                result += f' [{attr}="{value}"]'

        # -----------------------------
        # Useful data-* attributes
        # -----------------------------
        for attr, value in attrs.items():

            if not attr.startswith("data-"):
                continue

            if isinstance(value, list):
                value = " ".join(map(str, value))

            if value is None:
                continue

            value = str(value)

            if len(value) > 60:
                continue

            result += f' [{attr}="{value}"]'

        # -----------------------------
        # Leaf text
        # -----------------------------
        has_tag_child = any(
            isinstance(child, Tag)
            for child in node.children
        )

        if not has_tag_child:

            text = node.get_text(
                separator=" ",
                strip=True,
            )

            text = " ".join(text.split())

            if text:

                if len(text) > self.MAX_TEXT_LENGTH:
                    text = text[: self.MAX_TEXT_LENGTH] + "..."

                result += f" -> {text}"

        return result