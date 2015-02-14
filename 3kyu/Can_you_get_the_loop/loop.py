#!/usr/bin/python

# different algorithm, using 2 floating pointers, no interim growing data structures here, lobely-jobely :)
def loop_size(node):
    # we look for a point that lies on the circle
    pointer_main=node
    pointer_leader=node.next
    while pointer_leader!=pointer_main:
        pointer_main=pointer_main.next
        pointer_leader=pointer_leader.next.next
    # we have a point on the circle, now make 1 full round and count them
    count=1
    while pointer_leader.next!=pointer_main:
        count+=1
        pointer_leader=pointer_leader.next
    return count

# 1st solution is the knee-jerk one, works for small test cases, fails on final tests due to... being stupid
#
#def loop_size_1st(node):
#    if node.next==node: return 1
#    loop_nodes=[node]
#    while not node.next in loop_nodes:
#        loop_nodes.append(node.next)
#        node=node.next
#    return len(loop_nodes)-loop_nodes.index(node.next)

# same solution as 1st, but change list to dictionary... hash search kills the final tests, works
#
#def loop_size_HASH_search(node):
#    if node.next==node: return 1
#    loop_nodes=dict()
#    loop_nodes[str(node)]=0
#    while not str(node.next) in loop_nodes:
#        loop_nodes[str(node.next)]=0
#        node=node.next
#    loop_nodes[str(node)]=1
#    while not loop_nodes[str(node.next)]:
#        loop_nodes[str(node.next)]=1
#        node=node.next
#    loop_nodes[str(node)]=1
#    return len(filter(lambda i: i==1, loop_nodes.values()))
