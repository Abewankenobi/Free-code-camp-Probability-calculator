# Importing required methods
import random
import copy
# Creating the class method
class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        # Appending the keys into the content list
        for key,value in kwargs.items():
            self.contents.extend([key]*value)
    def draw(self,num): # num-->number of balls to draw from the hat
        result_lst = []
        if num > len(self.contents):
            return self.contents
        else:
            for probable in range(num):
                result = random.choice(self.contents)
                result_lst.append(result)
                self.contents.remove(result)
            return result_lst
# Creating experiment function
def experiment(hat,expected_balls,num_balls_drawn,num_experiments):
    m = 0 # For successes count
    for i in range(num_experiments):
        answer = dict()
        constant = 0 # To determine if all the keysvalue are from answer > keyvalues of expected_balls
        our_hat = copy.deepcopy(hat) # Copying values drawn from the hat
        ball_drawn = our_hat.draw(num_balls_drawn) # Balls drawn at random
        for i in ball_drawn:
            if i not in answer:
                answer[i] = 1
            else:
                answer[i] += 1
        for i,j in expected_balls.items():
            answer[i] = answer.get(i,0)
            if answer[i] >= j:
                constant += (1/len(expected_balls))
        if constant == 1:
            m += 1
        return (m/num_experiments)
hat = Hat(blue=4,red=2,green=6)
print(experiment(hat=hat, expected_balls={"blue":2,"red":1},num_balls_drawn=4,num_experiments=2000))
