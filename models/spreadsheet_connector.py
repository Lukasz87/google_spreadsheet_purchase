import json
import gspread
from odoo import api, exceptions, fields, models, _
import pandas as pd

class GoogleSpreadsheet:
    scopes = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']  # TODO - move to config

    def __init__(self, credentials):
        self.conn = self.connect(credentials)

    def connect(self, credentials: str) -> gspread.Client:
        credentials_json = json.loads(credentials)
        # scopes = json.loads(credentials.scopes).get('scopes')
        if not credentials_json:
            raise exceptions.UserError(_('No credentials or scopes. Please fill required fields.'))
        conn = gspread.service_account_from_dict(credentials_json, scopes=self.scopes)
        return conn

    def get_spreadsheet(self, spreadsheet_id: str):
        spreadsheet = self.conn.open_by_key(spreadsheet_id)
        # dataframe = pd.DataFrame(spreadsheet.get_all_records())
        return spreadsheet
