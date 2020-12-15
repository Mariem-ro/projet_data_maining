#!/usr/bin/python
import tweepy
import csv #Import csv
auth = tweepy.auth.OAuthHandler('4CeiBlbUxiJ4Y8lAtulJ70ubG', 'M9tE6Dsx64M7CgW6rUSyPafCBXga7ys2qTjlndzzPUyJxGJ7NW')
auth.set_access_token('1335880208864473090-AajfwSraulNljrKxo4aLkFjVwd2FRD', 'rYpcm6k9mGakaHKOZWrkLhIj8MFiRW5ywJX1jtcvkLqHf')

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