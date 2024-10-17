import sys

N = int(sys.stdin.readline())
parentsInput = list(map(int, sys.stdin.readline().split()))
deleteNode = int(sys.stdin.readline())
Nodes = dict()
answer = 0

class Node:
    def __init__(self):
        self.parent = None
        self.childs = []
    def delete(self):
        for i in self.childs:
            Nodes[i].delete()
            Nodes.pop(i)

for i in range(N):
    if i not in Nodes:
        Nodes[i] = Node()
    if parentsInput[i] != -1:
        Nodes[i].parent = parentsInput[i]
        if parentsInput[i] not in Nodes:
            Nodes[parentsInput[i]] = Node()
        Nodes[parentsInput[i]].childs.append(i)

mother = 0
while True:
    if Nodes[mother].parent:
        mother = Nodes[mother].parent
    else:
        break

Nodes[deleteNode].delete()
if Nodes[deleteNode].parent != None:
    Nodes[Nodes[deleteNode].parent].childs.remove(deleteNode)
Nodes.pop(deleteNode)

def count(Node):
    global answer
    if Node.childs:
        for i in Node.childs:
            count(Nodes[i])
    else:
        answer += 1

if Nodes:
    count(Nodes[mother])
   
print(answer)