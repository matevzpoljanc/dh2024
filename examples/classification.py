import os
import marvin

from pydantic import BaseModel


TOKEN = os.environ["API_TOKEN"]
BASE_URL = "https://openai-proxy.sellestial.com/api"

marvin.settings.openai.api_key = TOKEN
marvin.settings.openai.base_url = BASE_URL
marvin.settings.openai.chat.completions.model = "gpt-4-turbo"


def main():
    """
    Main function
    """

    # Marvin docs: https://www.askmarvin.ai/docs/text/classification/

    message = """
Hi support!

The app crashes when I try to upload a file."

Please help,
Matevz
"""

    category = marvin.classify(
        message,
        labels=["bug", "feature request", "inquiry"],
    )

    print(category)


if __name__ == "__main__":
    main()
