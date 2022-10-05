import gspread


class GoogleSpreadsheet:
    scopes = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']  # TODO - move to settings

    def connect(self, filename: str) -> gspread.Client:
        try:
            conn = gspread.service_account(filename=filename, scopes=self.scopes)
            return conn
        except Exception as ex:
            print(ex)
