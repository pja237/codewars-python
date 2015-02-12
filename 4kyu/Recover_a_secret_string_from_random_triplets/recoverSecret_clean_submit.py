
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
        result=''
        if not alphabet: return word
        nextjmps=filter(lambda i: i[0]==state , transtbl)
        for i in nextjmps:
                if not i[1] in alphabet: next
                result=get_word(i[1], word+i[1], alphabet-set(i[1]), transtbl)
                if result: break
        return result


def recoverSecret(triplets):
        'triplets is a list of triplets from the secrent string. Return the string.'
        alphabet=set()
        startletter=''
        transtbl=map(lambda i: (i[0],i[1]), triplets)+map(lambda i: (i[1],i[2]), triplets)
        for i in triplets:
                for j in i:
                        alphabet.add(j)
        for i in alphabet:
                if not filter(lambda j: j[1]==i, transtbl): startletter=i
        return get_word(startletter, startletter, alphabet-set(startletter), transtbl)


found=recoverSecret(triplets)
print "FOUND SECRET WORD: ", found
if found==secret:
	print "GOT IT!"
else:
	print "FAIL :S"
