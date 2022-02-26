import discord
import os
import requests
from bs4 import BeautifulSoup

def myrank(username):

    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }

    url = 'https://euw.op.gg/summoners/euw/' + username
    req = requests.get(url, headers=headers)

    soup = BeautifulSoup(req.content, features="html.parser")

    rank_tier = soup.find("div", class_="tier-rank").text
    lp = soup.find("span", class_="lp").text
    win_lose = soup.find("span", class_="win-lose").text
    rank = [rank_tier,lp,win_lose]
    return rank

myrank('Carlitooooo')
