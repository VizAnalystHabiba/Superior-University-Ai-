def minimax(node, depth, maximizing_player):
    if depth == 0 or is_terminal(node):
        return evaluate(node)
    if maximizing_player:
        max_value = float('-inf')
        for child in generate_children(node):
            value = minimax(child, depth - 1, False)
            max_value = max(max_value, value)
        return max_value
    else:
        min_value = float('inf')
        for child in generate_children(node):
            value = minimax(child, depth - 1, True)
            min_value = min(min_value, value)
        return min_value

def is_terminal(node):
    return node in [10,-10]  

def evaluate(node):
    return node 

def generate_children(node):
    childern= []
    if node <10:
        childern.append(node +1)
        childern.append(node -1)
    return childern  
initial_state = 0  
search_depth = 7    
optimal_value = minimax(initial_state, search_depth, True)
print("The best value for the maximizing player is:", optimal_value)
