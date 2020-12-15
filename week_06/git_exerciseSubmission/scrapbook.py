# %%

# The request library will grab the page
import requests
# The beautifulsoup library makes your code legible and helps you analyze the extracted page
import bs4

import pandas as pd

import re

# %%

soup = bs4.BeautifulSoup(response.text, 'html.parser')

response = requests.get("https://en.wikipedia.org/wiki/Pikachu")

soup

# %%

# next inspect the elements on the wiki page
soup.find_all('a', href=True)

# %%

links_dict = {}

# The soup.find_all('a', href=True) call finds all <a> elements that have an href attribute; elements without the attribute are skipped.
for link in soup.find_all('a', href=True, class_="external text", title=str):
    links_dict[link["href"]] = link.text

links_dict

# %%

# tuts: https://datatofish.com/dictionary-to-dataframe/
# make dataframe from a dict
df = pd.DataFrame(list(links_dict.items()),columns = ['url','description'])

# set display max row
pd.set_option('display.max_rows', 100)
df

# %%

"""Sometimes you have paren ( ) groupings in the pattern, but which you do not want to extract. In that case, write the parens with a ?: at the start, e.g. (?: ) and that left paren will not count as a group result.

Without (?: ) will get warning:

/opt/anaconda3/lib/python3.7/site-packages/pandas/core/strings.py:1952: UserWarning: This pattern has match groups. To actually get the groups, use str.extract.
return func(self, args, *kwargs)"""

# remove url that is not secured and start without https
pattern = re.compile(r'(?:^http:)|(?:^//w{3})')
filter = df['url'].str.contains(pattern)

# drop column that match regex pattern
df.drop(index=df[filter].index, inplace=True)

# reset index
pd.set_option('display.max_rows', 100)
df = df.reset_index(drop=True)

df
