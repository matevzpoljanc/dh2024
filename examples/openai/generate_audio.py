

import os
import openai

TOKEN = os.environ["API_TOKEN"]
BASE_URL = "https://openai-proxy.sellestial.com/api"


def main():
    """
    Main function
    """

    # OpenAI docs: https://platform.openai.com/docs/guides/text-to-speech

    client = openai.OpenAI(api_key=TOKEN, base_url=BASE_URL)

    audio = client.audio.speech.create(
        model="tts-1-hd",
        input="Ladies and gentlemen, welcome to DragonHack 2024!",
        voice="alloy",
    )
    audio.stream_to_file("welcome.mp3")


if __name__ == "__main__":
    main()