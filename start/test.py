class Room:
    def __init__(self, number, size):
        self.number = number
        self.size = size

    def out(self, arg):
        self.arg = arg
        s = self.arg * 50
        return s


def main():
    r1 = Room(10, 400)
    w = r1.out(10)
    print (w)
    # return w


if __name__ == "__main__":
    main()
