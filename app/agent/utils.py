import json
import re


def extract_json(text: str) -> dict:
    """
    Extracts and parses a JSON object from an LLM response.

    Handles responses like:

    ```json
    {
        ...
    }
    ```

    or

    Here is the JSON:

    {
        ...
    }

    Returns:
        dict: Parsed JSON object.

    Raises:
        ValueError: If no valid JSON is found.
    """

    if not text:
        raise ValueError("LLM returned an empty response.")

    # Remove markdown code fences
    text = re.sub(r"```json", "", text, flags=re.IGNORECASE)
    text = re.sub(r"```", "", text)

    text = text.strip()

    # Find the first JSON object
    match = re.search(r"\{.*\}", text, re.DOTALL)

    if not match:
        raise ValueError("No JSON object found in LLM response.")

    json_string = match.group()

    try:
        return json.loads(json_string)

    except json.JSONDecodeError as e:
        raise ValueError(
            f"Failed to parse JSON returned by the LLM.\n\n"
            f"Extracted JSON:\n{json_string}"
        ) from e