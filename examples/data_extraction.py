import os
import marvin

from typing import Optional
from pydantic import BaseModel

TOKEN = os.environ["API_TOKEN"]
BASE_URL = "https://openai-proxy.sellestial.com/api"

marvin.settings.openai.api_key = TOKEN
marvin.settings.openai.base_url = BASE_URL
marvin.settings.openai.chat.completions.model = "gpt-4-turbo"


class Person(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    job_title: Optional[str]
    company_name: Optional[str] 


def main():
    """
    Main function
    """

    # Marvin docs: https://www.askmarvin.ai/docs/text/transformation/

    signature = """
John Doe
Manager @ DragonHack
"""

    person = marvin.cast(signature, target=Person)

    print(person)


if __name__ == "__main__":
    main()
