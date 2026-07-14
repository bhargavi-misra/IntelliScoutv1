from pathlib import Path
import hashlib
import json
import re


class PlannerCache:

    def __init__(self):

        self.cache_dir = Path("cache")

        self.cache_dir.mkdir(exist_ok=True)

    def _normalize_prompt(
        self,
        prompt: str,
    ) -> str:
        """
        Reduce prompts to their meaningful intent.

        Removes punctuation, extra spaces,
        converts to lowercase.
        """

        prompt = prompt.lower()

        prompt = re.sub(
            r"[^a-z0-9\s]",
            " ",
            prompt,
        )

        prompt = " ".join(prompt.split())

        return prompt

    def _cache_key(
        self,
        url: str,
        prompt: str,
    ):

        normalized = self._normalize_prompt(prompt)

        return hashlib.sha256(
            f"{url}|{normalized}".encode()
        ).hexdigest()

    def _file(
        self,
        url: str,
        prompt: str,
    ):

        return self.cache_dir / (
            self._cache_key(url, prompt)
            + ".json"
        )

    def load(
        self,
        url: str,
        prompt: str,
    ):

        file = self._file(
            url,
            prompt,
        )

        if file.exists():

            with open(
                file,
                encoding="utf-8",
            ) as f:

                return json.load(f)

        return None

    def save(
        self,
        url: str,
        prompt: str,
        plan: dict,
    ):

        file = self._file(
            url,
            prompt,
        )

        with open(
            file,
            "w",
            encoding="utf-8",
        ) as f:

            json.dump(
                plan,
                f,
                indent=4,
                ensure_ascii=False,
            )