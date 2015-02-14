#!/usr/bin/python

class Automaton:
    def __init__(self):
        self.states={'q1': {'0': 'q1', '1': 'q2'}, 'q2': {'0': 'q3', '1': 'q2'}, 'q3': {'0': 'q2', '1': 'q2'}}
    def read_commands(self, commands):
        s='q1'
        for i in commands: s=self.states[s][i]
        if s=='q2':
            return True
        else:
            return False

a=Automaton()
is_accepted = a.read_commands(["1", "0", "0", "1", "0"])
if is_accepted:
    print "ACCEPTED"
else:
    print "NOT!"
