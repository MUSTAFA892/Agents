import requests
from bs4 import BeautifulSoup
import builtwith
import whois
import socket
import tldextract
from urllib.parse import urljoin, urlparse
import json
import time


def fetch_html(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        start_time = time.time()
        response = requests.get(url, headers=headers, timeout=10)
        load_time = time.time() - start_time
        return response.text, response.status_code, load_time, response.headers
    except Exception as e:
        return None, str(e), 0, {}


def extract_metadata(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.title.string.strip() if soup.title else ""
    description = ""
    if soup.find("meta", attrs={"name": "description"}):
        description = soup.find("meta", attrs={"name": "description"}).get("content", "")

    # Headings
    headings = {f"h{i}": [h.get_text(strip=True) for h in soup.find_all(f"h{i}")] for i in range(1, 7)}

    # Favicon
    icon_link = soup.find("link", rel=lambda x: x and 'icon' in x.lower())
    favicon = urljoin(base_url, icon_link['href']) if icon_link and icon_link.get('href') else ""

    # CMS Detection (common meta tag)
    generator = soup.find("meta", attrs={"name": "generator"})
    cms = generator['content'] if generator and generator.get("content") else "Unknown"

    # Count script and CSS files
    script_count = len(soup.find_all("script", src=True))
    css_count = len(soup.find_all("link", rel="stylesheet"))

    return {
        "title": title,
        "description": description,
        "headings": headings,
        "favicon": favicon,
        "cms": cms,
        "script_count": script_count,
        "css_count": css_count
    }


def detect_technologies(url):
    try:
        return list(builtwith.parse(url).keys())
    except Exception:
        return []


def get_whois_data(domain):
    try:
        return whois.whois(domain)
    except Exception as e:
        return {"error": str(e)}


def resolve_ip(domain):
    try:
        return socket.gethostbyname(domain)
    except Exception:
        return "Could not resolve"


def extract_links(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    internal, external = set(), set()
    base_domain = urlparse(base_url).netloc

    for a in soup.find_all('a', href=True):
        href = urljoin(base_url, a['href'])
        domain = urlparse(href).netloc
        if domain == base_domain:
            internal.add(href)
        else:
            external.add(href)

    return list(internal), list(external)


def analyze_site(url):
    html, status, load_time, headers = fetch_html(url)
    if not html:
        return {"error": f"Failed to fetch HTML: {status}"}

    ext = tldextract.extract(url)
    domain = f"{ext.domain}.{ext.suffix}"

    meta = extract_metadata(html, url)
    tech_stack = detect_technologies(url)
    whois_data = get_whois_data(domain)
    ip = resolve_ip(domain)
    internal_links, external_links = extract_links(html, url)

    return {
        "url": url,
        "status_code": status,
        "load_time_sec": round(load_time, 2),
        "response_headers": dict(headers),
        "title": meta["title"],
        "description": meta["description"],
        "favicon": meta["favicon"],
        "cms": meta["cms"],
        "script_file_count": meta["script_count"],
        "css_file_count": meta["css_count"],
        "ip": ip,
        "tech_stack": tech_stack,
        "whois": str(whois_data),
        "headings": meta["headings"],
        "internal_links_count": len(internal_links),
        "external_links_count": len(external_links)
    }


if __name__ == '__main__':
    input_url = input("Enter website URL: ")
    result = analyze_site(input_url)
    print(json.dumps(result, indent=2))
