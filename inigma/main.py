from string import ascii_lowercase
import random


string_lowercase = ascii_lowercase
list_lowercase = [*string_lowercase]

test = True

if not test:
    inp_rot_pos_0 = int(input("Rotor at position 1(1, 2, 3, 4, 5): ")) - 1
    inp_rot_pos_1 = int(input("Rotor at position 2(1, 2, 3, 4, 5): ")) - 1
    inp_rot_pos_2 = int(input("Rotor at position 3(1, 2, 3, 4, 5): ")) - 1

    start_pos_rot_0 = int(input("Starting position of rotor at position 1(1 - 26): ")) - 1
    start_pos_rot_1 = int(input("Starting position of rotor at position 2(1 - 26): ")) - 1
    start_pos_rot_2 = int(input("Starting position of rotor at position 3(1 - 26): ")) - 1

    characters_to_change_ls = []
    print("Change Characters (to move on press enter)")
    while True:
        character_to_change = input("Characters_to_change in format \"a : b\": ")
        if character_to_change == "":
            break

        characters_to_change_ls.append([character_to_change[0], character_to_change[4]])


def change_letter(char: str, change_set: list[list[str, str]]):
    for el in change_set:
        if el[0] == char:
            return el[1]
    return 0


class EnigmaMachine:
    def __init__(self, rotor_location: list[list[int]], changed_characters: list[list[str]]):
        """
        rotor_location: list
            [[2, 5], [4, 0], [0, 24]]
        changed_characters: list
            [["a", "z"], ["l", "q"]]

        """
        self.rotor_location = rotor_location
        self.changed_characters = changed_characters

        self.rotors_selected = [rotor_location[0][0], rotor_location[1][0], rotor_location[2][0]]
        self.rotors = self.Rotors(list_lowercase)

        self.TestSteckbrett = self.Steckbrett(changed_characters)
        self.set_rotor()

    def encrypt(self, message):
        message = message.lower()
        message = message.replace(" ", "")
        encrypted_message = ""
        for char in message:
            single_rotor = self.rotors
            char = single_rotor.run_through_rotor(char, self.rotor_location[0][0])
            char = single_rotor.run_through_rotor(char, self.rotor_location[1][0])
            char = single_rotor.run_through_rotor(char, self.rotor_location[2][0])
            char = single_rotor.run_through_rotor(char, 5)
            char = single_rotor.run_through_rotor(char, self.rotor_location[2][0])
            char = single_rotor.run_through_rotor(char, self.rotor_location[1][0])
            char = single_rotor.run_through_rotor(char, self.rotor_location[0][0])
            char = self.TestSteckbrett.run_through_steckbrett(char)

            encrypted_message += char
            self.rotors.rotate_rotors(self.rotors_selected)

        return encrypted_message

    def decrypt(self, message):
        message = message.lower()
        message = message.replace(" ", "")
        decrypted_message = ""
        for char in message:
            single_rotor = self.rotors
            char = single_rotor.run_through_rotor_backwards(char, self.rotor_location[0][0])
            char = single_rotor.run_through_rotor_backwards(char, self.rotor_location[1][0])
            char = single_rotor.run_through_rotor_backwards(char, self.rotor_location[2][0])
            char = single_rotor.run_through_rotor_backwards(char, 5)
            char = single_rotor.run_through_rotor_backwards(char, self.rotor_location[2][0])
            char = single_rotor.run_through_rotor_backwards(char, self.rotor_location[1][0])
            char = single_rotor.run_through_rotor_backwards(char, self.rotor_location[0][0])
            char = self.TestSteckbrett.run_through_steckbrett(char)

            decrypted_message += char
            self.rotors.rotate_rotors(self.rotors_selected)

        return decrypted_message

    def set_rotor(self):
        for i in range(len(self.rotor_location)):
            self.rotors.rotate_rotor(self.rotor_location[i][0], self.rotor_location[i][1])

    class Steckbrett:
        def __init__(self, changed_characters: list[list[str, str]]):

            # TODO: Add check if multible letters change the same char

            temp_list_lowercase = list_lowercase.copy()
            for i, el in enumerate(temp_list_lowercase):
                temp_list_lowercase[i] = [el, el]
            steckbrett_list_list = temp_list_lowercase

            # FUCKING HELL DON'T TOUCH IT
            for i, unchanged_characters in enumerate(steckbrett_list_list):  # el = ['a', 'a']
                for k, character_to_change in enumerate(changed_characters):  # character_to_change = ["a", "b"]
                    if unchanged_characters[0] == character_to_change[0]:  # if 'a' == 'a'
                        steckbrett_list_list[i][1] = character_to_change[1]
                        for j, second_ctc in enumerate(steckbrett_list_list):
                            if second_ctc[0] == character_to_change[1]:
                                steckbrett_list_list[j][1] = character_to_change[0]
                                break

            self.steckbrett_list = steckbrett_list_list

        def run_through_steckbrett(self, char):
            for el in self.steckbrett_list:
                if el[0] == char:
                    return el[1]

    class Rotors:
        def __init__(self, characters: list):
            self.rotors = []
            self.characters = characters
            self.rotors_000()
            self.chars_pressed = 0

        def rotate_rotor(self, rotor: int, starting_position: int = 1):
            """
            :type rotor: int
            :type starting_position 0 <= starting_position <= 25
            """
            for k in range(starting_position):
                rot_pos_1 = self.rotors[rotor][0][1]
                for i in range(len(self.rotors[rotor])):
                    if i == len(self.rotors[rotor]) - 1:
                        self.rotors[rotor][-1][1] = rot_pos_1
                    else:
                        self.rotors[rotor][i][1] = self.rotors[rotor][i + 1][1]
        
        def rotors_000(self):
            num_of_rotors = 6
            rotors = []
            for i in range(num_of_rotors):
                temp_characters = self.characters.copy()
                random.Random(i).shuffle(temp_characters)
                rotors.append(temp_characters.copy())

            for el in rotors:
                for index, char in enumerate(el):
                    el[index] = [self.characters[index], char]
            
            self.rotors = rotors
        
        def rotate_rotors(self, rotors_selected: list[int]):
            self.chars_pressed += 1
            self.rotate_rotor(rotors_selected[0])
            if self.chars_pressed // 26 == 0:
                self.rotate_rotor(rotors_selected[1])
            if self.chars_pressed // 26**2 == 0:
                self.rotate_rotor(rotors_selected[2])
                self.chars_pressed = 0

        def run_through_rotor(self, char: str, rotor: int):
            for el in self.rotors[rotor]:
                if el[0] == char:
                    return el[1]
            return 0

        def run_through_rotor_backwards(self, char: str, rotor: int):
            for el in self.rotors[rotor]:
                if el[1] == char:
                    return el[0]

            return 0


if not test:
    test_machine = EnigmaMachine([[inp_rot_pos_0, start_pos_rot_0], [inp_rot_pos_1, start_pos_rot_1], [inp_rot_pos_2, start_pos_rot_2]], characters_to_change_ls)

    while True:
        de_or_encrypt = input("Type \"e\" to encrypt, type \"d\" to decrypt: ")
        if de_or_encrypt == "e":
            msg = input("Message to encrypt: ")
            ret_msg = test_machine.decrypt(msg)
            print("Decrypted string: " + ret_msg)
            break

        elif de_or_encrypt == "d":
            msg = input("Message to encrypt: ")
            ret_msg = test_machine.encrypt(msg)
            print("Encrypted string: " + ret_msg)
            break

if test:
    test_machine = EnigmaMachine([[0, 0], [1, 1], [2, 2]], [])
    msg = test_machine.encrypt("Hello World")
    print("enc: " + msg)
    msg = test_machine.decrypt("xa")
    print("dec: " + msg)

# [['a', 'o'], ['b', 'a'], ['c', 'x'], ['d', 's'], ['e', 'g'], ['f', 'f'], ['g', 'h'], ['h', 'k'], ['i', 'w'], ['j', 'u'], ['k', 'e'], ['l', 'c'], ['m', 'v'], ['n', 'd'], ['o', 'r'], ['p', 'l'], ['q', 't'], ['r', 'j'], ['s', 'z'], ['t', 'p'], ['u', 'q'], ['v', 'i'], ['w', 'b'], ['x', 'n'], ['y', 'y'], ['z', 'm']]
# [['a', 'x'], ['b', 'y'], ['c', 'l'], ['d', 'k'], ['e', 'w'], ['f', 'b'], ['g', 'f'], ['h', 'z'], ['i', 't'], ['j', 'n'], ['k', 'j'], ['l', 'r'], ['m', 'q'], ['n', 'a'], ['o', 'h'], ['p', 'v'], ['q', 'g'], ['r', 'm'], ['s', 'u'], ['t', 'o'], ['u', 'p'], ['v', 'd'], ['w', 'i'], ['x', 'c'], ['y', 's'], ['z', 'e']]
# [['a', 'd'], ['b', 'u'], ['c', 'r'], ['d', 'p'], ['e', 'a'], ['f', 'x'], ['g', 'e'], ['h', 'h'], ['i', 'o'], ['j', 'q'], ['k', 't'], ['l', 'w'], ['m', 'm'], ['n', 's'], ['o', 'k'], ['p', 'n'], ['q', 'v'], ['r', 'z'], ['s', 'g'], ['t', 'i'], ['u', 'j'], ['v', 'f'], ['w', 'l'], ['x', 'y'], ['y', 'c'], ['z', 'b']]
# [['a', 'g'], ['b', 'q'], ['c', 'x'], ['d', 'o'], ['e', 'b'], ['f', 'f'], ['g', 'v'], ['h', 'k'], ['i', 'j'], ['j', 'n'], ['k', 'z'], ['l', 'm'], ['m', 'd'], ['n', 'i'], ['o', 'w'], ['p', 'u'], ['q', 'a'], ['r', 'c'], ['s', 'y'], ['t', 'p'], ['u', 't'], ['v', 'l'], ['w', 'e'], ['x', 'r'], ['y', 's'], ['z', 'h']]
# [['a', 'v'], ['b', 'l'], ['c', 'z'], ['d', 's'], ['e', 'n'], ['f', 'b'], ['g', 'g'], ['h', 'u'], ['i', 'f'], ['j', 'k'], ['k', 'i'], ['l', 'x'], ['m', 'r'], ['n', 'o'], ['o', 'q'], ['p', 'y'], ['q', 'w'], ['r', 'a'], ['s', 't'], ['t', 'c'], ['u', 'e'], ['v', 'p'], ['w', 'm'], ['x', 'd'], ['y', 'j'], ['z', 'h']]
# [['a', 'c'], ['b', 'k'], ['c', 'e'], ['d', 'm'], ['e', 'j'], ['f', 'n'], ['g', 'z'], ['h', 'w'], ['i', 's'], ['j', 'y'], ['k', 'g'], ['l', 'd'], ['m', 'r'], ['n', 'p'], ['o', 'v'], ['p', 'f'], ['q', 'b'], ['r', 'h'], ['s', 'o'], ['t', 'a'], ['u', 'q'], ['v', 'u'], ['w', 'l'], ['x', 'x'], ['y', 'i'], ['z', 't']]



