import math

def distance(city1, city2):
    # Euclidean distance between two cities
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def nearest_neighbor_tsp(cities):
    num_cities = len(cities)
    visited = [False] * num_cities
    tour = [0]  # Start from the first city

    for _ in range(num_cities - 1):
        current_city = tour[-1]
        min_distance = float('inf')
        nearest_city = None

        for next_city in range(num_cities):
            if not visited[next_city] and next_city != current_city:
                d = distance(cities[current_city], cities[next_city])
                if d < min_distance:
                    min_distance = d
                    nearest_city = next_city

        tour.append(nearest_city)
        visited[nearest_city] = True

    # Return to the starting city to complete the tour
    tour.append(tour[0])

    return tour

if __name__ == "__main__":
    # Example usage:
    cities = [(0, 0), (1, 2), (2, 4), (3, 1), (4, 3)]
    tsp_tour = nearest_neighbor_tsp(cities)

    print("Traveling Salesman Tour:", tsp_tour)
