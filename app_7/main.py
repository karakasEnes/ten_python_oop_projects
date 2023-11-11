import yagmail
import pandas
import  datetime

from dotenv import dotenv_values
from news import NewsFeed



todays_date = datetime.datetime.today()
yesterday_date = todays_date - datetime.timedelta(days=1)

todays_date_str = todays_date.strftime('%Y-%m-%d')
yesterday_date_str = yesterday_date.strftime('%Y-%m-%d')

df = pandas.read_excel('people.xlsx')

for index, row in df.iterrows():
    news_feed = NewsFeed(interest=row['interest'], from_date=yesterday_date_str, to_date=todays_date_str)

    yag = yagmail.SMTP(user=dotenv_values('.env').get('MAIN_GMAIL_ACCOUNT'),
                       password=dotenv_values('.env').get('MAIN_GMAIL_PASSWORD'))

    yag.send(to=row['email'],
             subject=f'Your {row['interest']} new for today!',
             contents=f'Hi {row['name']}\nSee what is on about {row['interest']} today.\n{news_feed.get()}\nSincerely, En!')
