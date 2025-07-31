# AI Content Generator

This project is a FastAPI-based utility exposing a POST /rewrite endpoint that uses the Hugging Face Inference API to rewrite content based on a scenario.

## Features

- POST `/rewrite` endpoint
- Accepts JSON: `{ "content": <string>, "scenario": <string> }`
- Uses Hugging Face model (default: `mistralai/Mixtral-8x7B-Instruct-v0.1`)
- Model and token configurable via environment variables
- Returns: `{ "rewritten_content": <string> }`
- Error handling for API and input issues

## Setup

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Set your Hugging Face API token:
   ```sh
   export HF_TOKEN=your_hf_token
   ```
   Optionally set a different model:
   ```sh
   export HF_MODEL=your_model_name
   ```
3. Run the server:
   ```sh
   uvicorn main:app --reload
   ```

## Example Request

```
POST /rewrite
{
  "content": "The sky is blue.",
  "scenario": "Make it sound poetic."
}
```

## Example Response

```
{
  "rewritten_content": "Beneath the heavens, the sky unfurls its endless blue tapestry."
}
```
