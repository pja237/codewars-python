#!/usr/bin/python

#
# Inspired from real-world Brainf**k, we want to create an interpreter of that language which will support the following instructions 
# (the machine memory or 'data' should behave like a potentially infinite array of bytes, initialized to 0):
# 
# > increment the data pointer (to point to the next cell to the right).
# < decrement the data pointer (to point to the next cell to the left).
# + increment (increase by one, truncate overflow: 255 + 1 = 0) the byte at the data pointer.
# - decrement (decrease by one, treat as unsigned byte: 0 - 1 = 255 ) the byte at the data pointer.
# . output the byte at the data pointer.
# , accept one byte of input, storing its value in the byte at the data pointer.
# [ if the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, 
#    jump it forward to the command after the matching ] command.
# ] if the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, 
#    jump it back to the command after the matching [ command.
#
# The function will take in input...
# 
# The program CODE, a string with the sequence of machine instructions,
# The program INPUT, a string, eventually empty, that will be interpreted as an array of bytes using each character's ASCII code and will be 
#  consumed by the , instruction
# ... and will return ...
# 
# The output of the interpreted code (always as a string), produced by the . instruction.
#

class Machine:
    def __init__(self,code='',input=''):
        self.input=input
        self.code=code
        self.output=''
        self.mem=[chr(0)]
        self.dp=0
        self.ip=0

    def get_output(self):
        tmp=str(self.output)
        return tmp

    def decode_n_exec(self,ip):
        #print 'DnE: decoding',self.code[self.ip]
        if self.code[self.ip] == '>':
            #print " DnE: dp++"
            self.dp+=1
            if self.dp>=len(self.input):
                self.mem.append(chr(0))
        elif self.code[self.ip] == '<':
            #print " DnE: dp--"
            self.dp-=1
            if self.dp<0:
                self.mem='0'+self.input
                self.mem.insert(0,chr(0))
        elif self.code[self.ip] == '+':
            #print " DnE: *(dp)++"
            self.mem[self.dp]=chr(ord(self.mem[self.dp])+1) if ord(self.mem[self.dp])<255 else chr(0)
        elif self.code[self.ip] == '-':
            #print ' DnE: *(dp)--'
            self.mem[self.dp]=chr(ord(self.mem[self.dp])-1) if ord(self.mem[self.dp])>0 else chr(255)
        elif self.code[self.ip] == '.':
            #print ' DnE: Put mem@dp to output'
            self.output+=self.mem[self.dp]
        elif self.code[self.ip] == ',':
            #print ' DnE: Read input to mem@dp' 
            self.mem[self.dp]=self.input[0]
            self.input=self.input[1:]
        elif self.code[self.ip] == '[':
            #print ' DnE: IF'
            brackcount=1
            if ord(self.mem[self.dp])==0:
                # search for ] and set ip after that
                while not (self.code[self.ip]==']' and brackcount==0):
                    self.ip+=1
                    if self.code[self.ip]=='[': brackcount+=1
                    if self.code[self.ip]==']' and brackcount>0:
                        brackcount-=1
        elif self.code[self.ip] == ']':
            #print ' DnE: BACK IF'
            brackcount=1
            if ord(self.mem[self.dp])!=0:
                while not (self.code[self.ip]=='[' and brackcount==0):
                    self.ip-=1
                    if self.code[self.ip]==']': brackcount+=1
                    if self.code[self.ip]=='[' and brackcount>0: brackcount-=1
        else:
            return None
        self.ip+=1
        return 1

    def got_code(self):
        if self.ip>=len(self.code):
            return False
        else:
            return True

    def dump(self):
        print " --- MACHINE ---"
        print "Memory:",self.mem
        print "Memory decoded",map(lambda i: ord(i), self.mem)
        print "Code:",self.code
        print '     ',''.join(map(lambda i: '-' if self.ip!=i else '^',xrange(len(self.code)) ))
        print "@instruction:",self.code[self.ip]
        print "Input:",str(self.input)
        print "Output:",str(self.output)
        print "DP:",self.dp
        print "IP:",self.ip
        print " ---------------"

def brain_luck(code, input):
    output=None
    comp=Machine(code,input)
    while comp.got_code():
        #print "We still have code"
        #comp.dump()
        comp.decode_n_exec(0)
        #raw_input()
    #print ord(comp.get_output())
    #comp.dump()
    return comp.get_output()


# Echo until byte(255) encountered
print 'INPUT:',',+[-.,+]', 'Codewars' + chr(255)
print brain_luck(',+[-.,+]', 'Codewars' + chr(255)),"SHOULD ==", 'Codewars'

# Echo until byte(0) encountered
print 'INPUT:',',[.[-],]', 'Codewars' + chr(0)
print brain_luck(',[.[-],]', 'Codewars' + chr(0)),"SHOULD ==", 'Codewars'

# Two numbers multiplier
print 'INPUT:',',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)
print brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)), "SHOULD ==", chr(72)

