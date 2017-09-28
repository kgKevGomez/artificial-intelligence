import sys
from queue import Queue

class State:
    def __init__(self, value, top, down, left, right):
        self.value = value
        self.top = top
        self.down = down
        self.left = left
        self.right = right

    def __str__(self):
        return f'VALUE: {self.value}, UP: {self.top}, DOWN: {self.down}, LEFT: {self.left}, RIGHT: {self.right}'

    def __eq__(self, other):
        return self.value == other.value and self.top == other.top and self.left == other.left and self.right == other.right

goal_state = State(0, None, 3, None, 1)

# Nodes are always visited in UDLR order

def bfs(state_map):
    current_state = state_map[0]
    if current_state == goal_state:
        return
    
    queue = Queue()
    explored = set()
    for step in ['top', 'down', 'left', 'right']:
        step_state = getattr(current_state, step)
        if not step_state is None and not state_map in queue and not state_map in explored:
            queue.put(step_state)
    
    print(queue)
    

def dfs(state_map):
    pass

def generate_state_map(initial_board):
    board = [initial_board[:3], initial_board[3:6], initial_board[6:9]]
    state_map = {}

    for y in range(3):
        for x in range(3):
            value = board[y][x]

            indexes = {
                'top': (y - 1, x),
                'down': (y + 1, x),
                'left': (y, x - 1),
                'right': (y, x + 1)
            }

            values = {
                'top': None if indexes['top'][0] < 0 else board[indexes['top'][0]][indexes['top'][1]],
                'down': None if indexes['down'][0] > 2 else board[indexes['down'][0]][indexes['down'][1]],
                'left': None if indexes['left'][1] < 0 else board[indexes['left'][0]][indexes['left'][1]],
                'right': None if indexes['right'][1] > 2 else board[indexes['right'][0]][indexes['right'][1]],
            }

            state_map[value] = State(value=value, top=values['top'], down=values['down'], left=values['left'], right=values['right'])
    return state_map

def solve(search_type, provided_initial_board):
    switcher = {
        'bfs': bfs,
        'dfs': dfs,
    }
    # Get the function from switcher dictionary
    func = switcher.get(search_type, lambda: "The requested search type isn't supported")
    # Execute the function
    return func(generate_state_map(provided_initial_board))

requested_search_type = 'bfs' #sys.argv[0]
provided_initial_board = [1, 2, 5, 3, 4, 0, 6, 7, 8] #sys.argv[1]

solve(requested_search_type, provided_initial_board)
