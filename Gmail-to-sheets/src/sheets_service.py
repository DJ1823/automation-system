from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from config import SCOPES, SPREADSHEET_ID, SHEET_NAME

def get_sheets_service(creds):
    return build("sheets", "v4", credentials=creds)

def append_row(service, values):
    body = {"values": [values]}
    service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=SHEET_NAME,
        valueInputOption="RAW",
        body=body
    ).execute()
