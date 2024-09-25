# Hitzeneu API

This project is a simple and incomplete API that allows you to translate a text from english to basque. It uses the [HiTZ machine translation EN-EU model](https://huggingface.co/HiTZ/mt-hitz-en-eu) and is inspired by the [Libre Translate API](https://libretranslate.com/).

## Usage

To use the API, you need to send a POST request to the `/translate` endpoint with the following JSON body:

```json
{
    "q": "Hello, how are you?",
    "source": "en",
    "target": "eu"
}
```

- `q`: The text you want to translate.
- `source`: The language of the text you want to translate (default: `en`).
- `target`: The language you want to translate the text to (default: `eu`).

The API will return a JSON response with the translated text:

```json
{
    "translatedText": "Kaixo, zer moduz zaude?"
}
```

Example using `curl`:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"q": "Hello, how are you?", "source": "en", "target": "eu"}' http://localhost:5000/translate
```

## Deployment with Docker (recommended)

First, clone the repository:

```bash
git clone https://github.com/xezpeleta/hitzeneu_api.git
cd hitzeneu_api
```

Then, build the Docker image:

```bash
docker compose build
docker compose up
```

The API will be available at `http://localhost:5000/translate`.


## Installation

First, clone the repository:

```bash
git clone https://github.com/xezpeleta/hitzeneu_api.git
cd hitzeneu_api
```

Then, create a virtual environment and install the dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Finally, start the server:

```bash
python app.py
```

The API will be available at `http://localhost:5000/translate`.
