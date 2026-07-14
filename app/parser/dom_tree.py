from bs4 import BeautifulSoup


class DOMTree:

    def simplify(self, html: str) -> str:

        soup = BeautifulSoup(html, "html.parser")

        lines = []

        def walk(node, depth=0):

            if not getattr(node, "name", None):
                return

            lines.append("  " * depth + node.name)

            for child in node.children:
                walk(child, depth + 1)

        walk(soup.body)

        return "\n".join(lines)