#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# Import modules
from bs4 import BeautifulSoup
from requests import get, utils
from jsbeautifier import beautify
from fake_useragent import UserAgent
from colorama import Fore
from wget import download
from os import path, mkdir

# Load user agents
user_agent = UserAgent()
def GetHeaders():
    return {
        "User-Agent": user_agent.random,
        "Connection": "keep-alive",
        "Host": "animeidhentai.com",
        "Referer": "https://animeidhentai.com"
    }

# If "downloads" dir not exists
if not path.exists("downloads"):
    mkdir("downloads")

# Get direct url to download video
def FetchVideo(video):
    video_url = video["url"]
    video_page = get(video_url, headers=GetHeaders()).content
    soup = BeautifulSoup(video_page, 'html.parser')
    player_url = soup.find('iframe')['data-lazy-src']
    player_page = get(player_url, headers=GetHeaders()).content
    soup = BeautifulSoup(player_page, 'html.parser')
    obfuscated_js = soup.find_all('script')[4].string
    deobfuscated_js = beautify(obfuscated_js)
    l1 = deobfuscated_js.find("http")
    l2 = deobfuscated_js.find("\"\n    }],\n    aspectratio")
    direct_url = utils.unquote(deobfuscated_js[l1:l2])
    print(f"\n{Fore.GREEN}[>]{Fore.YELLOW} Downloading {video['title']}")
    local_file = download(direct_url, out="downloads/")
    print(f"\n{Fore.GREEN}[+]{Fore.YELLOW} Downloading completed. File saved: {local_file}{Fore.RESET}")
