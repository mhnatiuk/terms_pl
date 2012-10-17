import re
import morfeusz
import csv
import nltk
from sys import argv
from time import time
####################
def get_word_counts(text):
	words = dict()
	tokens = nltk.wordpunct_tokenize(text.decode('utf8'))
	for word in tokens:
		res =  morfeusz.analyse(word)
		tup = res.pop().pop()
		#list.append(tup[1])
		if tup[1]:
			try:
				words[tup[1]] = words[tup[1]] + 1
			except KeyError:
				words[tup[1]] = 1
		else:
			pass
	return words

#################
try:
	sname, fname = argv
except ValueError:
	quit("Err: pass a filename.")

with open(fname, "r") as csvfile:
	reader = csv.reader(csvfile,delimiter=';',quotechar='"')
	start = time()
	for row in reader:
		try:
			rows_returned = get_word_counts(row[6])
		except IndexError:
			print "Woooooow %r" % (row)
			quit()

		for k,v in rows_returned.iteritems():
#			print "%s;%s;%s;\"%s\";\"%s\";\"%s\";%s;%s" % (row[0],row[1],row[2].decode("utf8"),row[3].decode("utf8"),row[4].decode("utf8"),row[5].decode("utf8"),k,v)
			text = row[0]+ ";" + row[1] + ";" +row[2]
			text = text + ";\"" + row[3] + "\";\"" + row[4] + "\";\"" + row[5] + "\";\""
			try:
				text = text +  k.encode("utf8") + "\";" + str(v)
			except AttributeError:
				print k
				quit()
			print text
	end = time()
#	print "Exec time: %r"% (end - start)




#read whole file -  for big files You might want to change this to buffer-wise reading


