from src.segment import Segment

digit_dict = {
    '0': [0, 1, 2, 4, 5, 6],
    '1': [2, 5],
    '2': [0, 2, 3, 4, 6],
    '3': [0, 2, 3, 5, 6],
    '4': [1, 2, 3, 5],
    '5': [0, 1, 3, 5, 6],
    '6': [0, 1, 3, 4, 5, 6],
    '7': [0, 2, 5],
    '8': [0, 1, 2, 3, 4, 5, 6],
    '9': [0, 1, 2, 3, 5, 6],
    "c": []
}

top_segment = Segment(id=0,
                      top_left_position=(1, 0),
                      bottom_right_position=(3, 0))
top_left_segment = Segment(id=1,
                           top_left_position=(0, 1),
                           bottom_right_position=(0, 2))
top_right_segment = Segment(id=2,
                            top_left_position=(4, 1),
                            bottom_right_position=(4, 2))
middle_segment = Segment(id=3,
                         top_left_position=(1, 3),
                         bottom_right_position=(3, 3))
bottom_left_segment = Segment(id=4,
                              top_left_position=(0, 4),
                              bottom_right_position=(0, 5))
bottom_right_segment = Segment(id=5,
                               top_left_position=(4, 4),
                               bottom_right_position=(4, 5))
bottom_segment = Segment(id=6,
                         top_left_position=(1, 6),
                         bottom_right_position=(3, 6))
segments = {
    segment.id: segment
    for segment in [
        top_segment, top_left_segment, middle_segment, top_right_segment,
        bottom_left_segment, bottom_right_segment, bottom_segment
    ]
}


class Display:

  def __init__(self, dimension: tuple) -> None:
    self.pixel_map = []
    self.dimension = dimension
    self.current_digit_offset = 0
    self.generate_pixel_map()

  def generate_pixel_map(self) -> None:
    for row in range(self.dimension[0] + 1):
      self.pixel_map.append([])
      for pixel in range(self.dimension[1] + 1):
        self.pixel_map[-1].append(" ")


  def add_segment(self, segment: Segment, offset: int) -> None:
    width_range = range(segment.top_left_position[0] + offset, segment.bottom_right_position[0] + offset + 1)
    height_range = range(segment.top_left_position[1], segment.bottom_right_position[1] + 1)
    for row_idx in height_range:
      for pixel_idx in width_range:
        self.pixel_map[row_idx][pixel_idx] = "#"

  def add_digit(self, digit: str) -> None:
    for segment_id in digit_dict[digit]:
      self.add_segment(segments[segment_id], self.current_digit_offset)
    self.current_digit_offset += 9

  def set_digit(self, digit: str, offset: int) -> None:
      # todo make overwritting cleaner
      for row in self.pixel_map:
        for pixel_idx in range(offset, 7):
          row[pixel_idx] = " "

      for segment_id in digit_dict[digit]:
        self.add_segment(segments[segment_id], offset)

  def delete_digit(self, offset: int) -> None:
    for segment in segments.values():
      width_range = range(segment.top_left_position[0] + offset, segment.bottom_right_position[0] + offset + 1)
      height_range = range(segment.top_left_position[1], segment.bottom_right_position[1] + 1)
      for row_idx in height_range:
        for pixel_idx in width_range:
          self.pixel_map[row_idx][pixel_idx] = " "

  def prettify_pixel_map(self) -> str:
    s = ""
    for row in self.pixel_map:
      if all(element == ' ' for element in row):
        continue
      s += "".join(row) + "\n"
    return s

  def __str__(self) -> str:
    return self.prettify_pixel_map()
