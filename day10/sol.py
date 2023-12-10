#!/bin/python3

from collections import defaultdict
import sys
from typing import List

FILE = sys.argv[1] if len(sys.argv) > 1 else "input"


def read_lines_to_list() -> List[str]:
    lines: List[str] = []
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            lines.append(list(line))

    return lines


def find_start(maze: List[List[str]]):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == "S":
                return (row, col)


def print_maze(maze: List[List[str]], visited: dict):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if (i, j) in visited:
                print(visited[(i, j)], end="")
            else:
                print(maze[i][j], end="")

        print("")


def blow_up_maze(maze: List[List[str]]) -> List[List[str]]:
    """Expands a maze to 3x the size, and then also adds a perimeter around the entire thing."""

    WIDTH = 3

    blown_up_maze = [[]]
    for i in range((len(maze[0]) + 2) * WIDTH):
        blown_up_maze[-1].append(" ")
    blown_up_maze.append([])
    for i in range((len(maze[0]) + 2) * WIDTH):
        blown_up_maze[-1].append(" ")
    for i in range(len(maze)):
        blown_up_maze.append(list("   "))
        blown_up_maze.append(list("   "))
        blown_up_maze.append(list("   "))
        for j in range(len(maze[i])):
            if maze[i][j] == "-":
                blown_up_maze[-1].extend(list("   "))
                blown_up_maze[-2].extend(list("███"))
                blown_up_maze[-3].extend(list("   "))
            elif maze[i][j] == "|":
                blown_up_maze[-1].extend(list(" █ "))
                blown_up_maze[-2].extend(list(" █ "))
                blown_up_maze[-3].extend(list(" █ "))
            elif maze[i][j] == "L":
                blown_up_maze[-3].extend(list(" █ "))
                blown_up_maze[-2].extend(list(" ██"))
                blown_up_maze[-1].extend(list("   "))
            elif maze[i][j] == "J":
                blown_up_maze[-3].extend(list(" █ "))
                blown_up_maze[-2].extend(list("██ "))
                blown_up_maze[-1].extend(list("   "))
            elif maze[i][j] == "7":
                blown_up_maze[-3].extend(list("   "))
                blown_up_maze[-2].extend(list("██ "))
                blown_up_maze[-1].extend(list(" █ "))
            elif maze[i][j] == "F":
                blown_up_maze[-3].extend(list("   "))
                blown_up_maze[-2].extend(list(" ██"))
                blown_up_maze[-1].extend(list(" █ "))
            else:
                blown_up_maze[-1].extend(list("   "))
                blown_up_maze[-2].extend(list("   "))
                blown_up_maze[-3].extend(list("   "))
        blown_up_maze[-1].extend(list("   "))
        blown_up_maze[-2].extend(list("   "))
        blown_up_maze[-3].extend(list("   "))

    blown_up_maze.append([])
    for i in range((len(maze[0]) + 2) * WIDTH):
        blown_up_maze[-1].append(" ")
    blown_up_maze.append([])
    for i in range((len(maze[0]) + 2) * WIDTH):
        blown_up_maze[-1].append(" ")
    return blown_up_maze


def pretty_print_maze(maze: List[List[str]]):
    for row in maze:
        for col in row:
            print(col, end="")
        print("")


def valid_coord(y, x, maze) -> bool:
    return y >= 0 and x >= 0 and y < len(maze) and x < len(maze[0])


def part_one():
    maze = read_lines_to_list()
    start = find_start(maze)

    neighbours = defaultdict(set)
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            value = maze[row][col]
            if value == "|":
                neighbours[(row, col)].add((row - 1, col))
                neighbours[(row, col)].add((row + 1, col))
            elif value == "-":
                neighbours[(row, col)].add((row, col - 1))
                neighbours[(row, col)].add((row, col + 1))
            elif value == "L":
                neighbours[(row, col)].add((row - 1, col))
                neighbours[(row, col)].add((row, col + 1))
            elif value == "J":
                neighbours[(row, col)].add((row - 1, col))
                neighbours[(row, col)].add((row, col - 1))
            elif value == "7":
                neighbours[(row, col)].add((row + 1, col))
                neighbours[(row, col)].add((row, col - 1))
            elif value == "F":
                neighbours[(row, col)].add((row + 1, col))
                neighbours[(row, col)].add((row, col + 1))

    keys = list(neighbours.keys())
    for key in keys:
        neighbour = neighbours[key]
        for n in neighbour:
            if n == start:
                neighbours[start].add(key)

    queue = [start]
    visited = dict()
    visited[start] = 0

    while queue:
        curr = queue.pop(0)
        for candidate in neighbours[curr]:
            if (
                candidate[0] >= 0
                and candidate[1] >= 0
                and candidate[0] < len(maze)
                and candidate[1] < len(maze[0])
                and candidate not in visited
            ):
                visited[candidate] = visited[curr] + 1
                queue.append(candidate)

    answer = max(visited.values())
    # print_maze(maze, visited)

    print(f"Part 1: {answer}")


def part_two():
    maze = read_lines_to_list()
    start = find_start(maze)

    neighbours_list = defaultdict(set)
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            value = maze[row][col]
            if value == "|":
                if row - 1 >= 0:
                    neighbours_list[(row, col)].add((row - 1, col))
                if row + 1 < len(maze):
                    neighbours_list[(row, col)].add((row + 1, col))
            elif value == "-":
                if col - 1 >= 0:
                    neighbours_list[(row, col)].add((row, col - 1))
                if col + 1 < len(maze[row]):
                    neighbours_list[(row, col)].add((row, col + 1))
            elif value == "L":
                if row - 1 >= 0:
                    neighbours_list[(row, col)].add((row - 1, col))
                if col + 1 < len(maze[row]):
                    neighbours_list[(row, col)].add((row, col + 1))
            elif value == "J":
                if row - 1 >= 0:
                    neighbours_list[(row, col)].add((row - 1, col))
                if col - 1 >= 0:
                    neighbours_list[(row, col)].add((row, col - 1))
            elif value == "7":
                if row + 1 < len(maze):
                    neighbours_list[(row, col)].add((row + 1, col))
                if col - 1 >= 0:
                    neighbours_list[(row, col)].add((row, col - 1))
            elif value == "F":
                if row + 1 < len(maze):
                    neighbours_list[(row, col)].add((row + 1, col))
                if col + 1 < len(maze[row]):
                    neighbours_list[(row, col)].add((row, col + 1))

    keys = list(neighbours_list.keys())
    for key in keys:
        neighbours = neighbours_list[key]
        for neighbour in neighbours:
            if neighbour == start:
                neighbours_list[start].add(key)

    west = {
        "-",
        "J",
        "7",
    }
    east = {
        "-",
        "L",
        "F",
    }
    north = {"|", "L", "J"}
    south = {"|", "7", "F"}
    start_type = {"-", "J", "7", "|", "L", "F"}

    if (start[0] - 1, start[1]) in neighbours_list[start]:
        start_type = start_type.intersection(north)

    if (start[0] + 1, start[1]) in neighbours_list[start]:
        start_type = start_type.intersection(south)

    if (start[0], start[1] - 1) in neighbours_list[start]:
        start_type = start_type.intersection(west)

    if (start[0], start[1] + 1) in neighbours_list[start]:
        start_type = start_type.intersection(east)

    start_type = list(start_type)[0]
    maze[start[0]][start[1]] = start_type

    # print_maze(maze, {})

    # Remove any pipes that are not part of the loop, and replace them with empty space.
    to_remove = set()
    to_check = list(neighbours_list.keys())
    for key in to_check:
        num_connects = 0
        for neighbour in neighbours_list[key]:
            if key in neighbours_list[neighbour]:
                num_connects += 1

        if num_connects != 2:
            # Make sure to re-check neighbours...
            to_check.extend(neighbours_list[key])
            to_remove.add(key)
            del neighbours_list[key]

    # print(to_remove)
    for r in to_remove:
        maze[r[0]][r[1]] = "."

    # print("")
    # print_maze(maze, {})

    big_maze = blow_up_maze(maze)

    # Now just do flood-fill.
    queue = [(0, 0)]
    visited = set()
    visited.add((0, 0))
    big_maze[0][0] = "X"

    # pretty_print_maze(big_maze)

    while queue:
        (y, x) = queue.pop(0)

        if y - 1 >= 0 and (y - 1, x) not in visited and big_maze[y - 1][x] != "█":
            queue.append((y - 1, x))
            visited.add((y - 1, x))
            big_maze[y - 1][x] = "X"

        if y + 1 < len(big_maze) and (y + 1, x) not in visited and big_maze[y + 1][x] != "█":
            queue.append((y + 1, x))
            visited.add((y + 1, x))
            big_maze[y + 1][x] = "X"

        if x - 1 >= 0 and (y, x - 1) not in visited and big_maze[y][x - 1] != "█":
            queue.append((y, x - 1))
            visited.add((y, x - 1))
            big_maze[y][x - 1] = "X"

        if x + 1 < len(big_maze[y]) and (y, x + 1) not in visited and big_maze[y][x + 1] != "█":
            queue.append((y, x + 1))
            visited.add((y, x + 1))
            big_maze[y][x + 1] = "X"

    # pretty_print_maze(big_maze)
    # print("")

    answer = 0
    for row in range(len(big_maze)):
        for col in range(len(big_maze[row])):
            if big_maze[row][col] == " ":
                any_bad = False
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if (
                            row + i < 0
                            or row + i >= len(big_maze)
                            or col + j < 0
                            or col + j >= len(big_maze[i])
                            or big_maze[row + i][col + j] != " "
                        ):
                            any_bad = True

                if not any_bad:
                    for i in [-1, 0, 1]:
                        for j in [-1, 0, 1]:
                            big_maze[row + i][col + j] = "O"
                    answer += 1

    pretty_print_maze(big_maze)
    print(f"Part 2: {answer}")


# part_one()
part_two()

