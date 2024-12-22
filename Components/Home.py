import UtilitiesFolder.Utilities as utilities
class House:
    #The constructor receives a batch of bricks, if the amount is enough should print "A house was built", otherwise print a error message
    def __init__(hs,bricks_needed, brick_batch): #brick_batch is object of the class BrickBatch
        hs.__bricks_needed_ = bricks_needed
        hs.__is_built_ = utilities.HasEnoughBricks(brick_batch, hs.__bricks_needed_)
    
    def GetBricksNeeded(hs):
        pass
    
    
    def IsBuilt(hs):
        return hs.__is_built_
        #true if have enough bricks false if not enough
    
class Apartment(House):
    def __init__(hs, brick_batch):
        super.__init__(1000, brick_batch)

class Mansion(House):
    def __init__(hs, brick_batch):
        super.__init__(3000, brick_batch)
    

class Castle(House):
    def __init__(hs, brick_batch):
        super().__init__(2500, brick_batch)


if __name__ == "__main__":
    import Bricks
    our_house = House(Bricks.BrickBatch(510))
    assert our_house.IsBuilt() == True
    our_house_2 = House(Bricks.BrickBatch(480))
    assert our_house_2.IsBuilt() == False

    our_house_3 = House(Bricks.BrickBatch(0))
    assert our_house_3.IsBuilt() == False

    our_house_4 = House(Bricks.BrickBatch(500))
    assert our_house_4.IsBuilt() == True

    """def MakeHouse(brick_batch):
    the_house = House(brick_batch)
    if the_house.IsHouseBuilt() == True:
        return the_house
    return False"""


