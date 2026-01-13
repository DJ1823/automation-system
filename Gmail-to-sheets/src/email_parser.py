import base64
from bs4 import BeautifulSoup

def extract_email_data(message):
    headers = message["payload"]["headers"]

    def get_header(name):
        for h in headers:
            if h["name"] == name:
                return h["value"]
        return ""

    body = ""
    if "parts" in message["payload"]:
        for part in message["payload"]["parts"]:
            if part["mimeType"] == "text/plain":
                body = base64.urlsafe_b64decode(
                    part["body"]["data"]
                ).decode("utf-8")
            elif part["mimeType"] == "text/html":
                html = base64.urlsafe_b64decode(
                    part["body"]["data"]
                ).decode("utf-8")
                body = BeautifulSoup(html, "html.parser").get_text()

    return [
        get_header("From"),
        get_header("Subject"),
        get_header("Date"),
        body.strip()
    ]
