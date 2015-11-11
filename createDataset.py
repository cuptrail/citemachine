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
        output += str(dblp.titles[key]) + ","
        output += str(dblp.authors[key]) + ","
        output += str(dblp.years[key]) + ","
        output += str(dblp.conferences[key]) + ","
        output += str(dblp.citation_counts[key]) + ","
        output += str(dblp.references[key]) + ","
        output += str(dblp.abstracts[key]) + "\n"
        document.write(output)
