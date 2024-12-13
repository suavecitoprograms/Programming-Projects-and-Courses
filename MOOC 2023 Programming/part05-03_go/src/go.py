# Write your solution here
def who_won(game_board: list):
    uno = 0
    dos = 0
    
    for row in game_board:
        for cell in row:
            if cell == 1:
                uno += 1
            elif cell == 2:
                dos += 1
    
    if uno > dos:
        return 1
    elif dos > uno:
        return 2
    return 0
