# sources
# https://www.w3schools.com/python/python_regex.asp
import re

lines_text = []
grouped_numbers_list = []
count = 0

f = open("text1.txt", "r")
for x in f:
    lines_text.append(x[0:-1])

f.close()

for i in range(len(lines_text)):
    if re.findall(r"\d+", lines_text[i]):
        if re.findall(r"[0-9]{1}", lines_text[i]):
            x = re.findall(r"[0-9]{1}", lines_text[i])

            if len(x) == 1:
                grouped_numbers_list.append(int("".join(x+x)))
                count += 1
            else:
                grouped_numbers_list.append(int("".join(x[0]+x[-1])))
                count += 1
    else:
        continue

print(count)
print(sum(grouped_numbers_list))