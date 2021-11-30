from random import randint
from os import system
def printGrid(grid):
	for row in grid:
		print("| ", end="")
		for i in row:
			print(i, end=" | ")
		print()

def transpose(grid):
    newGrid = []
    for i in range(4):
        newGrid.append([])
        for j in range(4):
            newGrid[i].append(grid[j][i])
    return newGrid

def reverse(grid):
	newGrid = []
	for row in grid:
		newGrid.append(row[::-1])
	return newGrid

def insertIntoGrid(grid, gridLength):
	while True:
		a, b = randint(0, gridLength-1), randint(0, gridLength-1)
		if grid[a][b] == 0:
			grid[a][b] = 2
			break
	return grid

def swipeRight(grid):
	for row in grid:
		if sum(row) != 0:
			for i in range(len(row) - 1):
				if row[i] != 0 and row[i + 1] == 0:
					row[i + 1] = row[i]
					row[i] = 0
				elif row[i] != 0 and row[i] == row[i + 1]:
					row[i + 1] = row[i] * 2
					row[i] = 0
	insertIntoGrid(grid, len(row))
	return grid

def swipeDown(grid):
	grid = transpose(grid)
	grid = swipeRight(grid)
	grid = transpose(grid)
	return grid

def swipeLeft(grid):
	grid = reverse(grid)
	grid = swipeRight(grid)
	grid = reverse(grid)
	return grid

def swipeUp(grid):
	grid = transpose(grid)
	grid = swipeLeft(grid)
	grid = transpose(grid)
	return grid

gridLength = int(input("Enter the length of the grid: "))
grid = [[0 for x in range(gridLength)] for y in range(gridLength)]
grid = insertIntoGrid(grid, gridLength)
while True:
	system("cls")
	print("""
1. Swipe Right
2. Swipe Left
3. Swipe Up
4. Swipe Down
5. Quit
""")
	printGrid(grid)
	choice = int(input("Enter your choice: "))
	if choice == 1:
		grid = swipeRight(grid)
	elif choice == 2:
		grid = swipeLeft(grid)
	elif choice == 3:
		grid = swipeUp(grid)
	elif choice == 4:
		grid = swipeDown(grid)
	elif choice == 5:
		break
