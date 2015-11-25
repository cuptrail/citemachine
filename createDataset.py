from citemachine.corpus.dblp import DBLP
import sqlite3 as lite
import sys

#set to the location where dblp is stored
path_to_dblp = 'acm_output.txt'
#set to location for output sqlite database
path_to_output = 'dblpextract.db'
#set to a small value like 5000 to test on a subset of the data
num_docs = None

#parses the dataset
dblp = DBLP(path_to_dblp, max_docs=num_docs)

#iterate through documents and write attributes to output database
with lite.connect(path_to_output) as con:
    cur = con.cursor();
    cur.execute("DROP TABLE IF EXISTS Articles")
    cur.execute("CREATE TABLE Articles(ID INT, Title TEXT, Author TEXT, \
    Year TEXT, Conference TEXT, Cite_Count TEXT, Refs TEXT, Abstract TEXT, Missing INT)")
    for key in dblp.keys():
        title = str(dblp.titles[key])
        title = unicode(title,"utf-8")
        author = ""
        for auth in dblp.authors[key]:
			author = author + str(auth) + ","
		author = unicode(author,"utf-8")
        year = str(dblp.years[key])
        year = unicode(year,"utf-8")
        conference = str(dblp.conferences[key])
        conference = unicode(conference,"utf-8")
        cite_count = str(dblp.citation_counts[key])
        cite_count = unicode(cite_count,"utf-8")
        refs = ""
        for ref in dblp.references[key]:
			refs = refs + str(ref) + ","
        refs = unicode(refs,"utf-8")
        abstract = str(dblp.abstracts[key])
        abstract = unicode(abstract,"utf-8")
        missing = dblp.missingrefs[key];
        cur.execute("INSERT INTO Articles VALUES(?,?,?,?,?,?,?,?,?)", (key, \
        title, author, year, conference, cite_count, refs, abstract, missing))
