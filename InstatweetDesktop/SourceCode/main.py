from selenium import webdriver
import pyautogui
import time
from selenium.webdriver.common.keys import Keys

import instapy_cli as client

from instabot import Bot

import tweepy


print("InstaTweet\n")



accounts_number = input("How many accounts do you have: ")

post_description = input("Post description: ")

accounts = []
passwords = []
accounts_type = []

consumer_keys = []
consumer_secrets = []
keys = []
secret_keys = []

instagram_pics = []
tweet_pics = []

i = 1


while i <= int(accounts_number):
    account_type = input(f"Account {i} type: ")
    account_name = input(f"Account {i} name: ")
    account_password = input(f"Account {i} password: ")
    if(account_type == "tweet"):
        tweet_pic = input(f"Tweet picture filename (ex: picture.png) for account {i}: ")
        consumer_key = input(f"Twitter API consumer key for account {i}: ")
        consumer_secret = input(f"Twitter API consumer secret key for account {i}: ")
        key = input(f"Twitter API access token for account {i}: ")
        secret = input(f"Twitter API access token secret for account {i}: ")
        consumer_keys.append(consumer_key)
        consumer_secrets.append(consumer_secret)
        keys.append(key)
        secret_keys.append(secret)
        tweet_pics.append(tweet_pic)
        instagram_pics.append("")
    elif(account_type == "insta"):
        insta_pic = input(f"Instagram post picture filename (ex: picture.png) for account {i}: ")
        instagram_pics.append(insta_pic)
        consumer_keys.append("")
        consumer_secrets.append("")
        keys.append("")
        secret_keys.append("")

    accounts.append(account_name)
    passwords.append(account_password)
    accounts_type.append(account_type)
    i += 1


def PostTwitter(consumer_key, consumer_secret, key, secret, filename):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(key, secret)

    api = tweepy.API(auth)

    api.update_with_media(f"TwitterPhoto/{filename}", post_description)

    mentions = api.mentions_timeline()

    for mention in mentions:
        print(str(mention.id) + " - " + mention.text)

def PostInstagram(username, password, filename):
    bot = Bot()

    bot.login(username=username, password=password)

    bot.upload_photo(f"InstaPhoto/{filename}", caption=post_description)
j = 0

while j < int(accounts_number):
    print(accounts_type[j])

    if(accounts_type[j] == "insta"):
        PostInstagram(username=accounts[j], password=passwords[j], filename=instagram_pics[j])
    elif(accounts_type[j] == "tweet"):
        PostTwitter(consumer_keys[j], consumer_secrets[j], keys[j], secret_keys[j], tweet_pics[j])
    j += 1


