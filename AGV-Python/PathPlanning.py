A = ["A", {"B" : [100,0], "Z" : [200,180]}]
B = ["B", {"V" : [150,0], "A" : [100,180]}]
V = ["V", {"B" : [150,180], "C" : [200, 90]}]
C = ["C", {"V" : [200,270], "D" : [500,90]}]
D = ["D", {"E" : [100, 90], "C" : [500,270]}]
E = ["E", {"D" : [100, 270], "G" : [500,180]}]
Z = ["Z", {"A" : [100, 0], "I" : [500,90]}]
G = ["G", {"E" : [100,0], "I" : [100,90]}]
I = ["I", {"G": [100,0], "Z" : [100,270]}]
local = locals()

class PathPlanning:
    def __init__(self):
        self.localVar = local
        self.A = A
        self.B = B
        self.V = C
        self.C = C
        self.D = D
        self.E = E
        self.Z = Z 
        self.G = G
        self.I = I
        self.member = [self.A, self.B, self.V, self.C, self.D, self.E, self.Z, self.G, self.I]
        self.target = None
    def setState(self, state):
        for i in range(len(self.member)):
            if self.member[i][0] == state:
                self.state = self.member[i]
        print("{} is the state".format(self.state))

    def preprocessing(self, a, arr):
        arr[0].append(a[0])
        arr[1].append(a[0])
        arr[0].append((list(a[1].keys()))[0])
        arr[1].append((list(a[1].keys()))[1])

    def checkDuplicate(self, arr):
        stateArr = False
        for i in range(0, len(arr)):    
            for j in range(i+1, len(arr)):    
                if(arr[i] == arr[j]):    
                    stateArr = True
        return stateArr

    def checker(self, a, n):
        print((list(a[1].keys())))
        print(list(self.localVar[(list(a[1].keys()))[n]]), '\n')

    def adjVal(self, arr, j):
        arr.append(j)
        if self.checkDuplicate(arr):
            arr.pop()

    def grandChild(self, a,i):
        return list(self.localVar[(list(a[1].keys()))[i]][1].keys())

    def child(self, a):
        return list(self.localVar[a[0]][1].keys())

    def grandChildMethod(self, arr, func):
        for j in range(len(func)):
            if j==1:
                self.adjVal(arr, func[j])
            else:
                self.adjVal(arr, func[j])

    def childMethod(self, i, arr, func):
        if(i==0):
            for j in range(len(func)):
                self.adjVal(arr[i], func[j])
        else:
            for j in range(len(func)):
                self.adjVal(arr[i], func[j])

    def findPath(self,b):
        arr = [[],[]]
        tempArr = list(self.state[1].keys())
        if self.state[0] and b[0] in self.localVar:
            if len(arr[0])<=0 or len(arr[0])<=0:
                self.preprocessing(self.state, arr)
            try:
                count = 0
                while True:
                    if arr[1][-1] == b[0] or arr[0][-1] == b[0]:
                        print("path found")
                        return arr[1] if arr[1][-1] == b[0] else arr[0]
                    elif count == 0:
                        for i in range(len(tempArr)):
                            self.grandChildMethod(arr[0], self.grandChild(self.state,i)) if i==0 else self.grandChildMethod(arr[1], self.grandChild(self.state,i)) 
                        tempArr[0], tempArr[1] = arr[0][-1], arr[1][-1]
                    elif count==10:
                        print("max loop reached, path not found"); break
                    else:
                        for i in range(len(tempArr)):
                            self.childMethod(i, arr, self.child(tempArr[i]))
                        tempArr[0], tempArr[1] = arr[0][-1], arr[1][-1]
                    count += 1
            except KeyError:
                print("data not available")

    def trackNext(self, arr, a):
        return (self.localVar[arr[a][0]][1][arr[a+1]])

    def pathPlanningStep(self, a, status = False, update=False):
        for i in range(len(self.member)):
            if self.member[i][0] == a:
                self.target = self.member[i]
        arr = self.findPath(self.target)
        if status == False:
            self.path = []
            for i in range(len(arr)):
                if i < len(arr)-1:
                    self.path.append([i+1, self.trackNext(arr, i)[0], self.trackNext(arr, i)[1], self.localVar[arr[i+1][0]][0]])
                    # print("plan:",i+1 ,"|| move:", self.trackNext(arr, i)[0], "degree:",  self.trackNext(arr, i)[1], "state:", self.localVar[arr[i+1][0]][0])
            if update==True:
                self.state = self.localVar[arr[-1]]
            return self.path
        elif status == True:
            print("path: ",arr)
            for i in range(len(arr)):
                if i < len(arr)-1:
                    print("plan:",i+1 ,"|| move:", self.trackNext(arr, i)[0], "degree:",  self.trackNext(arr, i)[1], "state:", self.localVar[arr[i+1][0]][0])
            if update==True:
                self.state = self.localVar[arr[-1]]
            print("done, robot finish planning")



a = PathPlanning()
