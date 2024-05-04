def main():
    time = input('What time is it? ')
    meal_time = check_meal_time(time)
    if meal_time:
        print(meal_time)


def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60


def check_meal_time(time):
    t = convert(time)
    if 7 <= t <= 8:
        return 'breakfast time'
    elif 12 <= t <= 13:
        return 'lunch time'
    elif 18 <= t <= 19:
        return 'dinner time'
    else:
        return None


if __name__ == "__main__":
    main()

