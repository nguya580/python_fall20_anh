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
def list_to_string(list, string_name):
    ''' this function convert list to string, because newsapi uses string for input '''
    string_name = ', '.join(list)

# %% codecell
def news_searchengine():
    print('''The application helps you search for news articles from the last 30 days.
Your results will be saved as a CSV file as "news_fromkeyword_python.csv". \n''')

    keyword = input(str('Enter a keyword you want to search: '))

    #sources list in English in the US
    sources_list = ['abc-news', 'bbc-news', 'bloomberg', 'business-insider', 'cbs-news', 'cnn', 'google-news', 'nbc-news', 'new-york-magazine', 'politico', 'reuters', 'the-verge', 'the-wall-street-journal', 'the-washington-post', 'the-washington-times', 'time', 'vice-news']

    #use function to convert list to string
    src_tostring = ''
    list_to_string(sources_list, src_tostring)

    #check if string from sources_list is print out correctly
    # print(src_tostring)

    top_headlines = newsapi.get_top_headlines(q = keyword, sources = src_tostring)
    # print(top_headlines)

    #creat and open a cvs file
    csv_file = open('news_fromkeyword_python.csv', 'w')
    csv_writer = csv.writer(csv_file)

    #the first row of csv file
    csv_writer.writerow(['Published date', 'Title', 'Summary', 'Link'])

    for article in top_headlines['articles']:
        date = article['publishedAt']
        print('Published date: ' + date)

        headline = article['title']
        print('Title: ' + headline)

        summary = article['description']
        print('Summary: ' + summary + '\n')

        link = article['url']
        print('Link: ' + link + '\n\n')

        #write row for every founded article
        csv_writer.writerow([date, headline, summary, link])

    csv_file.close()

# %% codecell
#news_searchengine()
news_searchengine()
