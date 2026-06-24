def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        # Hard should be the widest, so we bumped it
        # from 1-50 to 1-200.
        return 1, 200
    return 1, 100


def parse_guess(raw: str, low: int, high: int):
    """
    Parse user input into an int guess and validate it against the
    difficulty's inclusive [low, high] range.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    # I spotted that negative and out-of-range guesses were being accepted.
    # Claude first proposed validating in app.py. I asked to move parse_guess
    # here and add the range check.
    if value < low or value > high:
        return False, None, f"Guess must be between {low} and {high}."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).


    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    # I reported the game saying "Go HIGHER!" when a
    # guess was already too high. We traced it together to the hint strings
    # being attached to the wrong branches, then moved this function here from
    # app.py and corrected them — too high -> go LOWER, too low -> go HIGHER.
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    # We reviewed the scoring together and found two issues I flagged:
    # an off-by-one in the Win formula (it used attempt_number + 1, so a
    # first-try win was underpaid) and a "Too High" branch that ADDED points
    # on even attempts. We dropped the +1 and made every wrong guess a flat -5.
    if outcome == "Win":
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
