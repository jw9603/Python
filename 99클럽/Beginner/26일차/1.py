def solution(wallpaper):
    
    x = []
    y = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                x.append(i)
                y.append(j)
    return [min(x),min(y),max(x)+1,max(y)+1]

if __name__ == '__main__':
    print(solution([".#...", "..#..", "...#."]))
    print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))
    print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))
    print(solution(["..", "#."]))