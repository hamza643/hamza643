
def minimax(node, depth, maximizing_player):

    if depth == 0 or isinstance(node, int):  
        return node

    if maximizing_player:
        max_eval = float('-inf')
        for child in node:
            eval = minimax(child, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for child in node:
            eval = minimax(child, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval


def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player):

    if depth == 0 or isinstance(node, int):  
        return node

    if maximizing_player:
        max_eval = float('-inf')
        for child in node:
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, max_eval)
            if beta <= alpha:
                break  # Beta 
        return max_eval

    else:
        min_eval = float('inf')
        for child in node:
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, min_eval)
            if beta <= alpha:
                break  # Alpha 
        return min_eval



if __name__ == "__main__":
   
    tree = [  
        [3, 5],  
        [2, 9]   
    ]
    root = [tree[0], tree[1]] 


    print("Optimal value (Minimax):", minimax(root, 3, True))
    print("Optimal value (Alpha-Beta Pruning):", alpha_beta_pruning(root, 3, float('-inf'), float('inf'), True))
