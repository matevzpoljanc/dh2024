# DragonHack 2024 code samples

Code samples to aid with AI

## Access
You can access OpenAI's API by proxying your requests through our proxy server https://openai-proxy.sellestial.com/api.
The easiest way to do this is to set ```base_url``` argument in **openai**'s client:

```
BASE_URL = "https://openai-proxy.sellestial.com/api"

client = openai.OpenAI(api_key=TOKEN, base_url=BASE_URL)
```

In case you don't have api key for our proxy, come to Sellestial's table and collect yours.

Examples read key from env variable:
```
export API_TOKEN=<you-token>
```

## Installation
```
pip install poetry
poetry install
```

# AI Code samples
## Chat
Sample chat directly using OpenAI's python library

## Marvin
[Marvin](https://www.askmarvin.ai/welcome/what_is_marvin/) is a library which provides a very helpful abstraction for implmenting AI-based logic in Python.

It's amazingly easy to process text and implement AI classifiers, AI data extractors, even AI functions