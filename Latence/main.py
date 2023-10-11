with open("input.txt", "r") as file:
    inp = file.read()

def getTasks(inp):
    tasks = []
    numberOfTasks, inp = int(inp.split("\n")[0]), inp.split("\n")[1:]
    for task in range(numberOfTasks):
        devices = []
        for device in inp[1].split(" "):
            devices.append(int(device))
        tasks.append(devices)
        inp = inp[2:]
    return tasks

def solve(task):
    k = 1
    for i in range(1, len(task)+1):
        grupo = []
        for lat in task:
            if lat % i == 0:
                grupo.append(lat)
        if len(grupo) >= i:
            
            k = i
    return k

if __name__ == "__main__":
    tasks = getTasks(inp)
    for task in tasks:
        print(solve(task))