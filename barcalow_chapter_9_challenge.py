"""
A non-spare roll gets you the number of pins knocked down.

A spare gets you 10 points, plus the FIRST roll in the next frame.

A strike gets you 10 points, plus the score of the ENTIRE next frame.

10th frame: if you get a strike or a spare, you get to roll a third time.
"""
class ScoreError(ValueError):
    pass


class Frame:
    """Represent one frame of a bowling game."""

    def __init__(self, first: int, second = 0):
        """
        Initialize the first and second rolls of the frame.

        :param first: Number of pins knocked down in the first frame.
        :param second: Number of pins knocked down in the second frame.
        """
        self.first = first
        self.second = second
        self.score = 0

    def __str__(self):
        """
        Print out the neatly formatted frame.

        :return: Prints boxes with strike and spare marks or rolls.
        """
        if self.first == 0:
            first_char = "-"
        elif self.first == 10:
            first_char = "X"
        else:
            first_char = str(self.first)

        if self.second == 0:
            second_char = "-"
        elif self.first + self.second == 10:
            second_char = "/"
        else:
            second_char = str(self.second)

        return f"[{first_char}:{second_char}]={self.score}"

    def __repr__(self):
        """
        Return the call needed to instantiate an identical instance.

        :return: Returns the necessary call to create a new Frame with the
            same scores.
        """
        return f"Frame({repr(self.first)}, {repr(self.second)})"


class TenFrame(Frame):
    """Represents the tenth frame of a game of bowling."""

    def __init__(self, first: int, second = 0, third = 0):
        """
        Initialize the first, second, and third rolls of the frame.

        :param first: Number of pins knocked down in the first roll.
        :param second: Number of pins knocked down in the second roll.
        :param third: Number of pins knocked down in the third roll (only on
            the tenth frame).
        """
        super().__init__(first, second)
        self.third = third

    def __str__(self):
        """
        Print out the neatly formatted frame.

        :return: Prints boxes with strike and spare marks or rolls.
        """
        if self.first == 0:
            first_char = "-"
        elif self.first == 10:
            first_char = "X"
        else:
            first_char = str(self.first)

        if self.second == 0:
            second_char = "-"
        elif self.second == 10 and self.first == 10:
            second_char = "X"
        elif self.first + self.second == 10:
            second_char = "/"
        else:
            second_char = str(self.second)

        if self.third == 0:
            third_char = "-"
        elif self.third == 10 and self.second == 10:
            third_char = "X"
        else:
            third_char = str(self.third)

        return f"[{first_char}:{second_char}:{third_char}]={self.score}"

    def __repr__(self):
        """
        Return the call needed to instantiate an identical instance.

        :return: Returns the necessary call to create a new Frame with the
            same scores.
        """
        return (f"TenFrame({repr(self.first)}, {repr(self.second)}, "
                f"{repr(self.third)})")


class BowlingGame:
    """Create a game of bowling."""
    def __init__(self, frames: list):
        """
        Initialize the list of frames.

        :param frames: Frames in the game.
        """
        self.frames = frames
        self.total = 0

    def __str__(self):
        """
        Print out each frame, neatly formatted.

        :return: Prints each frame and its score.
        """
        returning = ""
        self.total = 0

        for frame in self.frames:
            self.total += frame.score
            returning += str(frame)
            if self.frames.index(frame) < 9:
                returning += f"; {self.total} | "
            else:
                returning += f"; {self.total}"

        return returning

    def __repr__(self):
        """
        Return the call needed to instantiate an identical instance.

        :return: Returns the necessary call to create a new BowlingGame with
            the same scores.
        """
        return f"BowlingGame({self.frames})"

    def score(self):
        """
        Score each frame. Bowling scoring is stupid.

        :return: If the added rolls equal less than 10, return the added
            rolls; if the added rolls equal 10, return 10 plus the next
            frame's first roll; if the first roll equals 10, return 10 plus
            the next frame's score.
        """
        for i in range(len(self.frames)):
            # Work backwards through the list.
            frame = self.frames[-i-1]

            # If the frame is the first one, then set the next frame to empty.
            if i > 1:
                next_frame = self.frames[-i]
                third_frame = self.frames[-i+1]
            elif i > 0:
                next_frame = self.frames[-i].first
                third_frame = self.frames[-i].second
            else:
                next_frame = Frame(0, 0)
                third_frame = Frame(0, 0)

            # If the frame is not the first (tenth) or second (ninth), then
            # score the frame based on the next.
            if i > 1:
                if frame.first == 10:
                    if next_frame.first == 10 and third_frame.first == 10:
                        frame.score = 30
                    elif next_frame.first == 10:
                        frame.score = 20 + third_frame.first
                    else:
                        frame.score = (10 + next_frame.first
                                          + next_frame.second)
                elif frame.first + frame.second == 10:
                    frame.score = 10 + next_frame.first
                elif frame.first + frame.second < 10:
                    frame.score = frame.first + frame.second
                else:
                    raise ScoreError("Rolls must add up to 10 or less")

            # If the frame is the ninth, score it uniquely.
            elif i == 1:
                if frame.first == 10:
                    if next_frame == 10 and third_frame == 10:
                        frame.score = 30
                    elif next_frame == 10:
                        frame.score = 20 + third_frame
                    else:
                        frame.score = 10 + next_frame
                elif frame.first + frame.second == 10:
                    frame.score = 10 + next_frame
                elif frame.first + frame.second < 10:
                    frame.score = frame.first + frame.second
                else:
                    raise ScoreError("Rolls must add up to 10 or less")

            # If the frame is the tenth, score it extra uniquely.
            elif i == 0:
                if frame.first == 10 or frame.first + frame.second == 10:
                    frame.score = frame.first + frame.second + frame.third
                else:
                    frame.score = frame.first + frame.second
            else:
                raise IndexError("this error should never be seen")

            self.total += frame.score


def create_frames():
    """
    Create 10 frames for 10-pin bowling.

    :return: Returns a list of frames.
    """
    frames = []
    for i in range(10):
        try:
            roll_1 = int(input(f"Enter the first roll (frame {i+1}): "))
        except (ValueError, TypeError):
            print("Error in input. Defaulting to 0")
            roll_1 = 0

        try:
            roll_2 = int(input(f"Enter the second roll (frame {i+1}): "))
        except (ValueError, TypeError):
            print("Error in input. Defaulting to 0")
            roll_2 = 0

        if i == 9:
            try:
                roll_3 = int(input(f"Enter the third roll (frame {i+1}): "))
            except (ValueError, TypeError):
                print("Error in input. Defaulting to 0")
                roll_3 = 0
        else:
            # This is to prevent editor warnings :P
            roll_3 = None

        if roll_3:
            new_frame = TenFrame(roll_1, roll_2, roll_3)
        else:
            new_frame = Frame(roll_1, roll_2)

        frames.append(new_frame)
        print()
    return frames


# Feel free to paste a list of frames in here.
frame_list = []

if not frame_list:
    frame_list = create_frames()

game = BowlingGame(frame_list)

game.score()
print(game)