# %% codecell

# import requests and json
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

#https://www.geeksforgeeks.org/removing-stop-words-nltk-python/
#Natural Language Toolkit
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# %% codecell

#stopwords.words('english') gives a list of unwanted words in English
print(stopwords.words('english'))

# %% codecell

#API key and setting for the community api
#https://developer.nytimes.com/docs/community-api-product/1/routes/user-content/url.json/get
api_key = "03Q77oAuM8UocuAmO9MwGeuV65h1KQeD"
article_url = "https://www.nytimes.com/2020/11/19/opinion/anthony-fauci-covid-interview.html"
sort = "newest"

# %% codecell

# show the API url with all the settings listed out
api_url = (f"https://api.nytimes.com/svc/community/v3/user-content/url.json?api-key={api_key}&url={article_url}&offset=0")
print(api_url)

# calling the API with requests
response = requests.get(api_url)

# creating a variable called data to hold the json formatted result
data = response.json()

# %% codecell

# isolate just the comments dictionary
comments_data = data['results']['comments']

#use pd to chart out the comments info
comments_df = pd.DataFrame(comments_data)
comments_df

#display all 26 columns
pd.set_option('display.max_columns', 26)

# %% codecell

# look at just one of the comments
#store comment index in a variable
comment = comments_df.loc[14, 'commentBody']

comment

# %% clean text data from comment

# convert comment to a string value
comment = str(comment)

#test if comment is a str or not
# print(type(comment))

comment_lower = comment.lower()

# print(comment13_lower)

unwanted = ['?', ':', ',', '!', ';', '...', '.', '\'', '"']

txt = comment_lower
for char in unwanted:
        txt = txt.replace(char, '')

# print(txt)

#Sets are used to store multiple items in a single variable.
stop_words = set(stopwords.words('english')) #a set of stopwords words in English
#prepare txt string into a list to filter through
txt_token = word_tokenize(txt)

#filter thru the list of txt_token then add word if it is not unwanted.
filtered_txt = []
for word in txt_token:
    if word not in stop_words:
        filtered_txt.append(word)

#convert list to string
txt_str = ' '.join(filtered_txt)

print(txt_str)

# %% prep text to dict for visualization
# sample_txt = ['apple', 'pear', 'kiwi', 'apple', 'mango', 'kiwi']

txt_data = {}

for word in filtered_txt:
    if word in txt_data:
        txt_data[word] += 1
    else:
        txt_data[word] = 1

print(txt_data)

# %% codecell

words_x = []
frequency_y = []

words_x = list(txt_data.keys())
frequency_y = list(txt_data.values())

plt.figure(figsize=(30, 10))  #figsize=(width, height)
plt.bar(words_x, frequency_y, align = 'center')

plt.xticks(rotation = 'vertical', fontsize = 18)
plt.yticks(fontsize = 18)

plt.tight_layout()
plt.style.use('seaborn-darkgrid')

plt.xlabel('Words in mentioned order', fontsize = 26, labelpad = 50, color = 'blue')
plt.ylabel('Frequency', fontsize = 26, labelpad = 50, color = 'blue')

plt.title('Frequency of words within a comment in article "When Will We Throw Our Masks Away? I Asked Dr. Fauci" by Elisabeth Rosenthal', fontsize = 26, pad = 20, color = 'blue')

plt.show()
