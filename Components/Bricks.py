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
