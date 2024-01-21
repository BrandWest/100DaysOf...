import pandas as pd
import datetime as dt



class Birthday():
    def __init__(self):
        super().__init__()
        self.filepath = r'~/codingProjects/python/udemy/Day32 - SMTP-daytime/project/birthday_wisher/data/birthdays.csv'
        self.birthday_dict = {}


    def open_birthday_list(self):
        self.birthday_df = pd.read_csv(self.filepath)
        self.csv_dict = self.birthday_df.to_dict()


    def get_paramters(self):
        for index in range (len(self.csv_dict["name"])):
            name = self.csv_dict['name'][index]
            email = self.csv_dict['email'][index]
            year = self.csv_dict['year'][index]
            month = self.csv_dict['month'][index]
            day = self.csv_dict['day'][index]
            self.birthday_dict.update({
                name: {
                    "email": email,
                    "year": year,
                    "month": month,
                    "day": day
                }
            })


    def get_datetime(self):
        self.now = dt.datetime.now()
        self.this_year = self.now.year
        