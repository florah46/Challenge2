from datetime import date


def compute_age(year_of_birth):
    year = date.today().year
    x = (year - year_of_birth)

    if x < 18:
        return "Minor"

    elif( x >= 18 and x <= 36):
        return "Youth"

    else:
        return 'Elder'


if __name__ == '__main__':
    year_of_birth = int(input("Enter Year of Birth"))
    print(compute_age(year_of_birth))         
   