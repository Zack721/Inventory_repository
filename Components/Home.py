import UtilitiesFolder.Utilities as utilities
class House:
    #The constructor receives a batch of bricks, if the amount is enough should print "A house was built", otherwise print a error message
    def __init__(hs, brick_batch): #brick_batch is object of the class BrickBatch
        hs.BRICKS_NEEDED_ = 500
        hs.__is_built_ = utilities.HasEnoughBricks(brick_batch, hs.BRICKS_NEEDED_)
    
    def IsHouseBuilt(hs):
        return hs.__is_built_
    

if __name__ == "__main__":
    import Bricks
    our_house = House(Bricks.BrickBatch(510))
    assert our_house.IsHouseBuilt() == True
    our_house_2 = House(Bricks.BrickBatch(480))
    assert our_house_2.IsHouseBuilt() == False

    our_house_3 = House(Bricks.BrickBatch(0))
    assert our_house_3.IsHouseBuilt() == False

    our_house_4 = House(Bricks.BrickBatch(500))
    assert our_house_4.IsHouseBuilt() == True

    """def MakeHouse(brick_batch):
    the_house = House(brick_batch)
    if the_house.IsHouseBuilt() == True:
        return the_house
    return False"""


