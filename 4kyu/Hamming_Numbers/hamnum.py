#!/bin/python

''' calculate n-th Hamming number (hamnum= 2^i * 3^i * 5^i) '''

def hamnum_1(n):
    hamnum_list=[1]
    hamnum_set=set(hamnum_list)

    array_len=n
    start=0

    print "********************************************************************************"
    while start<n/2:
        hamnum_set_add=set()
        print " HAMNUM LIST BEFORE ADD", start, "-th", hamnum_list
        print " HAMNUM SET BEFORE ADD", start, "-th", hamnum_set
        hamnum_set_add=set()
        hamnum_set_add=set(map(lambda i: i*2, hamnum_list[start:n/2 if len(hamnum_list)<n else len(hamnum_list)]))
        print hamnum_set_add
        hamnum_set_add=hamnum_set_add.union(set(map(lambda i: i*3, hamnum_list[start:n/2 if len(hamnum_list)<n else len(hamnum_list)])))
        print hamnum_set_add
        hamnum_set_add=hamnum_set_add.union(set(map(lambda i: i*5, hamnum_list[start:n/2 if len(hamnum_list)<n else len(hamnum_list)])))
        print hamnum_set_add
        hamnum_list=sorted(hamnum_set.union(hamnum_set_add))
        if len(hamnum_list)>n: hamnum_list=hamnum_list[:n]
        hamnum_set=set(hamnum_list)
        print " HAMNUM LIST AFTER ADD", start, "-th", hamnum_list
        print " HAMNUM SET AFTER ADD", start, "-th", hamnum_set
        raw_input()
        start+=1
    return hamnum_list[-1]


def hamnum_2(n):
    hamnum_list=[1]
    hamnum_set=set(hamnum_list)

    array_len=n
    start=0

    while start<n/2:
        hamnum_set_add=set()
        hamnum_set_add=set(map(lambda i: i*2, hamnum_list[start:n/2 if len(hamnum_list)<n else len(hamnum_list)]))
        hamnum_set_add=hamnum_set_add.union(set(map(lambda i: i*3, hamnum_list[start:n/2 if len(hamnum_list)<n else len(hamnum_list)])))
        hamnum_set_add=hamnum_set_add.union(set(map(lambda i: i*5, hamnum_list[start:n/2 if len(hamnum_list)<n else len(hamnum_list)])))
        hamnum_list=sorted(hamnum_set.union(hamnum_set_add))
        if len(hamnum_list)>n: hamnum_list=hamnum_list[:n]
        hamnum_set=set(hamnum_list)
        start+=1
    return hamnum_list[-1]

def hamnum(n):
    ''' get n-th hamnum '''
    hamset=set()

    hamset.add(1)
    i=1
    while i<=n/2:
        #print "[ ",n ," ] pre 2 ",hamset
        hamset=set(sorted(hamset.union(map(lambda i: i*2, hamset)))[0:n])
        #hamset=hamset.union( map(lambda i: i*2, hamset)[0:n] )
        #print "pre 3 ",hamset
        hamset=set(sorted(hamset.union(map(lambda i: i*3, hamset)))[0:n])
        #hamset=hamset.union( map(lambda i: i*3, hamset)[0:n] )
        #print "pre 5 ",hamset
        hamset=set(sorted(hamset.union(map(lambda i: i*5, hamset)))[0:n])
        #hamset=hamset.union( map(lambda i: i*5, hamset)[0:n] )
        #print "post all ", hamset
        i+=1
    #print " GOT FINAL SET ", sorted(hamset)
    #raw_input()
    return sorted(list(hamset))[n-1]

for i in xrange(64,75):
    print i,"-th == ", hamnum_1(i)
