"""
# bowling_score
This is bowling score calculating function

Bowling rules:
- Each `game` has 10 frames.
- Each `frame` gives you 2 rolls to knock down 10 pins.
- Each `pin` worth 1 point.
- Knocking down all 10 pins in one `roll` called `strike`: gives adds points: 10 + points of next 2 rolls
- Knocking down all 10 pins in one `frame` (2 rolls) called `spare`: gives adds point: 10 + point of the next roll
- 10th `frame` can have 3 rolls, when you hit `strike` or `spare` in first 2 rolls.
- Min score: 0
- Max Score: 300
"""


def validate_frame(frame: list[int], index: int) -> None:
    len_limit = 2

    if index == 9:
        len_limit = 3

    if not isinstance(frame, list) or len(frame) > len_limit:
        raise ValueError(f"frame: must be list with {len_limit} elements at most")

    frame_len = len(frame)

    if frame_len == 0:
        raise ValueError("frame: cannot be empty")

    if any(roll < 0 or roll > 10 for roll in frame):
        raise ValueError("frame: each roll must be between 0 and 10")

    if index < 9:
        if frame_len >= 2 and frame[0] != 10 and sum(frame[:2]) > 10:
            raise ValueError("frame: sum of first 2 rolls cannot exceed 10")
    else:
        if frame_len >= 2 and frame[0] != 10 and frame[0] + frame[1] > 10:
            if frame_len == 2:
                raise ValueError("frame: incomplete 10th frame with spare")
        if frame_len == 3:
            if frame[0] == 10 or frame[0] + frame[1] == 10:
                if frame[2] > 10:
                    raise ValueError("frame: bonus roll cannot exceed 10")
            else:
                raise ValueError(
                    "frame: 10th frame needs strike or spare to have 3 rolls"
                )


def validate_game(game: list[list[int]]) -> None:
    if not isinstance(game, list) or len(game) > 10:
        raise ValueError("game: must be list with 10 elements at most")


def bowling_score(game: list[list[int]]) -> int:
    """Bowling Score Calculating function

    Calculates score for a bowling game.

    Args:
        game: list of frames
    Return:
        score: 0 <= int <= 300

    """
    validate_game(game)
    score = 0
    stack = []
    for i, frame in enumerate(game):
        validate_frame(frame, i)
        for roll in frame:
            roll_score = roll * (1 + len(stack))
            score += roll_score
            stack = [count - 1 for count in stack if count > 1]

        if i < 9:
            if len(frame) == 1:  # Strike
                stack.append(2)
            elif sum(frame) == 10:  # Spare
                stack.append(1)

    return score
