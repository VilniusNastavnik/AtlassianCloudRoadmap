import requests
from feedgen.feed import FeedGenerator

# Endpoint JSON reale della Atlassian Cloud Roadmap (Next.js)
URL = "https://www.atlassian.com/roadmap/cloud?category=agileDevOps;analytics;ai;itsm;platform;workManagement&selectedProduct=confluence;jsw;jiraService"

# Recupero del JSON
resp = requests.get(URL)
resp.raise_for_status()
data = resp.json()

# Navigazione del JSON secondo struttura Next.js
items = data["pageProps"]["workStreams"]

# Creazione feed
fg = FeedGenerator()
fg.title("Atlassian Cloud Roadmap – Feed Dinamico")
fg.link(href="https://www.atlassian.com/roadmap/cloud")
fg.description("Feed generato automaticamente dalla Roadmap Atlassian Cloud")

for ws in items:
    f = ws["fields"]

    title = f.get("title", "Untitled")
    desc = f.get("description", "Nessuna descrizione disponibile.")
    status = f.get("status", "Unknown")

    entry = fg.add_entry()
    entry.title(f"{title} [{status}]")
    entry.link(href="https://www.atlassian.com/roadmap/cloud")
    entry.description(desc)

# Salvataggio RSS
fg.rss_file("roadmap.xml")
