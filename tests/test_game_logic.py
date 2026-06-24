from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


# --- Range validation (the bug we fixed) ---
# parse_guess used to accept any integer; negative and out-of-range
# values must now be rejected for the active difficulty range.

def test_parse_guess_rejects_negative():
    ok, value, err = parse_guess("-5", 1, 20)
    assert ok is False
    assert value is None
    assert err == "Guess must be between 1 and 20."


def test_parse_guess_rejects_above_range():
    # 25 is valid on Normal (1-100) but out of range on Easy (1-20).
    ok, value, err = parse_guess("25", 1, 20)
    assert ok is False
    assert value is None
    assert err == "Guess must be between 1 and 20."


def test_parse_guess_accepts_in_range():
    ok, value, err = parse_guess("15", 1, 20)
    assert ok is True
    assert value == 15
    assert err is None


def test_parse_guess_accepts_range_boundaries():
    # Range is inclusive on both ends.
    assert parse_guess("1", 1, 20) == (True, 1, None)
    assert parse_guess("20", 1, 20) == (True, 20, None)


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high_says_go_lower():
    # The bug we fixed: a guess ABOVE the secret used to say "Go HIGHER!".
    # It must report "Too High" and tell the player to go LOWER.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message


def test_guess_too_low_says_go_higher():
    # The mirror case: a guess BELOW the secret must say "Go HIGHER!".
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "LOWER" not in message


# --- Bug 1: secret was stringified on even attempts ---
# When the secret became a str, check_guess fell back to a LEXICAL compare,
# so 9 vs 50 compared "9" > "50" and wrongly reported "Too High". The fix
# keeps the secret an int, so the comparison is always numeric.

def test_comparison_is_numeric_not_lexical():
    # Numerically 9 < 50 -> "Too Low" (lexically "9" > "50" would be "Too High").
    outcome, _ = check_guess(9, 50)
    assert outcome == "Too Low"


def test_comparison_is_numeric_not_lexical_high():
    # Numerically 100 > 90 -> "Too High" (lexically "100" < "90").
    outcome, _ = check_guess(100, 90)
    assert outcome == "Too High"


# --- Bug 2: update_score scoring inconsistencies ---
# The Win formula had an off-by-one: winning on attempt 1 now gives 90.

def test_win_score_no_off_by_one():
    assert update_score(0, "Win", 1) == 90


def test_win_score_is_floored_at_10():
    assert update_score(0, "Win", 99) == 10


# Wrong guesses apply a consistent -5, regardless of attempt parity.
# "Too High" previously gave +5 on even attempts.

def test_too_high_penalty_consistent_regardless_of_parity():
    assert update_score(50, "Too High", 2) == 45  # even attempt
    assert update_score(50, "Too High", 3) == 45  # odd attempt


def test_too_low_penalty_consistent_regardless_of_parity():
    assert update_score(50, "Too Low", 2) == 45
    assert update_score(50, "Too Low", 3) == 45


# --- Bug 3: Hard range was smaller than Normal ---
# Hard must be a WIDER range than Normal, not narrower.

def test_hard_range_wider_than_normal():
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high


def test_difficulty_ranges():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 200)
