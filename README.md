# AI Content Generator

A FastAPI-based utility exposing endpoints for AI-powered content rewriting and prompt building, using OpenAI's API.

## Features

- **/rewrite**: Rewrite content for a given scenario using OpenAI (ChatGPT) models.
- **/build-prompt**: Generate detailed prompts for use with AI tools like Copilot or ChatGPT.
- **API Key Security**: All endpoints require an API key via the `x-api-key` header.
- **Environment-based configuration**: All secrets and model settings are loaded from a `.env` file.

## Supported AI Tools

- [OpenAI GPT-3.5, GPT-4, etc.](https://platform.openai.com/docs/models)
- Prompts generated are compatible with tools like [GitHub Copilot](https://github.com/features/copilot), [ChatGPT](https://chat.openai.com/), and other LLM-based assistants.

## Quickstart

1. **Clone the repo and install dependencies:**

   ```sh
   git clone https://github.com/yourusername/ai-content-generator.git
   cd ai-content-generator
   pip install -r requirements.txt
   ```

2. **Set up your `.env` file:**

   ```env
   OPENAI_API_KEY=your_openai_api_key
   # OPENAI_MODEL=gpt-3.5-turbo
   API_KEY=your_secret_api_key
   ```

3. **Run the server:**

   ```sh
   uvicorn main:app --reload
   ```

4. **Test the endpoints:**
   - `/rewrite` (POST): Rewrite content for a scenario
   - `/build-prompt` (POST): Build a detailed prompt for AI tools

## Example curl

**Rewrite:**

```sh
curl -X POST "http://127.0.0.1:8000/rewrite" \
  -H "Content-Type: application/json" \
  -H "x-api-key: your_secret_api_key" \
  -d '{"content": "The sky is blue.", "scenario": "Make it sound poetic."}'
```

**Build Prompt:**

```sh
curl -X POST "http://127.0.0.1:8000/build-prompt" \
  -H "Content-Type: application/json" \
  -H "x-api-key: your_secret_api_key" \
  -d '{"scenario": "Summarize a technical article", "context": "The article is about FastAPI deployment best practices."}'
```

## License

MIT
