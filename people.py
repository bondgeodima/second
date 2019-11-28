class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self, arg):
        speed = arg * 40
        return speed


def main():
    in_name = input_name()
    p1 = People(in_name[0], in_name[1])
    p1.speed = p1.run(10)
    print ('User {} age {} run speed {}'.format(p1.name, p1.age, p1.speed))


def input_name():
    name = input("Your name: ")
    age = input("Your age: ")
    return (name, age)


if __name__ == "__main__":
    main()
