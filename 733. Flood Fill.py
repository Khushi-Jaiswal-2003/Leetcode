image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
oldColor = image[sr][sc]

total_r = len(image)

total_c = len(image[0])

def dfs(sr, sc):
    if total_r > sr >= 0 and total_c > sc >= 0 and oldColor == image[sr][sc] and newColor != image[sr][sc]:
        image[sr][sc] = newColor
        print(image)
        dfs(sr + 1, sc)
        dfs(sr, sc + 1)
        dfs(sr - 1, sc)
        dfs(sr, sc - 1)

dfs(sr, sc)
print(image)