#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# Import modules
from core.FetchVideo import FetchVideo
from core.FetchList import GetList
from core.SelectVideo import SelectFromTable, GetQuery
from core.Terminal import clear, logo

# Main
if __name__ == "__main__":
    clear()
    logo()
    query = GetQuery()
    videos = GetList(query)
    video = SelectFromTable(videos)
    FetchVideo(video)