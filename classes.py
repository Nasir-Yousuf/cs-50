# self refarences the object that we currently dealing with
# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


# p = Point(2, 5)
# print(p.x)
# print(p.y)

class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passenger = []

    def add_passenger(self, name):
        if not self.open_seat():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passenger)


flight = Flight(3)

people = ['nasir', 'nasir1', 'nasir2', 'nasir3']

for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfully")
    else:
        print(f"No available seats for {person}")
