import csv
from pathlib import Path
from datetime import datetime


class CSVExporter:

    def export(
        self,
        items: list[dict]
    ) -> Path:

        if not items:
            raise ValueError("No items to export.")

        exports_dir = Path("exports")
        exports_dir.mkdir(exist_ok=True)

        filename = f"extraction_{datetime.now():%Y%m%d_%H%M%S}.csv"

        output_path = exports_dir / filename

        fieldnames = list(items[0].keys())

        with open(
            output_path,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(items)

        return output_path