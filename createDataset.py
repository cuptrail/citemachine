from citemachine.corpus.dblp import DBLP

#set to the location where dblp is stored
path_to_dblp = 'acm_output.txt'
#set to location for output dataset
path_to_output = 'dataset.txt'
#set to a small value like 5000 to test on a subset of the data
num_docs = 5000

#parses the dataset
dblp = DBLP(path_to_dblp, max_docs=num_docs)

#iterate through documents and write attributes to output file
with open(path_to_output, 'w') as document:
    for key in dblp.keys():
        output = ""
        output += dblp.titles[key] + ","
        output += dblp.authors[key] + ","
        output += dblp.years[key] + ","
        output += dblp.conferencces[key] + ","
        output += dblp.citation_counts[key] + ","
        output += dblp.references[key] + ","
        output += dblp.abstracts[key] + "\n"
    document.write(output)
