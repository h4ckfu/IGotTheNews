# coding: utf-8

import newspaper
import time
from time import gmtime, strftime
from string import punctuation
from collections import Counter, OrderedDict
import operator
from time import sleep
import logging

# These are all just helper functions, I'm sure they can be done more efficently
# I just hacked them together 

def save_crawl(crawl_list, news_name):
  
    file_name = 'data/crawl_list-' + news_name +'_alt.data'

    with open(file_name, 'w') as out_f:
        for li in crawl_list:
            w = "'" + li + "',"
            out_f.write(w)
    pass


def save_keywords(keyword_list, news_name):

    try:
        file_name = 'data/keyword_list-' + news_name +'_alt.data'
        flat_list = [i for row in keyword_list for i in row]

        with open(file_name, 'w') as out_f:
            for li in flat_list:
                w = "'" + li + "',"
                out_f.write(w)
    except:
        print (f'could not load' {news_name})
        logging.error('save_keywords failed, prolly empty keyword list')

    pass


def word_counts(keyword_list):
    c = dict(Counter(x[0] for x in keyword_list if x))
    return sorted(c.items(), key=lambda x: x[1], reverse=True)


def get_articles(paper_name):

    crawl_list = []

    for article in paper_name.articles:
        crawl_list.append(article.url)

    return crawl_list


def get_keywords(paper_name):

    keyword_list = []

    if len(crawl_list) > 0:

        for words in paper_name.articles:

            try:
                words.download()
                words.parse()
                words.nlp()

            except :
                logging.warning('Get Keywords Failed')
                pass

            keyword_list.append(words.keywords)

        return keyword_list

    else:
        print ('add logging and throw error')
        pass


if __name__ == "__main__":

    logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

    # Make the Dictonary to feed to helper functions
    names_and_urls={
                "mashable": "http://mashable.com",
                "cleveland": "http://www.cleveland.com",
                "religious": "http://www.religionnews.com",
                "sbnation": "http://www.sbnation.com",
                "huffpo": "https://www.huffingtonpost.com/",
                "atlantic": "http://theatlantic.com",
                "telegram": "http://telegram.com"}

    c=0

    # Iterate thro that dic
    for k, v in names_and_urls.items():

        # An instance of newspaper with the url
        np_build = newspaper.build(v, language='en')

        # get the article urls and keywords
        crawl_list = get_articles(np_build)
        keyword_list = get_keywords(np_build)
        
        #save them
        save_crawl(crawl_list, k)
        save_keywords(keyword_list, k)

        # Record Progress and Pause
        c += 1
        sleep(1)

        print(f"On Loop {c} - processing {k}")