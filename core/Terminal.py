#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Import modules
from os import system, name
from colorama import Fore

# Clear screen
def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")

# Logo
def logo():
    print(f"""
    {Fore.MAGENTA}
  _,  _, _ _, _ ___   __, __, ___  _, _,_ __, __,
 (_  /_\ | |\ |  |    |_  |_   |  / ` |_| |_  |_)
 , ) | | | | \|  |    |   |    |  \ , | | |   | \\
  ~  ~ ~ ~ ~  ~  ~    ~   ~~~  ~   ~  ~ ~ ~~~ ~ ~
                           {Fore.BLUE} > Created By LimerBoy                   
    {Fore.RESET}
    """)