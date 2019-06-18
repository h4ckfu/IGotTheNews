import os 
from time import gmtime, strftime
import logging
import shutil

archive_date = str(strftime("%Y-%m-%d", gmtime()))
here = os.getcwd()

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