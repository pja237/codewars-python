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

def brain_luck(code, input):
    output=None

    return output


# Echo until byte(255) encountered
print 'INPUT:',',+[-.,+]', 'Codewars' + chr(255)
print brain_luck(',+[-.,+]', 'Codewars' + chr(255)),"SHOULD ==", 'Codewars'

# Echo until byte(0) encountered
print 'INPUT:',',[.[-],]', 'Codewars' + chr(0)
print brain_luck(',[.[-],]', 'Codewars' + chr(0)),"SHOULD ==", 'Codewars'

# Two numbers multiplier
print 'INPUT:',',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)
print brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)), "SHOULD ==", chr(72)
