class House:
    #The constructor receives a batch of bricks, if the amount is enough should print "A house was built", otherwise print a error message
    def __init__(hs, brick_batch): #brick_batch is object of the class BrickBatch
        hs.BRICKS_NEEDED_ = 500
        hs.__is_built_ = hs.__CanBuildHouse(brick_batch)

    def __CanBuildHouse(hs, brick_batch):
        if brick_batch.amount_ < hs.BRICKS_NEEDED_:
            return False
        else:
            return True
        
    def IsHouseBuilt(hs):
        return hs.__is_built_