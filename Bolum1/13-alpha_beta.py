def minimax_alpha_beta(position, depth, alpha, beta, maximize_player):
    # Base Case (Oyun bitti veya derinlik sınırı aşıldı)
    if depth == 0 or position.current_winner:
        return static_evaluation(position) # Basit skor döndür

    if maximize_player:
        max_eval = -math.inf
        for move in position.available_moves():
            position.make_move(move, 'X')
            eval = minimax_alpha_beta(position, depth-1, alpha, beta, False)
            position.undo_move(move) # Hamleyi geri al

            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval) # Alpha'yı güncelle

            # BUDAMA NOKTASI
            if beta <= alpha:
                break # Beta Cutoff
        return max_eval

    else:
        min_eval = math.inf
        for move in position.available_moves():
            position.make_move(move, 'O')
            eval = minimax_alpha_beta(position, depth-1, alpha, beta, True)
            position.undo_move(move)

            min_eval = min(min_eval, eval)
            beta = min(beta, eval) # Beta'yı güncelle

            # BUDAMA NOKTASI
            if beta <= alpha:
                break # Alpha Cutoff
        return min_eval
