import geopy.distance
import settings  # global variable


# h(n)
def get_distance_h(station1, station2):
    '''
    method to obtain the h(n) between 2 stations
    '''
    coord1 = get_coords(station1)
    coord2 = get_coords(station2)
    dis = geopy.distance.distance(coord1, coord2).km
    return dis

# g(n)


def get_distance_g(station1, station2):
    '''
    method to obtain the g(n) between 2 stations
    if nodes not connected -> -1

    '''

    neighbours = get_neighbours(station1)
    for key, value in neighbours.items():
        if key == station2:
            return value
    return -1


def get_distance_f(station1, station2):
    '''
    method to obtain the f(n) between 2 stations
       f = g + h
    '''

    g = get_distance_g(station1, station2)
    h = get_distance_h(station1, station2)
    return g + h


def get_coords(metro_station):
    '''
    method to obtain the coordinates of a station

    '''
    for station in settings.data["stations"]:
        if metro_station == station["name"]:
            return station["coords"]


def get_neighbours(metro_station):
    '''
    method to obtain the neighbours of a station

    '''
    neighbours = []

    for station in settings.data["stations"]:
        if station["name"] == metro_station:
            # for neighbour in station["connected_to"]:

            neighbours.append(station["connected_to"])

    return neighbours[0]
