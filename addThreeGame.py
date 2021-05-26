# Rodrigue Andela
# 05/24/2021
# in this task I write a class that allow two player to play


# write the class
class AddThreeGame:

    __state = ''
    __track = 0
    __moves = []
    # initialize the files
    def __init__(self,):
        self.__state = "UNFINISHED"
        self.__track = 0
        self.__moves = []
    # return the current state

    def get_current_state(self):
        return self.__state
    # when a player make a move

    def make_move(self, player, game):
         if self.__state == "UNFINISHED":
             if game in [x for x in range(0,10)]:
                 if game not in self.__moves:
                     self.__track += game
                     self.__moves.append(game)
                     if self.__track == 15:
                         if player == "first":
                             self.__state = "FIRST_WON"
                         elif player == "second":
                             self.__state = "SECOND_WON"
                         return True
                     self.__moves.sort()
                     if self.__moves == [x for x in range(0,10)]:
                         self.__state = "DRAW"
                         return True
         return False









