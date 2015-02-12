#!/usr/bin/python


proc = [
  ['make axe', 'stone', 'axe'],
  ['make knife', 'stone', 'knife'],
  ['make bricks', 'stone', 'bricks'],
  ['cut tree', 'axe', 'tree'],
  ['shave with axe', 'axe', 'stubs'],
  ['build log cabin', 'tree', 'house'],
  ['shave with knife', 'knife', 'stubs'],
  ['build house', 'bricks', 'house']
]

proc_1=[ [12,1,2,],[23,2,3,],[34,3,4,],[45,4,5,],[52,5,2],[14,1,4],[76,7,6] ]

path=[]
paths=[]

def processes(pos, end, map):
	#test if start and end im map, if not, return [], else start find()
	global path
	global paths
	path=[]
	paths=[]
	if pos==end or not filter(lambda i: i[1]==pos , map) and not filter(lambda i: i[2]==pos , map):
		print " *** START OR END MISSING"
		return []
	else:
		find(pos, end, map)
		paths_sorted=sorted(paths, key=lambda i: len(i))
		return paths_sorted[0] if paths_sorted else []
		

def find(pos, end, map):
	global path
	global paths
	#raw_input(' Go on...')
	print "\nPOSITION ",pos," PATH TAKEN ",path
	if pos!=end:
		# TEST for circular with 'not i[0] in path
		possibles=filter(lambda i: i[1]==pos and not i[0] in path, map)
		if not possibles:
			print "***** REACHED DEAD END OR HIT CIRCULAR BEGINNING", pos, path, "\n"
			path=path[:-1]
			return
		print "-- @ ", pos," , WAYS ONWARDS ",possibles
		for i in possibles:
			path+=[i[0]]
			print "---> TAKE PATH TO ", i, " TO ", i[2]
			# fix, test the NEXT i[0] for circulars
			#if i[2] in path:
			#	print " *!*!*!*!* CIRCULAR SHIT, ABORT PATH ", i[2]
			#	break
			find(i[2], end, map)
		print " ===== EXHAUSTED WAYS: ",pos, "\n"
		path=path[:-1]
	else:
		paths.append(path)
		print "HIT END", paths
		path=path[:-1]


print processes('stone','house', proc)
print processes('stone','stubs', proc)
print processes(1,6, proc_1)
print processes(1,5, proc_1)
print processes(1,1, proc_1)

print "FINAL PATHS ", paths
print "SORTED PATHS ", sorted(paths, key=lambda i: len(i))
print "SHORTEST PATH ", sorted(paths, key=lambda i: len(i))[:1]

raw_input()
