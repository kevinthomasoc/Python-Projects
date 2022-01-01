import math
def find_next_square(sq):
    if isinstance(math.sqrt(sq), int) == False:
        return -1
    else:
        for i in sq + 1:
            if isinstance(math.sqrt(sq), int) == True:
                return sq
            else:
                sq = sq
    

print(find_next_square(4))
