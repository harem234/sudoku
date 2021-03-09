import numpy as np

M, N = 9, 9
# 0 mean the cell is empty
# 1 to 9 is a value for the cell
# SUDO_MAP_INIT = ((5, 3, 4, 6, 7, 8, 9, 1, 2),
#                  (6, 7, 2, 1, 9, 5, 3, 4, 8),
#                  (1, 9, 8, 3, 4, 2, 5, 6, 7),
#
#                  (8, 5, 9, 7, 6, 1, 4, 2, 3),
#                  (4, 2, 6, 8, 5, 3, 7, 9, 1),
#                  (7, 1, 3, 9, 2, 4, 8, 5, 6),
#
#                  (0, 6, 0, 5, 3, 7, 2, 8, 0),
#                  (0, 0, 0, 4, 1, 9, 0, 0, 5),
#                  (0, 0, 0, 0, 8, 0, 0, 7, 9),)
# with numpy

SUDO_MAP_INIT = np.array(
    [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [0, 6, 0, 0, 0, 7, 2, 8, 4],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ],
    np.int32,
)

SUDO_MAP_FINAL = np.array(
    [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9],
    ],
    np.int32,
)

# Version 1, 2
R = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
}
C = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
}
S = {
    (0, 0): [],
    (0, 1): [],
    (0, 2): [],
    (1, 0): [],
    (1, 1): [],
    (1, 2): [],
    (2, 0): [],
    (2, 1): [],
    (2, 2): [],
}


EMPTY_CELLS: set = set()

# {(i,j): cell_val}
VALUES_TRACE = dict()

SQUARE_MAP: dict = {
    # 0, 0
    **dict.fromkeys(
        (
            (0, 0),
            (0, 1),
            (0, 2),
            (1, 0),
            (1, 1),
            (1, 2),
            (2, 0),
            (2, 1),
            (2, 2),
        ),
        (0, 0),
    ),
    # 0, 1
    **dict.fromkeys(
        (
            (0, 3),
            (0, 4),
            (0, 5),
            (1, 3),
            (1, 4),
            (1, 5),
            (2, 3),
            (2, 4),
            (2, 5),
        ),
        (0, 1),
    ),
    # 0, 2
    **dict.fromkeys(
        (
            (0, 6),
            (0, 7),
            (0, 8),
            (1, 6),
            (1, 7),
            (1, 8),
            (2, 6),
            (2, 7),
            (2, 8),
        ),
        (0, 2),
    ),
    # 1, 0
    **dict.fromkeys(
        (
            (3, 0),
            (3, 1),
            (3, 2),
            (4, 0),
            (4, 1),
            (4, 2),
            (5, 0),
            (5, 1),
            (5, 2),
        ),
        (1, 0),
    ),
    # 1, 1
    **dict.fromkeys(
        (
            (3, 3),
            (3, 4),
            (3, 5),
            (4, 3),
            (4, 4),
            (4, 5),
            (5, 3),
            (5, 4),
            (5, 5),
        ),
        (1, 1),
    ),
    # 1, 2
    **dict.fromkeys(
        (
            (3, 6),
            (3, 7),
            (3, 8),
            (4, 6),
            (4, 7),
            (4, 8),
            (5, 6),
            (5, 7),
            (5, 8),
        ),
        (1, 2),
    ),
    # 2, 0
    **dict.fromkeys(
        (
            (6, 0),
            (6, 1),
            (6, 2),
            (7, 0),
            (7, 1),
            (7, 2),
            (8, 0),
            (8, 1),
            (8, 2),
        ),
        (2, 0),
    ),
    # 2, 1
    **dict.fromkeys(
        (
            (6, 3),
            (6, 4),
            (6, 5),
            (7, 3),
            (7, 4),
            (7, 5),
            (8, 3),
            (8, 4),
            (8, 5),
        ),
        (2, 1),
    ),
    # 2, 2
    **dict.fromkeys(
        (
            (6, 6),
            (6, 7),
            (6, 8),
            (7, 6),
            (7, 7),
            (7, 8),
            (8, 6),
            (8, 7),
            (8, 8),
        ),
        (2, 2),
    ),
}


def init_rcs():
    global SUDO_MAP_INIT, M, N
    full_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    x, y = M, N

    for i in range(x):
        r_set = set()
        for j in range(y):
            if SUDO_MAP_INIT[i][j] != 0:
                r_set.add(SUDO_MAP_INIT[i][j])

        R[i].append(full_set - r_set)

    for j in range(y):
        c_set = set()
        for i in range(x):
            if SUDO_MAP_INIT[i][j] != 0:
                c_set.add(SUDO_MAP_INIT[i][j])

        C[j].append(full_set - c_set)

    for m in range(0, 7, 3):
        for n in range(0, 7, 3):

            s_set = set()

            for i in range(3):
                for j in range(3):

                    if SUDO_MAP_INIT[m + i][n + j] != 0:
                        s_set.add(SUDO_MAP_INIT[m + i][n + j])

            S[SQUARE_MAP[(m, n)]].append(full_set - s_set)


# def generate_square_map(m, n):
def populate_empty_cells():
    global EMPTY_CELLS, SUDO_MAP_INIT
    for i in range(len(SUDO_MAP_INIT)):
        for j in range(len(SUDO_MAP_INIT[0])):
            if SUDO_MAP_INIT[i][j] == 0:
                EMPTY_CELLS.add(
                    (
                        i,
                        j,
                    )
                )


def possible_values_for_cell(i, j):
    return R[i][-1] & C[j][-1] & S[SQUARE_MAP[(i, j)]][-1]


def update_rcs(
    i,
    j,
    val,
):
    global R, C, S

    r = R[i][-1] - {val}
    c = C[j][-1] - {val}
    s = S[SQUARE_MAP[(i, j)]][-1] - {val}

    R[i].append(r)
    C[j].append(c)
    S[SQUARE_MAP[(i, j)]].append(s)


def delete_rcs(
    i,
    j,
):
    global R, C, S

    R[i].pop()
    C[j].pop()
    S[SQUARE_MAP[(i, j)]].pop()


def recursive_sudoku():
    global EMPTY_CELLS

    for (
        i,
        j,
    ) in EMPTY_CELLS:
        possible_values = possible_values_for_cell(i, j)

        for val in possible_values:

            update_rcs(
                i,
                j,
                val,
            )
            EMPTY_CELLS.remove(
                (
                    i,
                    j,
                )
            )
            VALUES_TRACE[
                (
                    i,
                    j,
                )
            ] = val

            recursive_sudoku()

            if len(EMPTY_CELLS) == 0:
                # "solved"
                return

            EMPTY_CELLS.add(
                (i, j),
            )
            delete_rcs(i, j)
            VALUES_TRACE.pop(
                (
                    i,
                    j,
                )
            )


populate_empty_cells()

init_rcs()

# del SUDO_MAP_INIT

recursive_sudoku()

print(VALUES_TRACE)

# test result
for i, j in VALUES_TRACE.keys():
    SUDO_MAP_INIT[i][j] = VALUES_TRACE[(i, j)]
print(SUDO_MAP_FINAL == SUDO_MAP_INIT)
