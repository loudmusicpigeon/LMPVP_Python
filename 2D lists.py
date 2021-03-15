colu = float(input('Enter a column number: '))
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
if colu == 0:
    for row in number_grid:
        print(number_grid[0][0])
    