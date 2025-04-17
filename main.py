import os
import requests
import feedparser
import time

# Ambil variabel dari environment (Railway Variables)
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
RSS_FEEDS_RAW = os.getenv("RSS_FEEDS")  # Nanti kita pisah pakai koma
USERNAME = os.getenv("BOT_NAME", "Bullnaut")

# Pecah RSS Feed jadi list
RSS_FEEDS = RSS_FEEDS_RAW.split(",") if RSS_FEEDS_RAW else []

posted_links = set()

def fetch_and_post():
    for url in RSS_FEEDS:
        feed = feedparser.parse(url.strip())
        for entry in feed.entries:
            if entry.link not in posted_links:
                post_to_discord(entry.title, entry.link)
                posted_links.add(entry.link)

def post_to_discord(title, link):
    data = {
        "username": USERNAME,
        "embeds": [{
            "title": title,
            "url": link,
            "color": 0xff9900
        }]
    }
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print(f"[✅ SENT] {title}")
    else:
        print(f"[❌ FAIL] {title} - Status {response.status_code}")

if __name__ == "__main__":
    while True:
        fetch_and_post()
        time.sleep(600)  # 10 menit
