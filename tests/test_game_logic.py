from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_score_win_first_attempt():
    # attempts starts at 0, incremented to 1 before update_score is called
    # points = 100 - 10*(1+1) = 80
    result = update_score(0, "Win", 1)
    assert result == 80

def test_score_win_later_attempt():
    # Win on 5th guess: attempts=5, points = 100 - 10*(5+1) = 40
    result = update_score(0, "Win", 5)
    assert result == 40

def test_score_win_minimum_points():
    # Win on attempt 9: points = 100 - 10*10 = 0, but minimum is 10
    result = update_score(0, "Win", 9)
    assert result == 10

def test_score_too_high_deducts_points():
    # Too High deducts 5 points
    result = update_score(100, "Too High", 0)
    assert result == 95

def test_score_too_low_deducts_points():
    # Too Low deducts 5 points
    result = update_score(100, "Too Low", 0)
    assert result == 95
