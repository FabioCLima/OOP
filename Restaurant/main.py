from src.restaurant import Restaurant


def main():
    arc = Restaurant("Arc", "Meditarrenea", True)
    nau = Restaurant("Nau", "Seafood")
    skyresto = Restaurant("SkyResto", "Contemporanea", True)

    restaurants = [arc, nau, skyresto]
    for restaurant in restaurants:
        restaurant.describe_restaurant()


if __name__ == "__main__":
    main()
