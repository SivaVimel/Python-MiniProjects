import time
import tweepy
from textblob import TextBlob
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

print("Welcome to Tweet Sentiment Analysis")
#getting user id
driver = webdriver.Chrome()
driver.get('https://www.codeofaninja.com/tools/find-twitter-id/#:~:text=How%20to%20use%3F&text=Put%20your%20username%20(without%20%40%20sign,appear%20in%20the%20green%20box.')

username = driver.find_element(By.ID,'username')
un = input("Enter The Username : ")
username.send_keys(un)

driver.find_element(By.XPATH,'//*[@id="find-twitter-id"]').click()
time.sleep(5)

idName = driver.find_element(By.XPATH,'//*[@id="answer"]/h3/span')
print("The User_ID for "+un+" is : "+idName.text)

#extracting tweets
client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAEPVlgEAAAAAo6N%2FWNsIk08gzQ%2B2PDRTpvEjBYA%3DDlomdTm0wzdVYVx2s3MXGXcyNNFAUwtVBcfCIjz6X3dbCkp4fJ')
id = idName.text
tweets = client.get_users_tweets(id=id, tweet_fields=['context_annotations','created_at','geo'])
print("Following are the recent tweets of "+un+" :")
print()

#cleaning
a = []
for tweet in tweets.data:
    clean = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", str(tweet)).split())
    a.append(clean)
    
#Analysis
for r in a:
    analysis = TextBlob(r)
    if analysis.sentiment.polarity > 0:
        print("Sentiment Analysis for "+r+" states as :")
        print('positive')
    elif analysis.sentiment.polarity == 0:
        print("Sentiment Analysis for "+r+" states as :")
        print('neutral')
    else:
        print("Sentiment Analysis for "+r+" states as :")
        print('negative')
    print()