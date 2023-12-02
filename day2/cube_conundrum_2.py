import re

lines_text = []

pattern = r"(?:\d+)"
split_pattern = r"(?:[;])"
game_number_pattern = r"\d+"    
remove_game_pattern = r"Game\s\d+:\s"


f = open("puzzle_input.txt", "r")
for line in f:
    lines_text.append(line[0:-1])

f.close


def remove_game_number(list_to_process):
    target_list = []
    for i in range(len(list_to_process)):
        target_list.append(re.sub(remove_game_pattern,"",list_to_process[i]))
    
    return target_list

# split into sets of rgb (unordered)
def split_into_sets_of_rgb(list_to_process):
    target_list = []
    for i in range(len(list_to_process)):
        target_list.append(re.split(split_pattern, list_to_process[i]))
    
    return target_list


processed_list = remove_game_number(lines_text)
# print(processed_list)
processed_list_2 = split_into_sets_of_rgb(processed_list)
# print(processed_list_2)

def check_highest_rgb(game_to_check):
    print(game_to_check)
    list_red = []
    list_green = []
    list_blue = []

    for element in game_to_check:
        print(f"element: {element}")

        pattern = r"(\d+) (red|green|blue)"
        counts = re.findall(pattern, element)

        print(f"counts: {counts}")

        for value, color in counts:
            if color == "red":
                list_red.append(int(value))
            if color == "green":
                list_green.append(int(value))
            if color == "blue":
                list_blue.append(int(value))

    print(f"red: {list_red}")
    print(f"green: {list_green}")
    print(f"blue: {list_blue}")
    
    multiplied_results = max(list_red)*max(list_green)*max(list_blue)

    return multiplied_results

result = 0
for i in range(len(processed_list_2)):
    result = result + check_highest_rgb(processed_list_2[i])

print(f"result = {result}")