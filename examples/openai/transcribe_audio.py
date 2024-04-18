

import os
import openai

TOKEN = os.environ["API_TOKEN"]
BASE_URL = "https://openai-proxy.sellestial.com/api"


def main():
    """
    Main function
    """

    # OpenAI docs: https://platform.openai.com/docs/guides/speech-to-text/quickstart?lang=python

    client = openai.OpenAI(api_key=TOKEN, base_url=BASE_URL)

    mp3_file = "speech-1.mp3" # replace with path to your audio file

    with open(mp3_file, "rb") as file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1", file=file
        )
    print(transcription.text)


if __name__ == "__main__":
    main()