import time

def move(b):
    try:
        global state
        print("dimulai dari " + state[0])
        print(state)
        if state[1][b[0]] > 0:
            print("bisa")
            time.sleep(2)
            d = state[1][b[0]]
            while(True):
                d-=1
                time.sleep(0.5)
                print(d)
                if d == 0:
                    state = b
                    print(state + '\n')
                    break
    except KeyError:
        print("error data not available, can't do movement")