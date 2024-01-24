year = input("Ingrese un año entre 1900 y 2199 ")
year = int(year)
year_count = 0
while year >= 1900 and year <= 2199:
  if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
      year -= 1
      continue
    year_count += 1
  year -= 1

print(year_count)