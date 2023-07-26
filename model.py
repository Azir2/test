import time
import json
from math import cos, sin

class Vehicle:
    def __init__(self, x=0, y=0, speed=0, direction=0, accel=0):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        self.accel = accel
        self.destinations = []
        self.status = "stopped"

    def move(self, log):
        if self.status == "stopped" or not self.destinations:
            return
        self.speed += self.accel
        self.x += self.speed * cos(self.direction)
        self.y += self.speed * sin(self.direction)
        if abs(self.destinations[0][0]-self.x) + abs(self.destinations[0][1]-self.y) < self.speed:
            log.write(instruction=f"Reached destination {self.destinations[0]}", status=self.get_status())
            self.destinations.pop(0)
            if not self.destinations:
                self.status = "stopped"

    def add_destination(self, x, y, log):
        self.destinations.append((x, y))
        log.write(instruction=f"Add destination ({x}, {y})", status=self.get_status())

    def remove_destination(self, index, log):
        if index < len(self.destinations):
            log.write(instruction=f"Remove destination {self.destinations[index]}", status=self.get_status())
            self.destinations.pop(index)
        else:
            print("Error: Index out of range.")

    def update_destination(self, index, x, y, log):
        if index < len(self.destinations):
            log.write(instruction=f"Update destination {index} to ({x}, {y})", status=self.get_status())
            self.destinations[index] = (x, y)
        else:
            print("Error: Index out of range.")

    def get_status(self):
        return {"x": self.x, "y": self.y, "speed": self.speed, "direction": self.direction, "accel": self.accel, "status": self.status}

    def start(self, log):
        self.status = "moving"
        log.write(instruction="Start", status=self.get_status())

    def stop(self, log):
        self.status = "stopped"
        log.write(instruction="Stop", status=self.get_status())


class Log:
    def __init__(self, filename="log.json"):
        self.filename = filename

    def write(self, instruction=None, status=None):
        with open(self.filename, "a") as f:
            entry = {"time": time.time()}
            if instruction:
                entry["instruction"] = instruction
            if status:
                entry["status"] = status
            f.write(json.dumps(entry))
            f.write("\n")

    def read(self):
        with open(self.filename, "r") as f:
            for line in f:
                print(json.loads(line))