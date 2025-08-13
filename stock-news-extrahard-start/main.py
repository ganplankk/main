from datetime import datetime, timedelta
import requests
import json
from twilio.rest import Client

from urllib3.fields import format_multipart_header_param

API_KEY = "V4KIC4S97BCUQKL2"
NEWS_API_KEY = "e8ac3a931e2645618c2ea4e9d0193e5c"
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEW_ENDPOINT = "https://newsapi.org/v2/everything"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=parameters)
response.raise_for_status()

current_date = datetime.now()
before_4_days = (current_date - timedelta(days=4)).strftime('%Y-%m-%d')

current_day = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in current_day.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']

day_before_yesterday_data = data_list[1]
day_before_yesterday_data_closing_price = day_before_yesterday_data['4. close']

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_data_closing_price))
diff_percent = (difference/float(yesterday_closing_price)) * 100

if diff_percent > 1:
    new_param = {
        'qInTitle': 'tesla',
        'apiKey': NEWS_API_KEY
    }

    news_response = requests.get(NEW_ENDPOINT, new_param)
    articles = news_response.json()['articles']
    three_articles = articles[:3]
    # send_data = [(a.get('title'), a.get('url')) for a in three_articles if a.get('title' and a.get('url'))]
    # send_data = [(a.get("title"), a.get("url"))
    #              for a in three_articles
    #              if a.get("title") and a.get("url")]
    formatted_articles = [f"Headline: {article['title']}.\nBrief: {article['description']}" for article in three_articles]


    # print(json.dumps(news, indent=2))
    # for i in range(0,3):
    #     print(f"Title : {news['articles'][i]['title']}, \nURL: {news['articles'][i]['url']}")

# new_data = 0
# for i in (0, 4):
#     for data in data_list[i]['4. close']:
#         data -
#         if new_data < data:
#             new_data = data
#             print(new_data)


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

