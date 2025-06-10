from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
from urllib.parse import urlparse, parse_qs

summarizer = pipeline("summarization", model="csebuetnlp/mT5_small_finetuned_summarize-news")


def extract_video_id(url):
    query = urlparse(url).query
    params = parse_qs(query)
    return params.get("v", [None])[0]

def summarize_text(video_url):
    video_id = extract_video_id(video_url)
    if not video_id:
        raise ValueError("Nie można znaleźć ID filmu w URL.")

    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["pl", "en"])
    full_text = " ".join([entry["text"] for entry in transcript])

    if len(full_text) > 1000:
        full_text = full_text[:1000]

    summary = summarizer(full_text, max_length=130, min_length=30, do_sample=False)
    return summary[0]["summary_text"]
