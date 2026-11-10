def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]
    moves = []

    def record():
        moves.append(
            f"{rods[0]} {rods[1]} {rods[2]}"
        )

    def move_disk(source, destination):
        disk = rods[source].pop()
        rods[destination].append(disk)
        record()

    def solve(n, source, auxiliary, destination):
        if n == 1:
            move_disk(source, destination)
            return

        solve(n - 1, source, destination, auxiliary)
        move_disk(source, destination)
        solve(n - 1, auxiliary, source, destination)

    record()
    solve(n, 0, 1, 2)

    return "\n".join(moves)