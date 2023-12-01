# sources
# https://www.w3schools.com/python/python_regex.asp
import re

lines_text = []
result = []
grouped_numbers_list = []
count = 0

# pattern = r"(?:\d|one|two|three|four|five|six|seven|eight|nine)"
pattern = r"(?=(\d|zero|one|two|three|four|five|six|seven|eight|nine))"

word_to_number = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

f = open("text1.txt", "r")
for x in f:
    lines_text.append(x[0:-1])

f.close()

for i in range(len(lines_text)):
    if re.findall(pattern,lines_text[i]):
        x = re.findall(pattern,lines_text[i])
        # print(x)
        for y in x:
            if y.isdigit():
                result.append(y)
            else:
                z = word_to_number[y]
                result.append(z)
        if len(result) == 1:
            grouped_numbers_list.append(int("".join(result+result)))
            count += 1
        else:
            grouped_numbers_list.append(int("".join(result[0]+result[-1])))
            count += 1
        print(f"{lines_text[i]} -> {x} -> {grouped_numbers_list[i]}")
        result.clear()
    else:
        continue

print(count)
print(sum(grouped_numbers_list))