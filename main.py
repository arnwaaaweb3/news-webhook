import requests, feedparser, time

WEBHOOK_URL = "https://discord.com/api/webhooks/1362251264326631435/ZW4Wn3OL2k-8R1PWxdx4O9JKIyGUKfTRyc5c1RVsKv9Va3emfmaVv4TZhFtjNkH_JX1I"

RSS_FEEDS = [
    "https://rss.app/feeds/Q5fY1ufKM5h0qUqq.xml",
    "https://rss.app/feeds/Iuu11qViSentddWI.xml",
    "https://rss.app/feeds/7TiZTimdzhX5lrDY.xml",
    "https://rss.app/feeds/LE4rb9El1JmZmej5.xml",
    "https://rss.app/feeds/E5PzUy5JBTERIKMw.xml",
    "https://rss.app/feeds/yzcgA0FIQxpkauvS.xml",
    "https://rss.app/feeds/VQGwB80jCYCHH3bj.xml",
    "https://rss.app/feeds/jxtlGnxgHk1xuicw.xml",
    "https://rss.app/feeds/1wQOoB7NgJpx0DNB.xml"
]

posted_links = set()

def fetch_and_post():
    for url in RSS_FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            if entry.link not in posted_links:
                post_to_discord(entry.title, entry.link)
                posted_links.add(entry.link)

def post_to_discord(title, link):
    data = {
        "username": "Bullnaut",
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
