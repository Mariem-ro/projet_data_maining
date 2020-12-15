#!/usr/bin/python
import tweepy
import csv #Import csv
auth = tweepy.auth.OAuthHandler('customer_key', 'customer_secret')
auth.set_access_token('access_token', 'access_token_secret')

api = tweepy.API(auth)

# Open/create a file to append data to
csvFile = open('tweet.csv', 'w',newline='')
#Use csv writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,
                           q = '*',
                           since = "2020-12-14",
                           until = "2020-12-15",
                           count=12000,
                           lang = "en").items():
    # Write a row to the CSV file. I use encode UTF-8
    csvWriter.writerow([tweet.id,tweet.created_at,tweet.favorite_count,tweet.retweet_count,tweet.text.encode('ascii', 'ignore').decode()])
    print (tweet.id,tweet.created_at,tweet.favorite_count,tweet.retweet_count, tweet.text)
csvFile.close()
