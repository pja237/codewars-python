#!/usr/bin/python



class universe:
    def __init__(self, start_matrix):
        self.matrix=start_matrix
        self.x=len(start_matrix)-1
        self.y=len(start_matrix[0])-1

    def getmatrix(self):
        return self.matrix

    def out(self):
        print "X , Y =", self.x,',',self.y
        #print self.matrix
        for i in self.matrix:
            print i
        print

    def out_trans(self):
        print "X , Y =", self.x,',',self.y
        for i in self.trans_matrix:
            print i
        print

    def expand(self):
        tmp=list()
        tmp.append([0 for i in xrange(self.y+3)])
        for i in self.matrix: tmp.append([ 0 if j==0 or j>len(i) else i[j-1] for j in xrange(len(i)+2)])
        tmp.append([0 for i in xrange(self.y+3)])
        self.matrix=tmp
        self.x=len(self.matrix)-1
        self.y=len(self.matrix[0])-1

    def shrink(self):
        self.matrix=self.matrix[1:-1]
        self.matrix=map(lambda i: i[1:-1], self.matrix)
        self.x=len(self.matrix)-1
        self.y=len(self.matrix[0])-1
        return

    def shrink_if(self):
        print "SHRINKING"
        self.out()
        while self.matrix[0] and not 1 in self.matrix[0]: 
            self.matrix=self.matrix[1:] if self.x>0 else [[]]
            self.x-=1
            print " cut up"
            self.out()
        while self.matrix[0] and not 1 in self.matrix[-1]:
            self.matrix=self.matrix[:-1]  if self.x>0 else [[]]
            self.x-=1
            print " cut down"
            self.out()
        while self.matrix[0] and not 1 in map(lambda i: i[0], self.matrix):
            self.matrix=map(lambda i: i[1:], self.matrix) if self.y>0 else [[]]
            self.y-=1
            print " cut left"
            self.out()
        while self.matrix[0] and not 1 in map(lambda i: i[-1], self.matrix):
            self.matrix=map(lambda i: i[:-1], self.matrix) if self.y>0 else [[]]
            self.y-=1
            print " cut right"
            self.out()

    def sum_cell(self,x,y):
        s=0
        x+=1
        y+=1
        self.expand()
        s1=sum( self.matrix[x-1][y-1:y+2] )
        s2=sum( self.matrix[x][y-1:y+2] )
        s3=sum( self.matrix[x+1][y-1:y+2] )
        self.shrink()
        return s1+s2+s3 if self.matrix[x-1][y-1]==0 else s1+s2+s3-1

    def make_trans_matrix(self):
        self.trans_matrix=list()
        for i in xrange(self.x+1):
            self.trans_matrix.append(map(lambda j: self.sum_cell(i,j) , xrange(self.y+1)))

    def live_or_die(self, s, t):
        nxt=0
        if s==0 and t==3: nxt=1
        elif s==0 and t!=3: nxt=0
        elif s==1 and t in (2,3): nxt=1
        elif s==1 and not t in (2,3): nxt=0
        return nxt

    def next_gen(self):
        next_gen_matrix=list()
        for i in xrange(self.x+1):
                next_gen_matrix.append(map(lambda j: self.live_or_die(self.matrix[i][j], self.trans_matrix[i][j]) , xrange(self.y+1)))
        self.matrix=next_gen_matrix

def get_generation(cells, generations):
    game=universe(cells)
    for i in xrange(generations):
        print "GENERATION ",i
        game.out()
        game.expand()
        game.make_trans_matrix()
        game.next_gen()
        game.shrink_if()
    return game.getmatrix()


start=[
[1,0,0],
[0,1,1],
[1,1,0]
]

start_2=[
[1,1,1],
[1,1,1],
[1,1,1]
]

mat=get_generation(start,100)

for i in mat:
    print i


#for i in xrange(game.x+1):
#    print map(lambda j: game.sum_cell(i,j) , xrange(game.y+1))
