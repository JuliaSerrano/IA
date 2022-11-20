import geopy.distance
import settings  # global variable


# h(n)
def get_distance(station1, station2):
    '''
    method to obtain the distance between 2 coordinates
    '''
    coord1 = get_coords(station1)
    coord2 = get_coords(station2)
    dis = geopy.distance.distance(coord1, coord2).km
    return dis


def get_coords(metro_station):
    for station in settings.data["stations"]:
        if metro_station == station["name"]:
            return station["coords"]


def get_neighbours(metro_station):
    neighbours = []

    for station in settings.data["stations"]:
        if station["name"] == metro_station:
            for neighbour in station["connected_to"]:
                neighbours.append(neighbour)

    return neighbours
