n = int(input())

day_seconds = 24 * 60 * 60
hour_seconds = 60 * 60
minute_seconds = 60

days = n // day_seconds
n = n % day_seconds

hours = n // hour_seconds
n = n % hour_seconds

minutes = n // minute_seconds
seconds = n % minute_seconds

hours = str(hours).zfill(2)
minutes = str(minutes).zfill(2)
seconds = str(seconds).zfill(2)

if days == 1 or (days % 10 == 1 and days != 11):
    day_word = "день"
elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
    day_word = "дні"
else:
    day_word = "днів"

print(str(days) + " " + day_word + ", " + hours + ":" + minutes + ":" + seconds)