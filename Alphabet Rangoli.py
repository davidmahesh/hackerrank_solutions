def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    width = 4 * size - 3
    rows = []
    for i in range(size):
        row = "-".join(alpha[size-1:i:-1] + alpha[i:size])
        rows.append(row.center(width, "-"))

    for r in rows[::-1] + rows[1:]:
        print(r)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)