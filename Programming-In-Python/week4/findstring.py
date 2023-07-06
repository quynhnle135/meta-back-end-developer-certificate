def ispresent(person):
    names = ["Al", "Bp", "Chi", "Ma"]
    if person in names:
        return True
    else:
        return False


def nodigit(person):
    if person.isalpha():
        return True
    else:
        return False
