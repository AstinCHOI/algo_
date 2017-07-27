# http://blog.eairship.kr/249

heap = []
usedSize = 0

def insert(data):
    global usedSize
    usedPos = usedSize
    parentPos = int((usedPos - 1) / 2)
    
    # if usedSize >= Q: # Q - capacity
    #     print("Heap is full!")
    #     return
    
    heap[usedSize] = data
    while (usedPos > 0 and heap[usedPos] < heap[parentPos]):
        heap[usedPos], heap[parentPos] = heap[parentPos], heap[usedPos]
        usedPos = parentPos
        parentPos = int((usedPos-1)/2)

    usedSize = usedSize + 1

def delete(data):
    global usedSize
    if usedSize == 0:
        return

    currPos = 0
    for i in range(usedSize):
        if data == heap[i]:
            currPos = i
            usedSize = usedSize - 1
            heap[currPos], heap[usedSize] = heap[usedSize], heap[currPos]
            break
    reArrangeHeap(currPos)

def reArrangeHeap(currPos):
    parentPos = currPos
    leftPos = 2 * parentPos + 1
    rightPos = leftPos + 1

    while True:
        selectChild = 0
        if leftPos >= usedSize:
            break
        elif rightPos >= usedSize:
            selectChild = leftPos
        else:
            if heap[leftPos] > heap[rightPos]:
                selectChild = rightPos
            else:
                selectChild = leftPos

        if heap[selectChild] < heap[parentPos]:
            heap[parentPos], heap[selectChild] = heap[selectChild], heap[parentPos]
            parentPos = selectChild
        else:
            break
        
        leftPos = 2 * parentPos + 1
        rightPos = leftPos + 1

# def extractMin():
#     global usedSize
#     if usedSize == 0:
#         return
#     parentPos, leftPos, rightPos = 0, 1, 2
    
#     heap[0] = None
#     usedSize = usedSize - 1
#     heap[0], heap[usedSize] = heap[usedSize], heap[0]
    
#     while True:
#         selectChild = 0
#         if leftPos >= usedSize:
#             break
#         elif rightPos >= usedSize:
#             selectChild = leftPos
#         else:
#             if heap[leftPos] > heap[rightPos]:
#                 selectChild = rightPos
#             else:
#                 selectChild = leftPos

#         if heap[selectChild] < heap[parentPos]:
#             heap[parentPos], heap[selectChild] = heap[selectChild], heap[parentPos]
#             parentPos = selectChild
#         else:
#             break
        
#         leftPos = 2 * parentPos + 1
#         rightPos = leftPos + 1

        
Q = int(input())
heap = [0 for _ in range(Q)]

for _ in range(Q):
    line = input()
    if line.startswith('1'):
        v = int(line.split()[1])
        insert(v)
    elif line.startswith('2'):
        v = int(line.split()[1])
        delete(v)
    else:
        print(heap[0])