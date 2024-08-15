class Segment:

    def __init__(self, id: int, top_left_position: tuple,
                 bottom_right_position: tuple) -> None:
        self.id = id
        self.top_left_position = top_left_position
        self.bottom_right_position = bottom_right_position

    def __str__(self) -> str:
        return f"Segment {self.id=}, {self.top_left_position=}, {self.bottom_right_position=}"
