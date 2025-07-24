import requests
from bs4 import BeautifulSoup, Comment

def fetch_clean_text_html(url: str, output_file: str):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/114.0.0.0 Safari/537.36"
        )
    }

    print(f"🔍 Fetching: {url}")
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Only extract content from <body>
    body = soup.body
    if not body:
        print("❌ No <body> tag found.")
        return

    # Remove undesired tags within body
    for tag in body(["script", "style", "svg", "nav", "title"]):
        tag.decompose()

    # Remove comments
    for comment in body.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()

    # Unwrap layout tags like <div>, <section>, etc.
    for tag in body.find_all(["div", "section", "header", "footer", "aside", "main"]):
        tag.unwrap()

    # Remove all attributes (classes, ids, styles, etc.)
    for tag in body.find_all(True):
        tag.attrs.clear()

    # Format and write only the inner content of <body>
    cleaned_html = "\n".join(str(child) for child in body.contents if str(child).strip())

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(cleaned_html)

    print(f"✅ Cleaned HTML body content saved to: {output_file}")


if __name__ == "__main__":
    fetch_clean_text_html(
        url="http://www.jabercrombia.com",
        output_file="cleaned-text.html"
    )
