import yagmail
import pandas
import datetime

from dotenv import dotenv_values
from news import NewsFeed


class Main:

    todays_date_str = None
    yesterday_date_str = None
    df = None

    def __init__(self):
        self.setup()

    def setup(self):
        todays_date = datetime.datetime.today()
        yesterday_date = todays_date - datetime.timedelta(days=1)

        self.todays_date_str = todays_date.strftime('%Y-%m-%d')
        self.yesterday_date_str = yesterday_date.strftime('%Y-%m-%d')

        self.df = pandas.read_excel('people.xlsx')

    def send_mail(self, row):
        news_feed = NewsFeed(interest=row['interest'],
                             from_date=self.yesterday_date_str,
                             to_date=self.todays_date_str)

        yag = yagmail.SMTP(user=dotenv_values('.env').get('MAIN_GMAIL_ACCOUNT'),
                           password=dotenv_values('.env').get('MAIN_GMAIL_PASSWORD'))

        yag.send(to=row['email'],
                 subject=f'Your {row['interest']} new for today!',
                 contents=f'Hi {row['name']}\nSee what is on about {row['interest']} today.\n{news_feed.get()}\nSincerely, En!')

    def run(self):
        for _, row in self.df.iterrows():
            self.send_mail(row)


Main().run()
