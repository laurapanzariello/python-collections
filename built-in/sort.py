# simple list

years = [1989, 2000, 1967, 2020, 2008]
print(years)
print("index - year")
for index, year in enumerate(years):
    print(index, "-", year)

print(years)
print("sorted")
for year in sorted(years):
    print(year)

print(years)
print("sorted - reverse True")
for year in sorted(years, reverse=True):
    print(year)

print(years)
print("reversed")
for year in reversed(years):
    print(year)

print(years)
print("Sorted type: ", type(sorted(years)))
print("Reversed type: ", type(reversed(years)))

print(years.sort())
print(years)
