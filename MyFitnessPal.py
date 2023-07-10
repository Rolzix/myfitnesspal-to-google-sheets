import myfitnesspal

client = myfitnesspal.Client()

day = client.get_date(2023, 4, 10)
day
# console log day
day.meals
print(day.meals)
print(day)
