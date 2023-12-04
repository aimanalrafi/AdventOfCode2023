# works only if first and last line doesn't contain a symbol o.O

lines_text = []
final_sum = []

f = open("puzzle_input2.txt", "r")
for line in f:
    lines_text.append(line[0:-1])

f.close

# # print(lines_text)
symbols_list = ['*']
list_symbol_with_index = []

def get_symbols_and_indexes(lines_text):
    result = []
    for i_row in range(len(lines_text)):
        # # print(lines_text[i])
        for i_column, symbol in enumerate(lines_text[i_row]):
            # to look for symbols
            # if not re.search(r"[.]|\d", symbol):
            #     if symbol not in symbols_list:
            #         symbols_list.append(symbol)
            if symbol in symbols_list:
                result.append([symbol,[i_row,i_column]])

    # # print(result)
    return result


def extract_number_at_index(symbol, row, column):
    number = []
    while column >= 0 and lines_text[row][column] != '.' and lines_text[row][column] not in symbols_list:
        if lines_text[row][column - 1] == '.' or lines_text[row][column - 1] in symbols_list or column == 0 or column == (len(lines_text[row]) - 1):
            # print("start index of number found")
            # while lines_text[row][column] != '.' and lines_text[row][column] not in symbols_list:
            while lines_text[row][column].isdigit():
                # print(lines_text[row][column], end="")
                number.append(lines_text[row][column])
                lines_text[row] = lines_text[row][:column] + '.' + lines_text[row][column + 1:]
                if column < (len(lines_text[0]) - 1):
                    column = column + 1
        else:
            # print("haven't reached start index of number")
            column = column - 1
    
    # print(f"number in list: {number}")
    index_to_pop = []
    for i in range(len(number)):
        if not number[i].isdigit():
            # print(f"{number[i]} will be popped")
            index_to_pop.append(i)
    
    for i in range(len(index_to_pop)):
        number.pop(index_to_pop[i])

    extracted_number = int("".join(number))
    # print(f"extracted_number: {extracted_number}")
    # # print(lines_text[row])
    return extracted_number


#[<symbol>, [row, column]
# 
# .ooo. <- row - 1 and column, column + 1, column - 1
# .oxo. <- row and column - 1 , column + 1
# .ooo. <- row + 1 and  and column, column + 1, column - 1
#
def find_acceptable_numbers(list_symbol_with_index, lines_text):

    gear_set = []
    count_gear = 0
    for symbol, index in list_symbol_with_index:
        # # print(f"{symbol} at {index}")
        row = index[0]
        column = index[1]

        # .ooo. <-
        # .oxo. 
        # .ooo.
        if lines_text[row - 1][column].isdigit():
            # print(f"found digit adjacent to {symbol} at [{row}, {column}]")
            gear_set.append(extract_number_at_index({symbol}, row - 1, column))
            count_gear += 1
        if lines_text[row - 1][column - 1].isdigit():
            # print(f"found digit adjacent to {symbol} at [{row}, {column}]")
            gear_set.append(extract_number_at_index({symbol}, row - 1, column - 1))
            count_gear += 1
        if lines_text[row - 1][column + 1].isdigit():
            # print(f"found digit adjacent to {symbol} at [{row}, {column}]")
            gear_set.append(extract_number_at_index({symbol}, row - 1, column + 1))
            count_gear += 1

        # .ooo. 
        # .oxo. <-
        # .ooo.
        if lines_text[row][column - 1].isdigit():
            # print(f"found digit adjacent to {symbol} at [{row}, {column}]")
            gear_set.append(extract_number_at_index({symbol}, row, column - 1))
            count_gear += 1
        if lines_text[row][column + 1].isdigit():
            # print(f"found digit adjacent to {symbol} at [{row}, {column}]")
            gear_set.append(extract_number_at_index({symbol}, row, column + 1))
            count_gear += 1

        # .ooo. 
        # .oxo. 
        # .ooo. <-
        if lines_text[row + 1][column].isdigit():
            # print(f"found digit adjacent to {symbol} at [{row}, {column}]")
            gear_set.append(extract_number_at_index({symbol}, row + 1, column))
            count_gear += 1
        if lines_text[row + 1][column - 1].isdigit():
            # print(f"found digit adjacent to {symbol} at [{row}, {column}]")
            gear_set.append(extract_number_at_index({symbol}, row + 1, column - 1))
            count_gear += 1
        if lines_text[row + 1][column + 1].isdigit():
            # print(f"found digit adjacent to {symbol} at [{row}, {column}]")
            gear_set.append(extract_number_at_index({symbol}, row + 1, column + 1))
            count_gear += 1
        
        if(count_gear == 2):
            # final_sum.append(gear_set)
            print(f"gear found: {gear_set}")
            
            final_sum.append((gear_set[0] * gear_set[1]))
        
        gear_set.clear()
        count_gear = 0


list_symbol_with_index = get_symbols_and_indexes(lines_text)

find_acceptable_numbers(list_symbol_with_index, lines_text)

# print(f"{final_sum}")
print(f"{sum(final_sum)}")
# for i_row in range(len(lines_text)):
#     print(lines_text[i_row])


        
