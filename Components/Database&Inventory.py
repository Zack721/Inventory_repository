"""class Database:
    def __init__(DB):
        
        DB.__builders_ = []  
        DB.__builderID_to_index_ = {}

    def AddBuilder(DB, builder):
        builder_index =  DB.__builderID_to_index_.get(builder.GetID())
        if builder_index == None:
            DB.__builders_.append(builder)
            DB.__builderID_to_index_[builder.GetID()] = len(DB.__builders_) -1
                   
        else:
            print("The ID is already associated with a different builder.")


    def GetBuilderByID(DB, ID):
        list_of_indexes = DB.__builderID_to_index_.get(ID) #when calling this method make sure to put that the argument ID is equal to builder.GetID() 
        if list_of_indexes == None:
            return None
        else:
            return DB.__builders_[list_of_indexes]  



class Inventory:
    #This class should have at least 3 data members: money_ (int), bricks_bought_ (container of Bricks objects), 
    #and authorized_personnel_ (container of Builder objects)
    def __init__(inv, money):#Done
        inv.__money_ = money
        inv.__bricks_bought_ = []



    #Make one private methods: IsAuthorizedPersonnel(id) - return bool

    def __IsAuthorizedPersonnel_(inv, construction_worker):#Done
        id = construction_worker.GetID()
        if id in inv.authorized_personnel_: #Josias, im not sure I should be calling id like this or if i should do it like builder.__id_
            return True
        else:
            return False

        
    
    #def GetBudget(inv):

    def BuyBricks(inv, bunch_of_bricks):
        total = bunch_of_bricks.CalcTotalPrice()
        if inv.__money_ >= total:
            inv.__money_-= total
        else:
            print(f"You dont have enough money come back when u do, you need an extra {total - inv.__money_}")

    #This method takes one argument typed Builder, if the builder is registred as authorized personnel,
    #so assign the necessary bricks to make a house, if you do not have enought bricks, inside the method buy the rest of bricks,
    #but if there is not necessary money, so print as much as you can, and then print a message error telling that there are not enough resources
    def AssignBricks(inv, builder):#To Josias,conflicting requirements with some other parts 
        if inv.__IsAuthorizedPersonnel_() == True:
            if len(inv.__bricks_bought_) <= House.BRICKS_NEEDED_:
                if Brick().VALUE_* (House.BRICKS_NEEDED_ - len(Inventory().__bricks_bought_)) >= #Dont know what to do """