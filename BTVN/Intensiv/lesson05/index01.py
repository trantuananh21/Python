def sort_descending_list(inp_list):
    return inp_list.sort(reverse=True)

l = [90.12, 50.2, 20.0, 3.14159, 0.0, -12.2, -12.2, -1000.0, -99999999.0]
print(l.sort(reverse=True))