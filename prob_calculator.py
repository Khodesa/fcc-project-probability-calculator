import copy
import random
# Consider using the modules imported above.

class Hat():
  def __init__(self, **balls):
    contents = []
    for key, value in balls.items():
      for i in range(value):
        contents.append(key)
    self.contents = contents
    self.holder = copy.copy(self.contents)

  def draw(self, num):
    self.contents = copy.copy(self.holder)
    draw = copy.copy(self.contents)
    return_list = []
    for x in range(num):
      choice = random.choice(self.contents)
      self.contents.remove(choice)
      return_list.append(choice)
      if len(self.contents) == 0:
        self.contents = copy.copy(draw)
    return return_list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0
  for experiment in range(num_experiments):
    balls_drawn = hat.draw(num_balls_drawn)
    balls_dict = {}
    for color in balls_drawn:
      if color in balls_dict:
        balls_dict[color] += 1
      else:
        balls_dict[color] = 1
    m = 0
    for key, value in expected_balls.items():
      if key in balls_dict:
        if balls_dict[key] >= value:
          m += 1
    if m == len(expected_balls):
      M += 1
  return M / num_experiments
