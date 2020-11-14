# %% codecell
from newsapi import NewsApiClient
import csv

# Init
newsapi = NewsApiClient(api_key='fdde27f8887d4a01bf80ebfe6a20295e')

# %% codecell
sources = newsapi.get_sources()

#check how many news media id the API offers
# for source in sources['sources']:
#     print(source['id'] + '\n' + source['language'] + '\n' + source['country'] + '\n\n')

# %% codecell
# def list_to_string(list, string_name):
#     ''' this function convert list to string, because newsapi uses string for input '''
#     string_name = ', '.join(list)

# %% codecell

# en_us_news = []
def list_to_string(list, string_name):
    ''' this function convert list to string, because newsapi uses string for input '''
    string_name = ', '.join(list)


def getnews_en_us(list, output_list):
    ''' this function get a list of news sources in English within the US '''

    en_us_filter = []

    #filter through to get a list of source in en and US
    for source in list:
        if source["language"] == "en" and source["country"] == "us":
            en_us_filter.append(source)

    en_us_filter

    #filter only the source ID in en and US
    output_list = []
    for item in en_us_filter:
        id = item['id']
        output_list.append(id)

getnews_en_us(sources['sources'], en_us_news)

news_en_us = en_us_news

# src_tostring = ', '.join(en_us_news)
#
# src_tostring

list_to_string(news_en_us, src_tostring)
src_tostring
