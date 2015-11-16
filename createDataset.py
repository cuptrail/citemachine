from citemachine.corpus.dblp import DBLP
import sqlite3 as lite
import sys

#set to the location where dblp is stored
path_to_dblp = 'acm_output.txt'
#set to location for output sqlite database
path_to_output = 'dblpextract.db'
#set to a small value like 5000 to test on a subset of the data
num_docs = 5000

#parses the dataset
dblp = DBLP(path_to_dblp, max_docs=num_docs)

#iterate through documents and write attributes to output database
with lite.connect(path_to_output) as con:
    cur = con.cursor();
    cur.execute("DROP TABLE IF EXISTS Articles")
    cur.execute("CREATE TABLE Articles(ID INT, Title TEXT, Author TEXT, \
    Year TEXT, Conference TEXT, Cite_Count TEXT, Refs TEXT, Abstract TEXT)")
    for key in dblp.keys():
        title = str(dblp.titles[key]) + ","
        author = str(dblp.authors[key]) + ","
        year = str(dblp.years[key]) + ","
        conference = str(dblp.conferences[key]) + ","
        cite_count = str(dblp.citation_counts[key]) + ","
        refs = str(dblp.references[key]) + ","
        abstract = str(dblp.abstracts[key]) + "\n"
        cur.execute("INSERT INTO Articles VALUES(?,?,?,?,?,?,?,?)", (key, \
        title, author, year, conference, cite_count, refs, abstract))
