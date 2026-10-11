class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        rows, cols = len(matrix), len(matrix[0])

        # dr is change in right
        # dl is change in left
        x, y, dr, dl = 0, 0, 1, 0
        res = []

        for _ in range(rows * cols):
            res.append(matrix[y][x])
            matrix[y][x] = "#"

            if x + dr < 0 or x + dr >= cols or y + dl < 0 or y + dl >= rows or matrix[y + dl][x + dr] == "#":
                dr, dl = -dl, dr

            x += dr
            y += dl

        return res