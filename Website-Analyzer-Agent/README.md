## 🌐 Website Analyzer Agent

A Python-based intelligent crawler that fetches and analyzes any website to return:

* 🌍 Domain & IP Info
* 🧠 Tech Stack Used
* 🏷️ Meta Tags (Title, Description)
* 🧾 WHOIS Details
* 🧱 SEO Structure (Headings, Links, Favicon)
* 🔍 External Scripts & Assets
* 📊 Internal vs External Link Count

> ✅ Ideal for developers, marketers, SEO analysts, and auditors.

---

### 🚀 Features

* ✅ **HTML Scraping** with `BeautifulSoup`
* 🌐 **Tech Detection** using `builtwith`
* 🔒 **WHOIS Lookup** with `python-whois`
* 🧠 **Full Metadata Analysis** (title, desc, headings)
* 📊 **Asset Scan** (scripts, styles, images, favicon)
* 🔗 **Link Categorization** (internal/external)
* 🔧 CLI interface for quick testing

---

### 📦 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

Requirements include:

* `requests`
* `beautifulsoup4`
* `tldextract`
* `builtwith`
* `python-whois`

---

### 🛠️ Usage

Run the analyzer from terminal:

```bash
python website_analyzer.py
```

You'll be prompted to enter a website URL:

```
Enter website URL: https://example.com
```

Output: A structured JSON report.

---

### 🖼️ Screenshot / Photo Idea

You can use a **dashboard-style banner**:

* **Left:** World icon 🌐 + HTML/CSS/JS logos
* **Center:** “Website Analyzer Agent”
* **Right:** JSON-style snippet of output




