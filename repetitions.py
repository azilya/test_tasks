with open("input_reps.txt") as f:
    n_lines = int(f.readline())
    prev = "None"
    for _ in range(n_lines):
        curr = f.readline().strip()
        if curr != prev:
            print(curr)
        prev = curr
