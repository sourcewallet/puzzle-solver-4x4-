import heapq
import itertools

# 目标状态
goal_state = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 0]
]

# 获取目标状态的位置字典，方便计算曼哈顿距离
goal_positions = {goal_state[i][j]: (i, j) for i in range(4) for j in range(4)}


# 曼哈顿距离的计算函数
def manhattan_distance(state):
    distance = 0
    for i in range(4):
        for j in range(4):
            if state[i][j] != 0:
                x, y = goal_positions[state[i][j]]
                distance += abs(x - i) + abs(y - j)
    return distance


# 获取空白块的位置
def find_blank(state):
    for i in range(4):
        for j in range(4):
            if state[i][j] == 0:
                return i, j


# 生成可能的移动
def generate_moves(state):
    blank_i, blank_j = find_blank(state)
    moves = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for di, dj in directions:
        new_i, new_j = blank_i + di, blank_j + dj
        if 0 <= new_i < 4 and 0 <= new_j < 4:
            new_state = [row[:] for row in state]
            new_state[blank_i][blank_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[blank_i][blank_j]
            moves.append(new_state)
    return moves


# A*算法求解拼图
def solve_puzzle(start_state):
    priority_queue = []
    heapq.heappush(priority_queue, (0 + manhattan_distance(start_state), 0, start_state, []))
    visited = set()
    visited.add(tuple(itertools.chain(*start_state)))

    while priority_queue:
        _, cost, current_state, path = heapq.heappop(priority_queue)

        if current_state == goal_state:
            return path + [current_state]

        for move in generate_moves(current_state):
            flattened_move = tuple(itertools.chain(*move))
            if flattened_move not in visited:
                visited.add(flattened_move)
                heapq.heappush(priority_queue,
                               (cost + 1 + manhattan_distance(move), cost + 1, move, path + [current_state]))


# 打印拼图状态
def print_puzzle(state):
    for row in state:
        print(' '.join(f'{num:2}' for num in row))
    print()


# 示例起始状态
start_state = [
    [5, 1, 2, 3],
    [4, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 0, 15]
]

# 求解拼图
solution_path = solve_puzzle(start_state)

# 打印解法路径
print(f"拼图复原需要的步数: {len(solution_path) - 1}")
for step in solution_path:
    print_puzzle(step)
