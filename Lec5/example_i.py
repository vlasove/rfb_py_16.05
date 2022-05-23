# Решение задачи K

count = 0

LOW_PULSE_LIMIT = 100
HIGH_PULSE_LIMIT = 140

MAX_PULSE, MIN_PULSE = 99, 141

while True:
    pulse = float(input())
    if pulse < 0:
        break

    if pulse >= LOW_PULSE_LIMIT and pulse <= HIGH_PULSE_LIMIT:
        count += 1

        if pulse > MAX_PULSE:
            MAX_PULSE = pulse

        if pulse < MIN_PULSE:
            MIN_PULSE = pulse


print(count)
print(MIN_PULSE, MAX_PULSE)