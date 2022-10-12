import json
import gspread
from odoo import api, exceptions, fields, models, _


class GoogleSpreadsheet:
    scopes = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']  # TODO - move to config

    def connect(self, credentials: object) -> gspread.Client:
        try:
            credentials_json = json.loads(credentials.spreadsheet_credentials)
            # scopes = json.loads(credentials.scopes).get('scopes')
            if not credentials_json:
                raise exceptions.UserError(_('No credentials or scopes. Please fill required fields.'))
            conn = gspread.service_account_from_dict(credentials_json, scopes=self.scopes)
            return conn
        except Exception as ex:
            print(ex)
