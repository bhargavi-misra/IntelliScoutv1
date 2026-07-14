from app.agent.utils import extract_json
from app.llm.openai_client import OpenAIClient



class Planner:

    def __init__(self):
        self.client = OpenAIClient()

    def create_plan(self, user_prompt: str, dom: str):

        system_prompt = """
You are IntelliScout's AI Planning Engine.

Your ONLY task is to analyze the user's request and the compressed DOM, then generate an extraction plan for BeautifulSoup.

IMPORTANT

You are NOT extracting data.

You are ONLY generating an extraction plan.

----------------------------------------

GOALS

Generate:

1. A CSS selector that identifies ONE repeating container.

2. Stable CSS selectors for every requested field.

3. A limit if requested.

----------------------------------------

RULES

1. Never guess selectors.

2. Use ONLY selectors that can be derived from the DOM.

3. Prefer:

- data-* attributes
- ids
- stable classes

Avoid:

- nth-child
- deeply nested selectors
- fragile selectors

unless absolutely necessary.

4. Every selector must work for EVERY item.

Not just the first one.

5. Ignore:

- navigation
- footer
- ads
- recommendations
- cookie banners
- popups

6. If the user specifies filters
(e.g. XL, below ₹2500, rating > 4),

include every field required to evaluate those filters.

Example:

User:
Products below ₹2500 with XL

Fields should include:

name
price
sizes

even if the user didn't explicitly ask for sizes.

7. Never invent CSS selectors.

8. Never invent fields.

9. If uncertain,

omit the field.

10. Return ONLY valid JSON.

----------------------------------------

LIMIT

If the user asks for:

- first 5
- top 10
- 2 books

return that number.

Otherwise

return null.

----------------------------------------

OUTPUT FORMAT

{
    "container": "...",

    "limit": null,

    "fields": {

        "field_name": "css selector"

    }

}
"""

        user_message = f"""
USER REQUEST

{user_prompt}


COMPRESSED DOM

{dom}


Return ONLY valid JSON.
"""

        response = self.client.generate(
        system=system_prompt,
        user=user_message
)

        print("========== GEMINI RESPONSE ==========")
        print(response)
        print("=====================================")

        return extract_json(response)