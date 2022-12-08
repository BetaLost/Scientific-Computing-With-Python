import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        
        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(key)
                
    def draw(self, number_of_times):
        number_of_times = min(number_of_times, len(self.contents))
        drawn = []
        for _ in range(number_of_times):
            ball_drawn = self.contents.pop(random.randrange(len(self.contents)))
            drawn.append(ball_drawn)
            
        return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    required = []
    
    for key, value in expected_balls.items():
            for _ in range(value):
                required.append(key)
    
    required.sort()
    
    for _ in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        balls_drawn = new_hat.draw(num_balls_drawn)
        
        if not set(required).issubset(set(balls_drawn)):
        #if set(required) >= set(balls_drawn):
            success += 1

    return success / num_experiments

obj = Hat(yellow=5,red=1,green=3,blue=9,test=1)
print(experiment(obj, {"yellow":2,"blue":3,"test":1}, 4, 1000))
