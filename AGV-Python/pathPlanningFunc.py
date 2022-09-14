A = ["A", {"B" : [100,0], "Z" : [200,180]}]
B = ["B", {"V" : [150,0], "A" : [100,180]}]
V = ["V", {"B" : [150,180], "C" : [200, 90]}]
C = ["C", {"V" : [200,270], "D" : [500,90]}]
D = ["D", {"E" : [100, 90], "C" : [500,270]}]
E = ["E", {"D" : [100, 270], "G" : [500,180]}]
Z = ["Z", {"A" : [100, 0], "I" : [500,90]}]
G = ["G", {"E" : [100,0], "I" : [100,90]}]
I = ["I", {"G": [100,0], "Z" : [100,270]}]

state = A
localVar = locals()

def preprocessing(a, arr):
    arr[0].append(a[0])
    arr[1].append(a[0])
    arr[0].append((list(a[1].keys()))[0])
    arr[1].append((list(a[1].keys()))[1])

def checkDuplicate(arr):
    stateArr = False
    for i in range(0, len(arr)):    
        for j in range(i+1, len(arr)):    
            if(arr[i] == arr[j]):    
                stateArr = True
    return stateArr

def checker(a, n):
    print((list(a[1].keys())))
    print(list(localVar[(list(a[1].keys()))[n]]), '\n')

def adjVal(arr, j):
    arr.append(j)
    if checkDuplicate(arr):
        arr.pop()

def grandChild(a,i):
    return list(localVar[(list(a[1].keys()))[i]][1].keys())

def child(a):
    return list(localVar[a[0]][1].keys())

def grandChildMethod(a,i, arr, func):
    for j in range(len(func)):
        if j==1:
            adjVal(arr, func[j])
        else:
            adjVal(arr, func[j])

def childMethod(i, arr, func):
    if(i==0):
        for j in range(len(func)):
            adjVal(arr[i], func[j])
    else:
        for j in range(len(func)):
            adjVal(arr[i], func[j])

def findPath(a,b):
    arr = [[],[]]
    tempArr = list(a[1].keys())
    if a[0] and b[0] in localVar:
        preprocessing(a,arr)
        try:
            count = 0
            while True:
                if arr[1][-1] == b[0] or arr[0][-1] == b[0]:
                    print("path found")
                    return arr[1] if arr[1][-1] == b[0] else arr[0]
                elif count == 0:
                    for i in range(len(tempArr)):
                        grandChildMethod(a,i,arr[0], grandChild(a,i)) if i==0 else grandChildMethod(a,i,arr[1], grandChild(a,i)) 
                    tempArr[0], tempArr[1] = arr[0][-1], arr[1][-1]
                elif count==10:
                    print("max loop reached, path not found"); break
                else:
                    for i in range(len(tempArr)):
                        childMethod(i, arr, child(tempArr[i]))
                    tempArr[0], tempArr[1] = arr[0][-1], arr[1][-1]
                count += 1
        except KeyError:
            print("data not available")

def trackNext(arr, a):
    return (localVar[arr[a][0]][1][arr[a+1]])

def pathPlanningStep(a):
    global state
    arr = findPath(state,a)
    print("path: ",arr)
    for i in range(len(arr)):
        if i < len(arr)-1:
            print("plan:",i+1 ,"|| move:", trackNext(arr, i)[0], "rotation:",  trackNext(arr, i)[1], "state:", localVar[arr[i+1][0]][0])
    state = localVar[arr[-1]]
    print("done, robot finish planning")

