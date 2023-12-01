import copy
import random

class Hat:
  '''take variable # of arguments that specify number balls of each color'''
  def __init__(self,**balls):
    '''arguments passed converted to contents list of str one item for each ball'''
    self.contents = []
    #loop through key, value in argument with items function
    for color, qty in balls.items():
      #append to contents list with extend function
      self.contents.extend([color] * qty)
  '''draw method accepts argument indicating the number of balls to draw from the hat'''
  def draw(self,num_balls):
    '''remove balls random-without replacement from contents,return balls as list str'''
    #random.sample(population, k) population=list to be sampled, k=elements to sample
    drawn_balls = random.sample(self.contents, min(num_balls, len(self.contents)))
    #loop through drawn balls list
    for ball in drawn_balls:
      #use remove function from contents
      self.contents.remove(ball)
    return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  '''The experiment function should return a probability.'''
  '''perform N experiments,count how many times M and estimate the probability as M/N'''
  # loop through range of passed # of experiments to perform
  success = 0 #successful experiments variable init at 0 and added to in loop
  for _ in range(num_experiments): #loop in range of passed # of time to run experiment
    #use copy.deepcopy function to ensure experiment has same starting point each time
    hat_copy = copy.deepcopy(hat)
    #use draw method to draw # balls passed
    drawn_balls = hat_copy.draw(num_balls_drawn)
    #assign drawn balls back to dictionary to compare to passed dictionary
    drawn_balls_count = {color: drawn_balls.count(color) for color in expected_balls}
    # use all function tor return True for successful matches
    if all(drawn_balls_count.get(color, 0) >= count for color, count
           in expected_balls.items()):
      success += 1 #increment succesful experiments
  '''estimate the probability as M/N'''
  probability = success / num_experiments
  return probability
  
