class School:
    def __init__(self, number, type):
        self.number = number
        self.type = type


def main():
    school = School(10, "medium")
    # return school
    print (school.number)


if __name__ == "__main__":
    main()
