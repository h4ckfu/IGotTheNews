# IGotTheNews

This is the code I use to grab the news every week.

It basically cycles through some news sources and collects keywords and counts how many times it finds each one.

This is just the first in a set of scripts I use to get a handle on the zietgiest; more to come.

As of now the idea is to:
    run collect_news.py to gather the news from the sources
    run process_news.py to manipulate the text files, make the DataFrame, and save out the csv file
    run archive_news.py to clean up

When I get this to the state where I am happy with it I'll make a igtn.py to run everything