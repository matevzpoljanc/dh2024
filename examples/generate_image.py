import os
import openai

TOKEN = os.environ["API_TOKEN"]
BASE_URL = "https://openai-proxy.sellestial.com/api"


def main():
    """
    Main function
    """

    # OpenAI docs: https://platform.openai.com/docs/guides/images?context=node

    client = openai.OpenAI(api_key=TOKEN, base_url=BASE_URL)

    response = client.images.generate(
        model="dall-e-3",
        prompt="A painting of a car in the style of Picasso",
        size="1024x1024",
        quality="hd",
    )
    
    image_url = response.data[0].url
    print(image_url)


if __name__ == "__main__":
    main()