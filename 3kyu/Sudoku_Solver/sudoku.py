#!/usr/bin/python

import time

count=0

puzzle = [
[5,3,0,0,7,0,0,0,0],
[6,0,0,1,9,5,0,0,0],
[0,9,8,0,0,0,0,6,0],
[8,0,0,0,6,0,0,0,3],
[4,0,0,8,0,3,0,0,1],
[7,0,0,0,2,0,0,0,6],
[0,6,0,0,0,0,2,8,0],
[0,0,0,4,1,9,0,0,5],
[0,0,0,0,8,0,0,7,9]
]

puz=[
[1,2,3],
[4,5,6],
[7,8,9]
]


class Grid:
    def __init__(self, a):
        self.grid=a
        self.x=9
        self.y=9

    def dump_data(self):
        tmp=map(lambda i: list(i), self.grid[:])
        return tmp

    def dump(self):
        for i in self.grid:
            print i
        print " --- "

    def is_full(self):
        if filter(lambda i: i.count(0)>0, self.grid):
            return False
        else:
            return True

    def find_ziher(self):
        for i in xrange(self.x):
            for j in xrange(self.y):
                if self.grid[i][j]==0:
                    rp=self.get_row_pos(i)
                    cp=self.get_col_pos(j)
                    sp=self.get_sq_pos(i,j)
                    #print i,j,rp,cp,sp, set.intersection(rp,cp,sp)
                    if len(set.intersection(rp,cp,sp))==1:
                        #print "GOT ZIHER @",i,j, set.intersection(rp,cp,sp)
                        self.grid[i][j]=set.intersection(rp,cp,sp).pop()

    def find_next_empty(self):
        for i in xrange(self.x):
            for j in xrange(self.y):
                if self.grid[i][j]==0:
                    return (i,j)

    def try_add(self,x,y,i):
        self.grid[x][y]=i
        return None

    def get_row_pos(self,x):
        return set(range(1,10))-set(self.grid[x])

    def get_col_pos(self,y):
        return set(range(1,10))-set(map(lambda i: i[y] ,self.grid))

    def get_sq_pos(self,x,y):
        #print "x=",(x/3)*3,':',(x/3)*3+3
        #print "y=",(y/3)*3,':',(y/3)*3+3
        ss=set()
        for i in xrange((x/3)*3, (x/3)*3+3):
            for j in xrange((y/3)*3, (y/3)*3+3):
                #print self.grid[i][j]
                ss.add(self.grid[i][j])
        return set(range(1,10))-ss

solution=list()

def recurse_solve(g):
    global solution
    global count
    count+=1
    #print "Entering recurse"
    if g.is_full():
        print "FULL"
        solution=g.dump_data()
        return 

    (x,y)=g.find_next_empty()
    #print x,y
    for i in xrange(1,10):
        #g.dump()
        #print x,y,i,  set.intersection(g.get_row_pos(x), g.get_col_pos(y), g.get_sq_pos(x,y) )
        if not i in set.intersection(g.get_row_pos(x), g.get_col_pos(y), g.get_sq_pos(x,y) ): continue
        data=g.dump_data()
        tmp=Grid(data)
        tmp.try_add(x,y,i)
        #print "adding i=",i,'to x,y=',x,y
        recurse_solve(tmp)

    return 

print " --- METHOD 1  --- "
t=time.time()
g=Grid(puzzle)
g.dump()
recurse_solve(g)
for i in solution:
    print i
print "Function call count:",count
print "TIME:",time.time()-t

print " --- METHOD 2 --- "
t=time.time()
g=Grid(puzzle)
g.dump()
while not g.is_full():
    g.find_ziher()
g.dump()
print "TIME:",time.time()-t
