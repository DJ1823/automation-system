import json
from gmail_service import get_gmail_service
from sheets_service import get_sheets_service, append_row
from email_parser import extract_email_data
from config import STATE_FILE

def load_state():
    if not STATE_FILE or not open(STATE_FILE, "a+"):
        return None
    try:
        with open(STATE_FILE) as f:
            return json.load(f).get("last_id")
    except:
        return None

def save_state(msg_id):
    with open(STATE_FILE, "w") as f:
        json.dump({"last_id": msg_id}, f)

def main():
    gmail = get_gmail_service()
    sheets = get_sheets_service(gmail._http.credentials)

    last_id = load_state()

    query = "is:unread"
    results = gmail.users().messages().list(
        userId="me",
        q=query
    ).execute()

    messages = results.get("messages", [])

    for msg in messages:
        if msg["id"] == last_id:
            break

        message = gmail.users().messages().get(
            userId="me",
            id=msg["id"],
            format="full"
        ).execute()

        row = extract_email_data(message)
        append_row(sheets, row)

        gmail.users().messages().modify(
            userId="me",
            id=msg["id"],
            body={"removeLabelIds": ["UNREAD"]}
        ).execute()

        save_state(msg["id"])

if __name__ == "__main__":
    main()
