import math
import sys

with open("input.txt", "r") as file:
    inp = file.read()
    
def calculate_angle(x, y):
    # Vypočítá úhel vzhledem k počátečnímu bodu (0, 0)
    return math.atan2(y, x)
class Device:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

    def __repr__(self) -> str:
        string = f"{self.x} {self.y} {self.name}"
        return string


class Task:

    def __init__(self, x, y):
        self.devices = []
        self.x = x
        self.y = y

    def addDevice(self, x, y, name):
        d = Device(x, y, name)
        self.devices.append(d)
    def sort_devices(self):

        # Seřaď body podle úhlu vzhledem k počátečnímu bodu
        self.devices = sorted(self.devices, key=lambda dev: calculate_angle(dev.x, dev.y))
        for i in range(len(self.devices)-1):
            if calculate_angle(self.devices[i].x, self.devices[i].y) == calculate_angle(self.devices[i+1].x, self.devices[i+1].y):
                if self.devices[i].x > self.devices[i+1].x:
                    self.devices[i], self.devices[i+1] = self.devices[i+1], self.devices[i]
                if self.devices[i].y < self.devices[i+1].y:
                    self.devices[i], self.devices[i+1] = self.devices[i+1], self.devices[i]
    def __repr__(self) -> str:
        string = f"{self.x}, {self.y}, {self.devices}"
        return string


def getTasks(inp):
    numberOftasks, inp = int(inp.split("\n")[0]), inp.split("\n")[1:]
    tasks = []
    for i in range(numberOftasks):
        
        x = inp[0].split(" ")[0]
        y = inp[0].split(" ")[1]
        numberOfdevices = int(inp[0].split(" ")[2])
        inp = inp[1:]
        tasks.append(Task(x, y))
        for j in range(numberOfdevices):
            x = int(inp[0].split(" ")[0])
            y = int(inp[0].split(" ")[1])
            name = inp[0].split(" ")[2]
            tasks[i].addDevice(x, y, name)
            inp = inp[1:]
        tasks[i].sort_devices()
    return tasks

def solve(devices):
    
    while devices:
        for i in range(len(devices)):
            if devices[i].name == devices[i-1].name:
                devices.remove(devices[i])
                devices.remove(devices[i-1])
                break
        else:
            return False
    return True
        


if __name__ == "__main__":
    output = []
    tasks = getTasks(inp)
    for i, task in enumerate(tasks):
        print(i)
        if solve(task.devices):
            output.append("pujde to")
            print("pujde to")
        else:
            output.append("ajajaj")
            print("ajajaj")
    
    with open("out.txt", "w") as f:
        for i in output:
            f.write(f"{i}\n")
    print("hotove")