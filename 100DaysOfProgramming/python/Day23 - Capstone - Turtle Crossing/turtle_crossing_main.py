from random import randint


from modules.screen.Screen import PlayArea
from modules.player.Player import Player
from modules.scoreboard.Scoreboard import Scoreboard
from modules.cars.Cars import Cars


def main():
    #creates the screen
    screen = PlayArea()
    #Create player object
    player = Player()
    # player.create_player()
    print(player.position())


    #Create Scoreboard
    # screen.update()
    # car = Cars()
    
    #Variables
    car_objects = []
    playing = True
    # while playing:
    
    for i in range(0, 20):        
        car = Cars(str(i))
        car_objects.append(car)

    while playing:
        
        car = car_objects[randint(0,len(car_objects)-1)]
        car.move_car()
        if car != None:
        # print(f"car.cars {car.cars}")
            car.move_car()
        

    screen.click_exit()



if __name__ == "__main__":
    main()