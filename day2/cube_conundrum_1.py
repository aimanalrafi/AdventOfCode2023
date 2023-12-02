import re

lines_text = []

rgb_conf = [12, 13, 14]

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

def split_into_sets_of_rgb(list_to_process):
    target_list = []
    for i in range(len(list_to_process)):
        target_list.append(re.split(split_pattern, list_to_process[i]))
    
    return target_list

def check_game_illegal(game_to_check):
    print(game_to_check)

    for element in game_to_check:

        pattern = r"\s+(\d+)\s+(blue|red|green)"
        counts = dict(re.findall(pattern, element))

        # print(counts.items())

        for key, value in counts.items():
            if value == "red":
                if int(key) > 12:
                    print(f"illegal {value} of {key}")
                    return True
            elif value == "green":
                if int(key) > 13:
                    print(f"illegal {value} of {key}")
                    return True
            elif value == "blue":
                if int(key) > 14:
                    print(f"illegal {value} of {key}")
                    return True
    print("passed vibe check")
    return False


processed_list = remove_game_number(lines_text)
# print(processed_list)
processed_list_2 = split_into_sets_of_rgb(processed_list)
# print(processed_list_2)

numbers = []
spotted_games = []
count = 0



for game in range(len(processed_list_2)):
    true_game = game + 1
    print(f"game {true_game}")
    # print(processed_list_2[game])

    for sub_game in processed_list_2[game]:
        numbers.append(re.findall(r"\d+", sub_game))

    one_d_number_list = []
    # print(numbers)
    for elements in numbers:
        for element in elements:
            one_d_number_list.append(element)
    
    # print(one_d_number_list)
    for element in one_d_number_list:
        if int(element) > 14:
            spotted_games.append(true_game)
            print(f"{processed_list_2[game]}")
            print(f"game {true_game} is illegal")
            break
        elif int(element) > 12:
            print(f"check {true_game}")
            if check_game_illegal(processed_list_2[game]):
                spotted_games.append(true_game)
                print(f"game {true_game} has been added to spotted illegal games")
                break
    
    count = count + 1
    numbers.clear()
    one_d_number_list.clear()

print(spotted_games)
print(f"total iterations: {count}")
print(f"sum of illegal games: {sum(spotted_games)} with a total of {len(spotted_games)} games")
print(f"sum of valid games: {5050 - sum(spotted_games)}")
                





