cities = ['tacloban', 'manila', 'cebu']
print(cities[0])
print(cities[-1])

developer = 'elizah'
list(developer)

print(len(cities))
cities[1] = 'ormoc'
print(cities)

del cities[2]
print(cities)

print("tacloban" in cities)

developer = ['Alice', 25, ['Python', 'Java']]
print(developer[2][1])

developer = ['Elizah', 20, 'Java developer']
name, age, job = developer
print(age)

name, *rest = developer
print(rest)

desserts = ['cake', 'cookies', 'ice cream', 'pie', 'brownies']
print(desserts[1:4])



