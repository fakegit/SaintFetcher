#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# Import modules
from tabulate import tabulate
from colorama import Fore

# Select search query
def GetQuery():
    try:
        choice = input(f"\n {Fore.BLUE}-- {Fore.MAGENTA}Hi, just select a category. You can enter anything\n {Fore.BLUE}>> {Fore.MAGENTA}")
    except KeyboardInterrupt:
        raise SystemExit(f"\n{Fore.MAGENTA}[?] Exiting the program ...")
    else:
        return choice

# Select videos from table
def SelectFromTable(videos):
    headers = ["#", "Title", "Categories"]
    table = []
    id = 0
    for video in videos:
        id += 1
        table.append([
            f"{Fore.GREEN}{id}",
            f"{Fore.WHITE}{video['title']}",
            f"{Fore.YELLOW}{video['categories']}"
        ])

    print(tabulate(table, headers=headers, tablefmt="simple"))

    try:
        choice = int(input(f"\n {Fore.BLUE}-- {Fore.MAGENTA}Select a number from the table to start downloading\n {Fore.BLUE}>> {Fore.MAGENTA}"))
        return videos[choice - 1]
    except IndexError:
        raise SystemExit(f"{Fore.RED}[!] Video with number {choice} not exists in table")
    except ValueError:
        raise SystemExit(f"{Fore.RED}[!] You need to enter a numeric value")
    except KeyboardInterrupt:
        raise SystemExit(f"\n{Fore.MAGENTA}[?] Exiting the program ...")