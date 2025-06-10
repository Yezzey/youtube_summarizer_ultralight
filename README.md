# YouTube Summarizer (UltraLight)

A simple, lightweight web app for summarizing YouTube videos using `distilbart`.

## Features
- Automatically fetches transcript (subtitles) from public YouTube videos
- Summarizes content using Hugging Face transformers
- Works without login or API keys

## How to Deploy on Render.com

1. Upload this ZIP to GitHub or push via git
2. Create a new **Web Service** on [Render.com](https://render.com)
3. Set **start command** to:

    ```
    gunicorn app:app
    ```

4. Use `POST /api/summarize` with JSON body:
    ```json
    {
        "video_url": "https://www.youtube.com/watch?v=XXXXXX"
    }
    ```

## Requirements
- Render Free Tier (512MB RAM)
- Python 3.9+

## Example
Try with:
https://www.youtube.com/watch?v=dQw4w9WgXcQ
