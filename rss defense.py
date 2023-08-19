import requests, re
from bs4 import BeautifulSoup

website_links = ["https://www.defense.gov/DesktopModules/ArticleCS/RSS.ashx?ContentType=400&Site=945&max=10"]

rss_feeds = []

def check_for_real_rss(url):
    base_url = re.search('^(?:https?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)?([^:\/\n]+)',url).group(0)
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    for e in soup.select('[type="application/rss+xml"],a[href*=".rss"],a[href$="feed"]'):
        if e.get('href').startswith('/'):
            rss = (base_url+e.get('href'))
        else:
            rss = (e.get('href'))
        if 'xml' in requests.get(rss).headers.get('content-type'):
            rss_feeds.append(rss)

for url in website_links:
    soup = BeautifulSoup("features=lxml",requests.get(url).text)
    for e in soup.select('a[href*="rss"],a[href*="/feed"],a:-soup-contains-own("RSS")'):
        if e.get('href').startswith('/'):
            check_for_real_rss(url.strip('/')+e.get('href'))
        else:
            check_for_real_rss(e.get('href'))
set(rss_feeds)
