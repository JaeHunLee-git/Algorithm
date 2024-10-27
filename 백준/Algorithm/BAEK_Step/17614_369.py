NumberString = input()
power = 1
prev_369 = 0
prev_num = 0
count = 0

for n in NumberString[::-1]:
    num = int(n)
    count += prev_369 * num + int((num - 1) / 3) * power
    if num > 0 and num % 3 == 0:
        count += 1 + prev_num
    prev_369 = 10 * prev_369 + 3 * power
    prev_num += num * power
    power *= 10

print(count)
