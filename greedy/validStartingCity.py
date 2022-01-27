from tracemalloc import start


def validStartingCity(distances, fuel, mpg):
    # Test starting at index...
    for startingIdx in range(len(distances)):
        remainingMiles = 0
        citiesVisited = 0
        # Travel logic goes here
        for travelIdx in range(len(distances)):
            # Find correct index given above
            arrayIdx = (startingIdx + travelIdx) % len(distances)

            # Fill up the tank
            gallonsFromCurrentCity = fuel[arrayIdx]
            milesFromCurrentCity = gallonsFromCurrentCity * mpg
            remainingMiles += milesFromCurrentCity

            # Travel to next city
            distanceToNextCity = distances[arrayIdx]
            remainingMiles -= distanceToNextCity
            citiesVisited += 1

            # Check if ran out of gas
            if remainingMiles >= 0:
                continue 
            else:
                break

        if citiesVisited == len(distances) and remainingMiles >= 0:
            return startingIdx

        






if __name__ == '__main__':
    distances = [5, 25, 15, 10, 15]
    fuel = [1, 2, 1, 0, 3]
    mpg = 10
    print(validStartingCity(distances, fuel, mpg))
