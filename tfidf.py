import csv
import math
from sys import argv
## This script calculates TF/IDF value for words in a set of documents
## User has to specify: 
## 1. A csv-formatted file (';' as separator, '"' as quote),
## 2. The number of a column which contains words
## 3. The number of a column which contains the sum of term occurances in a document
## 4. The number of a column that indicates by which column to aggregate ( a document : 'd' in http://en.wikipedia.org/wiki/TFIDF )
## This script writes output to STDOUT
##


try:
	sname, filename, w_col, sum_col, a_col = argv
except ValueError:
        quit("Please try: script.py filename column-with-words column-to-aggregate-by")

try:
	w_col= int(w_col)-1
	sum_col= int(sum_col) -1
	a_col= int(a_col) -1
except ValueError:
	quit("Last 3 arguments must be integers")

with open(filename, "r") as csvfile:
	reader = csv.reader(csvfile,delimiter=';',quotechar='"')
	docs = dict()
	docfreq = dict() # number of documents where the term T appears
	termfreq = dict() # term frequency per document
	for row in reader:
		try:
			docfreq[row[w_col]] += 1
		except KeyError:
			docfreq[row[w_col]] = 1
		docs[row[a_col]] = 1
		key = (row[w_col], row[a_col])  
		termfreq[key] = int(row[sum_col])
		
	D = len(docs) # total no documents
	dictTFIDF = dict() # wyniki tfidf
	for keys, val in termfreq.iteritems():
		term = keys[0]
		doc = keys[1]
		tf = termfreq[keys]
		idf = math.log( D / docfreq[term] ) 
		tfidf = tf * idf
		#dictTFIDF[keys] = tfidf
		print "\"%s\";\"%s\";%s" % (term,doc,tfidf)
		#print "In document %s term %s has tfidf value of %r" % (doc, term, tfidf)
	
	#D # number of documents in the corpus
	#tf #per document, so its length is equal to the number of rows in csv file
	#idf #per term, so its length equal to the number of unique words in csv file




