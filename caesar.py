def rotate_character (char,rot):
    import string

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    rotated_lower=""
    rotated_upper=""


    if char.isalpha() == True:
        if char in lowercase:
            rotated_lower_index = (alphabet_position(char)) + rot
            if rotated_lower_index < 26:
                rotated_lower = rotated_lower + lowercase[rotated_lower_index]
            else:
                rotated_lower = rotated_lower + lowercase[rotated_lower_index % 26]
            return rotated_lower

        else:
            if char in uppercase:
                rotated_upper_index = (alphabet_position(char)) + rot
                if rotated_upper_index < 26:
                    rotated_upper = rotated_upper + uppercase[rotated_upper_index]
                else:
                    rotated_upper = rotated_upper + uppercase[rotated_upper_index % 26]
                return rotated_upper

    else:
        return char


def alphabet_position(letter):
    import string

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    if letter in lowercase:
        letter_index_lowercase = lowercase.find(letter)
        return letter_index_lowercase

    elif letter in uppercase:
        letter_index_uppercase = uppercase.find(letter)
        return letter_index_uppercase
def encrypt(text, rot):
    import string
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase

    encrypted=""

    for char in text:
        if char == ' ':
            encrypted += char

        elif char.isalpha() != True:
            encrypted += char

        else:
            encrypted = encrypted + (rotate_character(char,rot))
    return encrypted




