# Modify the room class to calculate area by using constructors and destructors.
class Room:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width
    
    def __del__(self):
        print(f"The room with length {self.length} and width {self.width} is destroyed")

my_room = Room(10,8)
area = my_room.calculate_area()
print(f"The area of the room is {area}")