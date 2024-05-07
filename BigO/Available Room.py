class Room:
    def __init__(self, a="", b="", c=""):
        self.room_id = a
        self.unit_price = b
        self.room_availability = c

    def __str__(self):
        s = f"{self.room_id} {self.unit_price}"
        return s


N = int(input())
rooms = []
for i in range(N):
    a, b, c = map(str, input().split())
    room = Room(a, b, c)
    rooms.append(room)

for room in rooms:
    if room.room_availability == "0":
        print(room)
