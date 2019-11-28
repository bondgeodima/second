class Room:
    def __init__(self, number, size):
        self.number = number
        self.size = size

    def out(self, arg):
<<<<<<< HEAD
        s = self.arg * 50
=======
        s = self.arg
>>>>>>> first
        return s


def main():
    r1 = Room(10, 400)
<<<<<<< HEAD
    return r1
=======
    print(r1)
>>>>>>> first


if __name__ == "__main__":
    main()