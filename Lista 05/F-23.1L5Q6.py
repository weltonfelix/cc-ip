X_BLOCK = "X"
H_BLOCK = "H"
EMPTY_SPACE = "O"
EXIT = "sair"

grid_size = int(input())


def load_grid(rows_left, grid_size, current_grid=[]):
    if rows_left == 0:
        return current_grid

    current_grid_copy = current_grid.copy()
    row = list(input())

    for block in range(grid_size):
        if row[block] not in [X_BLOCK, H_BLOCK]:
            row[block] = EMPTY_SPACE

    current_grid_copy.append(row)

    return load_grid(rows_left - 1, grid_size, current_grid_copy)


def get_column(grid, column_index, line_index=0, partial_column=[]):
    if line_index == len(grid):
        return partial_column

    if line_index == 0:
        partial_column = [""] * len(grid)

    partial_column[line_index] = grid[line_index][column_index]

    return get_column(grid, column_index, line_index + 1, partial_column)


def merge_column(grid, column, column_index, current_line_index=0):
    if current_line_index == len(column):
        return grid
    else:
        grid[current_line_index][column_index] = column[current_line_index]
        return merge_column(grid, column, column_index, current_line_index + 1)


def run_fall(grid, current_column_index=0):
    if current_column_index == len(grid):
        return grid
    else:
        raw_column = get_column(grid, current_column_index)
        processed_column = run_column(raw_column, len(raw_column) - 1)
        grid = merge_column(grid, processed_column, current_column_index)

        return run_fall(grid, current_column_index + 1)


def run_column(column, current_line=-2):
    if current_line == -1:
        return column

    if current_line < len(column) - 1:
        if column[current_line] in [X_BLOCK, H_BLOCK]:
            if column[current_line + 1] == EMPTY_SPACE:
                column[current_line + 1] = column[current_line]
                column[current_line] = EMPTY_SPACE

                if (
                    current_line < len(column) - 2
                    and column[current_line + 2] == EMPTY_SPACE
                ):
                    return run_column(column, current_line + 1)

        return run_column(column, current_line - 1)
    else:
        return run_column(column, current_line - 1)


def count_points(grid, grid_size, current_line=0, eliminated_lines=0, current_points=0):
    if current_line == len(grid):
        return grid, current_points, eliminated_lines

    else:
        line = grid[current_line]

        if all(col == X_BLOCK for col in line):
            grid[current_line] = [EMPTY_SPACE] * grid_size
            current_points += (len(grid) ** 2) * max(len(grid), eliminated_lines)

            eliminated_lines += 1

        return count_points(
            grid, grid_size, current_line + 1, eliminated_lines, current_points
        )


def run_round(grid, points=0, eliminated_lines=0):
    grid = run_fall(grid)

    grid, new_points, eliminated_lines = count_points(
        grid, grid_size, eliminated_lines=eliminated_lines, current_points=points
    )

    if new_points != points:
        return run_round(grid, new_points, eliminated_lines)

    return grid, new_points, eliminated_lines


def substitutions(grid, grid_size, points, eliminated_lines):
    current_input = input()
    if current_input == EXIT:
        return grid, points

    line, column, block = current_input.split(",")
    line = int(line)
    column = int(column)

    if line in range(0, grid_size) and column in range(0, grid_size):
        if grid[line][column] == EMPTY_SPACE:
            grid[line][column] = block if block in [X_BLOCK, H_BLOCK] else EMPTY_SPACE

            grid, points, eliminated_lines = run_round(grid, points, eliminated_lines)

    return substitutions(grid, grid_size, points, eliminated_lines)


def print_grid(grid):
    for line in grid:
        print("".join(line))


grid = load_grid(grid_size, grid_size)

grid, points, eliminated_lines = run_round(grid)

grid, points = substitutions(grid, grid_size, points, eliminated_lines)

print("Resultado:")
print_grid(grid)

print(f"Pontuação: {points}")
