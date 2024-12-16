def HasEnoughBricks(brick_batch, bricks_needed):
    if brick_batch.amount_ < bricks_needed:
        return False
    else:
        return True
    
if __name__== "__main__":
    class Brick:
        def __init__(obj):
            obj.VALUE_ = 5

    class BrickBatch:
        def __init__(br, amount):
            br.bricks_= []
            br.amount_ = amount
            br.__BatchMaker()
        
        def __BatchMaker(br):
            for i in range(0, br.amount_):
                br.bricks_.append(Brick())
            
        def CalcTotalPrice(br):
            return br.amount_ * Brick().VALUE_
   
    assert HasEnoughBricks(BrickBatch(500), 600) == False
    assert HasEnoughBricks(BrickBatch(500), 100) == True
    assert HasEnoughBricks(BrickBatch(500), 500) == True
    assert HasEnoughBricks(BrickBatch(0), 0) == True
    assert HasEnoughBricks(BrickBatch(0), 200) == False



