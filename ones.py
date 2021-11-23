with open("input_ones.txt") as f:
    n = int(f.readline().strip())
    c = ind = ind_max = 0
    while c < n:
        line = f.readline()
        if line.strip() == "1":
            ind += 1
        else:
            ind = 0
        ind_max = max(ind_max, ind)
        c += 1
    print(ind_max)
