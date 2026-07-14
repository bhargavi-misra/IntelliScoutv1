from playwright.sync_api import sync_playwright, TimeoutError


class Browser:

    def get_html(self, url: str) -> str:

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=True
            )

            page = browser.new_page(
                viewport={
                    "width": 1440,
                    "height": 900,
                }
            )

            page.goto(
                url,
                wait_until="domcontentloaded",
                timeout=60000,
            )

            try:

                page.wait_for_load_state(
                    "networkidle",
                    timeout=10000,
                )

            except TimeoutError:

                print(
                    "Network idle timed out. Falling back to DOMContentLoaded..."
                )

            # Give React/Vue/Next.js pages time to render
            page.wait_for_timeout(5000)

            html = page.content()

            browser.close()

            return html