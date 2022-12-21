# Author Nam-Phuong Tran github: https://github.com/phuongtrannam
# Version 1.0
# Python running version recommended 3.8 or above
# Realize the function: input the ieee keywords you want to search, and output the titles, abstracts, retrieval dates, keywords, and article homepages of all articles found.

from get_articlelist import airtcle_list
from get_information import get_article, get_title, get_abstract, get_published, get_date, get_kwd, get_citation_number, get_year
import pandas as pd 

# Enter search keywords
searchword = input('Search:')

# get list of articles
Airtcle_List = airtcle_list(searchword)
list_long = len(Airtcle_List)
print(list_long)
df = pd.DataFrame(columns=['index', 'type', 'year', 'title','abstract','publication_title','publication_date','keywords','citation_number','url'])

for airtcle_number in Airtcle_List:
    num_article = len(df.index)
    page_text = get_article(airtcle_number)
    print (str ( num_article +1 ) +  '/'  +  str ( list_long ))
    title = get_title(page_text)
    abstract = get_abstract(page_text)
    published = get_published(page_text)
    publication_date = get_date(page_text)
    publication_year = get_year(page_text)
    keywords = get_kwd(page_text)
    citation_number = get_citation_number(page_text)
    url = 'https://ieeexplore.ieee.org/document/' + str(airtcle_number)
    df.loc[num_article] = [num_article+1, 'Journal', publication_year, title, abstract, published, publication_date, keywords, citation_number, url]

df.to_csv('results1.csv', index=False)

print('Finish!')
