
def show_location(lat, lon):
    print(f"lat is {lat} lon is {lon}")

show_location(5, 10)
show_location(8, 99)

place = 3, 16
show_location(*place)

places = [
    (3, 16), (9, 4), (6, 6), (7, 10)
]
for place in places:
    show_location(*place)

