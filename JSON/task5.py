import json

with open('wiki_info.json') as jfile :
    wiki = json.load(jfile) 
    #wiki bu yerda wiki_info.json faylning ichidagi malumot

title = wiki['query']['pages']['13801']['title']
extract = wiki['query']['pages']['13801']['extract']
info = f'{title} \n{extract}'

print(info)
