def pascal_triangle(row):
    if not row:
        return [1]
    return [left + right for left, right in zip([0] + row, row + [0])]

print(pascal_triangle([1, 2, 1]))
print(pascal_triangle([]))
print(pascal_triangle([1, 4, 6, 4, 1]))