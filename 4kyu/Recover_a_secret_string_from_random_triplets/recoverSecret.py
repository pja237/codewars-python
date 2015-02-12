#!/usr/bin/python

secret = "whatisup"

triplets = [
['t','u','p'],
['w','h','i'],
['t','s','u'],
['a','t','s'],
['h','a','p'],
['t','i','s'],
['w','h','s']
]

def get_word(state, word, alphabet, transtbl):
	''' find the path from STATE using TRANSTBL that covers whole ALPHABET '''
	print "ENTERED: (state, word, alphabet)", state, word
	print alphabet
	raw_input()
	if not alphabet:
		print "WORD FOUND: ", word
		raw_input()
		return word
	nextjmps=filter(lambda i: i[0]==state , transtbl)
	print "JUMPS POSSIBLE:", nextjmps
	for i in nextjmps:
		# push where we're going
		if not i[1] in alphabet:
			# skip letter, we've been there
			next
		print " WORD: ",word
		print " GOING TO: ",i
		#word+=i[1]
		print " WORD: ",word
		raw_input()
		word=get_word(i[1], word+i[1], alphabet-set(i[1]), transtbl)
		print "BACK IN NXTJMPS: ", word, alphabet
		return word[:-1]
	return word


def recoverSecret(triplets):
	'triplets is a list of triplets from the secrent string. Return the string.'
	alphabet=set()
	startletter=''
	endletter=''
	gotit=''

	# create table of state changes, 
	# format: tuples (start, end)
	transtbl=map(lambda i: (i[0],i[1]), triplets)+map(lambda i: (i[1],i[2]), triplets)
	# get alphabet
	for i in triplets:
		for j in i:
			alphabet.add(j)
	print "table: ", transtbl
	print "alphabet: ",alphabet
	# find starting letter, one that is never in 2nd pos of transtbl tuple
	for i in alphabet:
		startletter=i if not filter(lambda j: j[1]==i, transtbl) else ''
	print "startletter: ",startletter
	# find ending letter, one that is never in 1nd pos of transtbl tuple
	for i in alphabet:
		endletter=i if not filter(lambda j: j[0]==i, transtbl) else ''
	print "endletter: ",endletter
	# we have starting letter, we have the table of state-changes
	# now find the path that covers ALL the letters from the alphabet
	gotit=get_word(startletter, startletter, alphabet-set(startletter), transtbl)

	return gotit


found=recoverSecret(triplets)
print found
if found==secret:
	print "GOT IT!"
else:
	print "FAIL :S"
