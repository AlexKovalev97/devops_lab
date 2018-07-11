def is_leap(year):
    leap = False
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        if (year >= 1900) and (year <= 10 ** 5):
            leap = True
    return leap


year = int(input())
print(is_leap(year))
