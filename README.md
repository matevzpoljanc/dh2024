# DragonHack 2024 code samples

Code samples to aid with incorporating AI in your hacks

## Access

### Proxy
You can access OpenAI's API by proxying your requests through our proxy server.
The easiest way to do this is to set ```base_url``` argument in **openai**'s client:

```
BASE_URL = "https://openai-proxy.sellestial.com/api"

client = openai.OpenAI(api_key=TOKEN, base_url=BASE_URL)
```

### API key for proxy

In case you don't have api key for our proxy, come to Sellestial's table and collect yours.

Example code reads the key from env variable:
```
export API_TOKEN=<you-token>
```

## Installation
```
pip install poetry
poetry install
```

# AI Code examples
## OpenAI client: chat, image, audio
Sample chat, text-to-speech, speech-to-text and image generation directly using OpenAI's python library

## Marvin
[Marvin](https://www.askmarvin.ai/welcome/what_is_marvin/) is a library which provides a very helpful abstraction for implmenting AI-based logic in Python.

It's amazingly easy to process text and implement AI classifiers, AI data extractors, even AI functions