def hanoi_solver(disks):
    # Initialize rods
    src = [i for i in range(disks, 0, -1)]
    aux = []
    dest = []

    steps = []  # store all rod states

    # Save the starting state
    steps.append(f"{src.copy()} {aux.copy()} {dest.copy()}")

    def move(n, source, auxiliary, destination):
        if n == 0:
            return

        # Move n-1 disks from source to auxiliary
        move(n-1, source, destination, auxiliary)

        # Move nth disk from source to destination
        disk = source.pop()
        destination.append(disk)

        # Save the state of the rods in SRC, AUX, DEST order
        steps.append(f"{src.copy()} {aux.copy()} {dest.copy()}")

        # Move n-1 disks from auxiliary to destination
        move(n-1, auxiliary, source, destination)

    move(disks, src, aux, dest)
    return "\n".join(steps)

n=int(input("Enter the number of disks: "))
print(hanoi_solver(n))