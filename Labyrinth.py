def define_input():
    input_demanded = True
    inputs = []
    while input_demanded:
        input_line = input()
        if (input_line == "0 0 0"):
            input_demanded = False
        if (input_line != "" and input_line != "0 0 0"):
            inputs.append(input_line)
    return inputs


def draw_layers(number_of_layers, height, layers):
    global input_lines
    for layer_index in range(number_of_layers):
        layer = ""
        for height_index in range(height):
            layer += input_lines[(height_index + 1) * (layer_index + 1)]
            layer += "\n"
        layers.append(layer)


def go_north(current_coordinate):
    layer, row, entry = current_coordinate
    new_row = row + 1
    if new_row < 0 or new_row == height:
        return current_coordinate
    return (layer, new_row, entry)


def go_south(current_coordinate):
    layer, row, entry = current_coordinate
    new_row = row - 1
    if new_row < 0 or new_row == height:
        return current_coordinate
    return (layer, new_row, entry)


def go_right(current_coordinate):
    layer, row, entry = current_coordinate
    new_entry = entry + 1
    if new_entry < 0 or new_entry == length:
        return current_coordinate
    return (layer, row, new_entry)


def go_left(current_coordinate):
    layer, row, entry = current_coordinate
    new_entry = entry - 1
    if new_entry < 0 or new_entry == length:
        return current_coordinate
    return (layer, row, new_entry)


def go_up(current_coordinate):
    layer, row, entry = current_coordinate
    new_layer = layer + 1
    if new_layer < 0 or new_layer == number_of_layers:
        return current_coordinate
    return (new_layer, row, entry)


def go_down(current_coordinate):
    layer, row, entry = current_coordinate
    new_layer = layer - 1
    if new_layer < 0 or new_layer == number_of_layers:
        return current_coordinate
    return (new_layer, row, entry)


def is_border(function, start):
    return function(start) == start


def is_block(function, start):
    global labyrinth_dict
    new_coordinate = function(start)
    return labyrinth_dict[new_coordinate] == "#"


def is_in_black(black, coord):
    return coord in black


def clone_list(list):
    cloned_list = []
    for i in list:
        cloned_list.append(i)
    return cloned_list


def go(current_route, black):
    global trapped, length, height, number_of_layers
    new_start = current_route[len(current_route)-1]
    if(labyrinth_dict[new_start] == "E"):
        print("Entkommen in " + str(len(current_route)-1) + " Minute(n)!") #start position doesnt cost time -> -1
        trapped= False
        return current_route
    if not is_border(go_north, new_start) and not is_block(go_north, new_start) and not is_in_black(black, new_start):
        cloned_route = clone_list(current_route)
        cloned_route.append(go_north(new_start))
        black_clone = clone_list(black)
        black_clone.append(new_start)
        go(cloned_route, black_clone)
    if not is_border(go_south, new_start) and not is_block(go_south, new_start) and not is_in_black(black, new_start):
        cloned_route = clone_list(current_route)
        cloned_route.append(go_south(new_start))
        black_clone = clone_list(black)
        black_clone.append(new_start)
        go(cloned_route, black_clone)
    if not is_border(go_right, new_start) and not is_block(go_right, new_start) and not is_in_black(black, new_start):
        cloned_route = clone_list(current_route)
        cloned_route.append(go_right(new_start))
        black_clone = clone_list(black)
        black_clone.append(new_start)
        go(cloned_route, black_clone)
    if not is_border(go_left, new_start) and not is_block(go_left, new_start) and not is_in_black(black, new_start):
        cloned_route = clone_list(current_route)
        cloned_route.append(go_left(new_start))
        black_clone = clone_list(black)
        black_clone.append(new_start)
        go(cloned_route, black_clone)
    if not is_border(go_up, new_start) and not is_block(go_up, new_start) and not is_in_black(black, new_start):
        cloned_route = clone_list(current_route)
        cloned_route.append(go_up(new_start))
        black_clone = clone_list(black)
        black_clone.append(new_start)
        go(cloned_route, black_clone)
    if not is_border(go_down, new_start) and not is_block(go_down, new_start) and not is_in_black(black, new_start):
        cloned_route = clone_list(current_route)
        cloned_route.append(go_down(new_start))
        black_clone = clone_list(black)
        black_clone.append(new_start)
        go(cloned_route, black_clone)
    pass


def calculate_labyrinth(layers, labyrinth_dict):
    global length, height, number_of_layers
    layer_index = 0
    start_position = (0, 0, 0)  # where letter is E - random init //TODO check if this is correct
    for layer in layers:
        rows = layer.split("\n")
        row_index = 0
        for row in rows:
            entries = list(row)
            entry_index = 0
            for entry in entries:
                coordinate = (layer_index, row_index, entry_index)
                labyrinth_dict[coordinate] = entry
                entry_index += 1
                if entry == "S":
                    start_position = coordinate
            row_index += 1
        layer_index += 1

    black_list = []
    go([start_position], black_list)
    if trapped:
        print("Gefangen :-(")


input_index = 0
input_lines = define_input()
for input in input_lines:
    if " " in input:  # then header
        trapped = True
        labyrinth_dict = {}
        layers = []
        number_of_layers, height, length = input.split(" ")
        number_of_layers, height, length = int(number_of_layers), int(height), int(length)
        draw_layers(number_of_layers, height, layers)
        calculate_labyrinth(layers, labyrinth_dict)
    input_index += 1
