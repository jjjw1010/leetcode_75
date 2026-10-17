class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        # perform flood fill on image[sr][sc] w/ color
        nr = len(image)
        nc = len(image[0])
        old_color = image[sr][sc]
        if old_color == color: return image 

        def dfs(r, c):
            # change adjacent pixels if pixel share same original color of starting pixel
            if image[r][c] == old_color:
                image[r][c] = color
                if r > 0:
                    dfs(r - 1, c) # up
                if r < nr - 1:
                    dfs(r + 1, c) # down
                if c > 0:
                    dfs(r, c - 1) # left
                if c < nc - 1:
                    dfs(r, c + 1) # right
        dfs(sr, sc)
        return image