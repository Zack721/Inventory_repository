#This class must have one data member: id_ which is a string         
class Builder:
    def __init__(bd, id):#Done
        if type(id) == str:
            bd.__id_ = id
           
    def GetID(bd):
        return bd.__id_

    def Build(bd, brick_batch):
        if brick_batch.amount_ >= House().BRICKS_NEEDED_:
            print("Building house...")
            return House()
        else:
            print("Not enough bricks")

        #will take some bricks from the inventory
        #To Josias, the instructions here arent clear, how many bricks exactly do u want here
        for i in range(0, House.BRICKS_NEEDED_):
            Inventory.__bricks_bought_.pop(i)






