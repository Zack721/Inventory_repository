import Components.Bricks
import Components.Home
def main():
    red_bricks = Components.Bricks.Brick()
    bunch_of_bricks = Components.Bricks.BrickBatch(14000)
    user_house = Components.Home.House(bunch_of_bricks)
    total_price = bunch_of_bricks.CalcTotalPrice()
    if user_house.IsHouseBuilt() == True:
        print(f"The house is built and it cost {total_price}")
    #doesnt work dont know why"""

main()




#is a class helper with only one property which is public
#has one method that makes the batch
#should receive one argument that is an int saying the number of bricks they want also have a container that holds objects
#have a method that calcs the total value of all the bricks in the container

