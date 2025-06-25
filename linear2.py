def __main__(list, x):
    for i in range(0, len(list)):
        if list[i] == x:
            return True
    return False

list_items = [23, 5, 3, 2, 6, 43, 2, 7, 5, 34]
x = 43

if __main__(list_items, x):
    print("found", x)
else:
    print("not found", x)
