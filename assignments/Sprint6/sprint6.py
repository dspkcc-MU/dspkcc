import os
import google.oauth2.credentials

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

CREDENTIALS_FILE = "credentials.json"
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'

def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
    credentials = flow.run_console()
    return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)
    
def translate(service, phrase):
    sheet = service.spreadsheets()
    spreadsheet = {
        'properties': {
            'title': 'translator'
        }
    }
    print('Creating sheet...')
    spreadsheet = sheet.create(body=spreadsheet,fields='spreadsheetId').execute()
    spreadsheet_id = spreadsheet.get('spreadsheetId')
 
    values = [
        [
            phrase, '=GOOGLETRANSLATE(A2, "en", "de")'
        ],
    ]
    body = {
        'values': values
    }
    print('Translating phrase...')
    result = service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id, range='A2:B2',
        valueInputOption='USER_ENTERED', body=body).execute()
 
    print('Retrieving translation...')
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range='B2').execute()
    rows = result.get('values', [])
 
    print('Original: {}'.format(phrase))
    print('Translation: {}'.format(rows[0][0]))
 
    print('Done')
    

if __name__ == '__main__':
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    service = get_authenticated_service()
    translate(service, 'Hello World')