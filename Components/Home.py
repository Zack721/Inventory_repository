from Components.Utilities import HasEnoughBricks
class House:
    #The constructor receives a batch of bricks, if the amount is enough should print "A house was built", otherwise print a error message
    def __init__(hs, brick_batch): #brick_batch is object of the class BrickBatch
        hs.BRICKS_NEEDED_ = 500
        hs.__is_built_ = HasEnoughBricks(brick_batch, hs.BRICKS_NEEDED_)
    
    def IsHouseBuilt(hs):
        return hs.__is_built_
    
def MakeHouse(brick_batch, user_house):
    the_house = House(brick_batch)
    if the_house.IsHouseBuilt() == True:
        return the_house
    return False