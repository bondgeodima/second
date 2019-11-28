class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population + 1000


def main():
    dnepr_city = City("Dnepr", 1000)
    return dnepr_city


if __name__ == "__main__":
    main()