import os 
from time import gmtime, strftime
import logging
import shutil

archive_date = str(strftime("%Y-%m-%d", gmtime()))
here = os.getcwd()

#tomorrow lets test this to make sure it runs correctly...
# This is overkill, but I am leaving it for future use..
root_files = os.listdir(here)
csv_source = here + '/data/csv'

for r in root_files:
    if (r.endswith("csv")):
        shutil.move(r, csv_source)


# Archive the Keywords and Crawl Files...
source = here + '/data'
kw_dir = archive_date + '/keywords'
cr_dir = archive_date + '/crawls'

os.chdir('data')

os.mkdir(archive_date)
os.mkdir(kw_dir)
os.mkdir(cr_dir)

files = os.listdir(source)

for f in files:
    if (f.startswith("keyword") or f.startswith("Keyword")):
        shutil.move(f, kw_dir)
    elif (f.startswith("crawl") or f.startswith("Crawl")):
        shutil.move(f, cr_dir)