#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# Import modules
from bs4 import BeautifulSoup
from requests import get
from fake_useragent import UserAgent
from colorama import Fore

# Load user agents
user_agent = UserAgent()
def GetHeaders():
    return {
        "User-Agent": user_agent.random,
        "Connection": "keep-alive",
        "Host": "animeidhentai.com",
        "Referer": "https://animeidhentai.com"
    }

# Get list with hentai
def GetList(query):
    videos = []
    pageNumber = 0
    print(f"\n{Fore.GREEN}[*]{Fore.YELLOW} Searching video's using \"{query}\" as search query. {Fore.RESET}")
    while True:
        pageNumber += 1
        print(f"{Fore.GREEN}[+]{Fore.YELLOW} Loading data from page {pageNumber}...{Fore.RESET}")
        # Get page content
        page = get(f"https://animeidhentai.com/search/{query}/page/{pageNumber}")
        # If end
        if "The page you are looking for does not exist..." in page.text:
            print(f"{Fore.GREEN}[+]{Fore.YELLOW} Scanning completed.{Fore.RESET}")
            break
        # Parse html
        soup = BeautifulSoup(page.content, "html.parser")
        list = soup.find(class_ = "movies-lst").find_all("li")
        # Fetch all links
        for target in list:
            # Find url, title, categories
            url = target.find("a")["href"]
            title = target.find(class_ = "entry-title").string
            categories = target.find(class_ = "categories").text
            # Add
            videos.append({"title": title, "categories": categories, "url": url})

    print(f"{Fore.BLUE}[?] {Fore.MAGENTA}Found {len(videos)} hentai videos ;){Fore.RESET}")
    return videos