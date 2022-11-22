from datos import get_neighbours, get_coords, get_distance_g
import settings
from Algorithm import a_star_algorithm


if __name__ == "__main__":
    settings.init()
    # print(get_neighbours("Victoria"))
    # print(get_distance_g("Victoria", "Kato Patissia"))
    print(a_star_algorithm("Perissos", "Eleonas"))
