colu = int(input('Enter a column number: '))
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
for col in number_grid:
    try:
        print(col[colu])
    except:
        print("invalid number")