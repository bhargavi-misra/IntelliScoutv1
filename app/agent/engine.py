from app.agent.extractor import Extractor
from app.agent.planner import Planner
from app.browser.browser import Browser
from app.parser.dom_cleaner import DOMCleaner
from app.parser.dom_compressor import DOMCompressor
from app.cache.planner_cache import PlannerCache


class IntelliScoutEngine:

    def __init__(self):

        self.browser = Browser()
        self.cleaner = DOMCleaner()
        self.compressor = DOMCompressor()
        self.planner = Planner()
        self.extractor = Extractor()
        self.cache = PlannerCache()

    def extract(
        self,
        url: str,
        prompt: str,
    ):

        print("\n" + "=" * 70)
        print("🚀 STARTING EXTRACTION")
        print("=" * 70)

        # --------------------------------------------------
        # Step 1 : Download webpage
        # --------------------------------------------------

        print("\n📥 Downloading webpage...")

        html = self.browser.get_html(url)

        print(f"✅ HTML downloaded ({len(html):,} characters)")

        # --------------------------------------------------
        # Step 2 : Clean HTML
        # --------------------------------------------------

        print("\n🧹 Cleaning HTML...")

        cleaned_html = self.cleaner.clean(html)

        print(f"✅ Cleaned HTML ({len(cleaned_html):,} characters)")

        # Save cleaned HTML for debugging
        with open(
            "debug.html",
            "w",
            encoding="utf-8",
        ) as file:
            file.write(cleaned_html)

        print("💾 Saved cleaned HTML -> debug.html")

        # --------------------------------------------------
        # Step 3 : Compress DOM
        # --------------------------------------------------

        print("\n🗜 Compressing DOM...")

        compressed_dom = self.compressor.compress(cleaned_html)

        print(
            f"✅ Compressed DOM ({len(compressed_dom):,} characters)"
        )

        # Save compressed DOM
        with open(
            "compressed_dom.txt",
            "w",
            encoding="utf-8",
        ) as file:
            file.write(compressed_dom)

        print("💾 Saved compressed DOM -> compressed_dom.txt")

        # --------------------------------------------------
        # Step 4 : Planner Cache
        # --------------------------------------------------

        plan = self.cache.load(
            url,
            prompt,
        )

        if plan is not None:

            print("\n" + "=" * 70)
            print("🟢 Planner Cache HIT")
            print("=" * 70)

        else:

            print("\n" + "=" * 70)
            print("🟡 Planner Cache MISS")
            print("=" * 70)

            print("🤖 Asking Gemini to create extraction plan...")

            plan = self.planner.create_plan(
                prompt,
                compressed_dom,
            )

            self.cache.save(
                url,
                prompt,
                plan,
            )

            print("💾 Plan cached.")

        # --------------------------------------------------
        # Step 5 : Print Plan
        # --------------------------------------------------

        print("\n========== EXTRACTION PLAN ==========\n")
        print(plan)
        print("\n=====================================\n")

        # --------------------------------------------------
        # Step 6 : Extract
        # --------------------------------------------------

        print("📦 Running extractor...\n")

        items = self.extractor.extract(
            html=cleaned_html,
            plan=plan,
        )

        print(f"\n✅ Extracted {len(items)} items.")

        print("\n" + "=" * 70)
        print("🏁 EXTRACTION FINISHED")
        print("=" * 70 + "\n")

        return items