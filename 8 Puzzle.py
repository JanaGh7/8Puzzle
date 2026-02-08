from collections import deque
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import heapq
import math
import time

class Node:
    def __init__(self, value, level):
        self.parent = None
        self.value = value
        self.level = level
    def __lt__(self, other):
        return self.value < other.value
path = []
# Movement functions
def up(state, id):
    st = str(state.value).zfill(9)
    mod = list(st)
    if id < 4:
        return None
    else:
        mod[id - 1], mod[id - 4] = mod[id - 4], mod[id - 1]
        return int("".join(mod))

def down(state, id):
    st = str(state.value).zfill(9)
    mod = list(st)
    if id > 6:
        return None
    else:
        mod[id - 1], mod[id + 2] = mod[id + 2], mod[id - 1]
        return int("".join(mod))

def right(state, id):
    st = str(state.value).zfill(9)
    mod = list(st)
    if id in [3, 6, 9]:
        return None
    else:
        mod[id - 1], mod[id] = mod[id], mod[id - 1]
        return int("".join(mod))

def left(state, id):
    st = str(state.value).zfill(9)
    mod = list(st)
    if id in [1, 4, 7]:
        return None
    else:
        mod[id - 1], mod[id - 2] = mod[id - 2], mod[id - 1]
        return int("".join(mod))

def getNeighbours(state):
    st = str(state.value).zfill(9)
    mod = list(st)
    id = mod.index("0") + 1
    return [move for move in (left(state, id), right(state, id), up(state, id), down(state, id)) if move is not None]

# BFS function
def BFS():
    global path
    goal = 12345678
    initial = int(case.get())
    root = Node(initial,1)
    frontier = deque()
    frontier.append(root)
    visited = []
    start_time=time.time()
    while len(frontier) != 0:
        state = frontier.popleft()
        visited.append(state)
        if state.value == goal:
            path = []
            while state is not None:
                path.append(state.value)
                state = state.parent
            print("Path:")
            for move in path[::-1]:
                print(move)
            print("")
            print("Depth and cost:", len(path))
            print("")
            print("Expanded Nodes:",len(visited))
            end_time=time.time()
            print("Time:",(end_time-start_time)*1000,"Milliseconds")
            return True
        for n in getNeighbours(state):
            if all(node.value != n for node in frontier) and all(node.value != n for node in visited):
                nn = Node(n, (state.level)+1)
                nn.parent = state
                frontier.append(nn)
    end_time=time.time()
    print("Time:",(end_time-start_time)*1000,"Milliseconds")
    return False

# DFS function
def DFS():
    global path
    goal = 12345678
    initial = int(case.get())
    root = Node(initial,1)
    frontier = []
    frontier.append(root)
    visited = []
    start_time=time.time()
    while frontier:
        state = frontier.pop()
        visited.append(state)
        if state.value == goal:
            path = []
            while state is not None:
                path.append(state.value)
                state = state.parent
            print("Path:")
            for move in path[::-1]:
                print(move)
            print("")
            print("Depth and cost:", len(path))
            print("")
            print("Expanded Nodes:",len(visited))
            end_time=time.time()
            print("Time:",(end_time-start_time)*1000,"Milliseconds")
            return True
        for n in getNeighbours(state):
            if all(node.value != n for node in frontier) and all(node.value != n for node in visited) :
                nn = Node(n, (state.level)+1)
                nn.parent = state
                frontier.append(nn)
    end_time=time.time()
    print("Time:",(end_time-start_time)*1000,"Milliseconds")
    return False

#IDFS function
def IDFS():
    global path
    goal = 12345678
    initial = int(case.get())
    max_depth = int(dep.get())
    start_time=time.time()
    for i in range (max_depth+1):
        print("Trying with max depth =",i)
        root = Node(initial,1)
        frontier = []
        frontier.append(root)
        visited = []
  
        while frontier:
            state = frontier.pop()
            visited.append(state)
            if state.value == goal:
                path = []
                while state is not None:
                    path.append(state.value)
                    state = state.parent
                print("Path:")
                for move in path[::-1]:
                    print(move)
                print("")
                print("Depth and cost:", len(path))
                print("")
                print("Expanded Nodes:",len(visited))
                end_time=time.time()
                print("Time:",(end_time-start_time)*1000,"Millisecondss")
                return True
            if(state.level<i):
                for n in getNeighbours(state):
                    if all(node.value != n for node in frontier) and all(node.value != n for node in visited):
                        nn = Node(n, (state.level)+1)
                        nn.parent = state
                        frontier.append(nn)
    end_time=time.time()
    print("Time:",(end_time-start_time)*1000,"Milliseconds")
    return False


def manhattan_distance(state):
    distance = 0
    st = str(state.value).zfill(9)
    goal = "012345678"
    i=0
    for value in st:
        if value != '0':
            goal_index = goal.index(value)
            x1, y1 = i // 3, i % 3
            x2, y2 = goal_index // 3, goal_index % 3
            distance += abs(x1 - x2) + abs(y1 - y2)
        i=i+1
    return distance


def euclidean_distance(state):
    distance = 0
    st = str(state.value).zfill(9)
    goal = "012345678"
    i=0
    for value in st:
        if value != '0':
            goal_index = goal.index(value)
            x1, y1 = i // 3, i % 3
            x2, y2 = goal_index // 3, goal_index % 3
            distance += math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        i=i+1
    return distance


# A* function
def A_star():
    global path
    goal = 12345678
    initial =int(case.get())
    root = Node(initial,1)

    frontier = []
    heapq.heappush(frontier, (0, root))

    visited = {}
    visited[root.value] = 0
    start_time=time.time()
    if(heur.get()=="E"):
        print("Used heuristic: Euclidian distance")
    elif(heur.get()=="M"):
        print("Used heuristic: Manhattan distance")
    while frontier:
        _, state = heapq.heappop(frontier)
        if state.value == goal:
            path = []
            while state:
                path.append(state.value)
                state = state.parent
            print("Path:")
            for move in path[::-1]:
                print(move)
            print("Depth and cost:", len(path))
            print("Expanded Nodes:", len(visited))
            end_time=time.time()
            print("Time:",(end_time-start_time)*1000,"Milliseconds")
            return True

        for n in getNeighbours(state):
            nn = Node(n,(state.level)+1)
            nn.parent = state
            g_cost = visited[state.value] + 1

            # Select method
            if(heur.get()=="E"):
                h_cost = euclidean_distance(nn)
            elif(heur.get()=="M"):
                h_cost = manhattan_distance(nn)
            f_cost = g_cost + h_cost 
            if n not in visited or g_cost < visited[n]:
                visited[n] = g_cost
                heapq.heappush(frontier, (f_cost, nn))
    end_time=time.time()
    print("Time:",(end_time-start_time)*10000,"Milliseconds")
    return False


# GUI Part
Eight_Puzzle = Tk()
Eight_Puzzle.title("8 Puzzle")
Eight_Puzzle.geometry("240x600")

the_text = Label(Eight_Puzzle, text="Enter the initial case", height=2, font=("Arial", 15))
the_text.grid(row=0, column=0, columnspan=3)

case = StringVar()
case.set("012345678")  # Default case

case_input = Entry(Eight_Puzzle, width=9, font=("Arial", 30), textvariable=case)
case_input.grid(row=1, column=0, columnspan=3)

# Buttons for BFS and DFS
btn1 = Button(Eight_Puzzle, text="BFS", width=12, height=2, bg="#3d72dc", fg="white", borderwidth=0, command=lambda: BFS_and_update())
btn1.grid(row=2, column=0, columnspan=3, pady=3)

btn2 = Button(Eight_Puzzle, text="DFS", width=12, height=2, bg="#e91e63", fg="white", borderwidth=0, command=lambda: DFS_and_update())
btn2.grid(row=3, column=0, columnspan=3, pady=3)

btn3 = Button(Eight_Puzzle, text="IDFS", width=12, height=2, bg="#e91e63", fg="white", borderwidth=0, command=lambda: IDFS_and_update())
btn3.grid(row=4, column=0, columnspan=3, pady=3)

dep = StringVar()
dep.set("5") 
dep_input = Entry(Eight_Puzzle, width=3, font=("Arial", 8), textvariable=dep)
dep_input.grid(row=4, column=2, columnspan=3)

btn4 = Button(Eight_Puzzle, text="A*", width=12, height=2, bg="#008000", fg="white", borderwidth=0, command=lambda: ASTAR_and_update())
btn4.grid(row=5, column=0, columnspan=3, pady=3)

heur = StringVar()
heur.set("E") 
heur_input = Entry(Eight_Puzzle, width=3, font=("Arial", 8), textvariable=heur)
heur_input.grid(row=5, column=2, columnspan=3)

btn5 = Button(Eight_Puzzle, text="next", width=20, height=2, bg="#000000", fg="white", borderwidth=0 , command=lambda:Next_step())
btn5.grid(row=10, column=0, columnspan=3, pady=3)

# Create the puzzle grid
buttons = []
for i in range(3):
    row = []
    for j in range(3):
        btn = Button(Eight_Puzzle, text="", font=("Arial", 20), width=4, height=2)
        btn.grid(row=i + 7, column=j, padx=3, pady=3)  # Using grid for the puzzle buttons
        row.append(btn)
    buttons.append(row)

# Function to update the grid based on current puzzle state
def update_grid(state):
    st = str(state).zfill(9)
    for i in range(9):
        value = st[i]
        buttons[i // 3][i % 3].config(text=value if value != "0" else "", state=tk.NORMAL)

# Override BFS and DFS to update grid after solving
def BFS_and_update():
    if BFS():
        reset_counter()
        update_grid(int(case.get()))

def DFS_and_update():
    if DFS():
        reset_counter()
        update_grid(int(case.get()))

def IDFS_and_update():
    if IDFS():
        reset_counter()
        update_grid(int(case.get()))

def ASTAR_and_update():
    if A_star():
        reset_counter()
        update_grid(int(case.get()))

# Global counter
counter = 0

def increment():
    global counter  # Declare the global variable
    counter += 1

def reset_counter():
    global counter  # Declare as global
    counter = 1  # Reset the counter to 0
    print("Counter has been reset.")  # Optional print statement for debugging

def Next_step():
    global counter  # Ensure the counter is declared as global
    if counter < len(path):  # Check if the counter is within the bounds of path
        move = path[-(counter + 1)]  # Get the current move (reversing path if needed)
        update_grid(move)  # Update grid to show the next step
        increment()  # Increment the counter
    else:
        print("Reached the end of the path.")   

Eight_Puzzle.mainloop()
