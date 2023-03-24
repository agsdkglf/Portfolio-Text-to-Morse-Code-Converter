from art import logo

morse_code = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
    "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----",
    "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.", "!": "-.-.--", "/": "-..-.",
    "(": "-.--.", ")": "-.--.-", "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-", "+": ".-.-.", "-": "-....-",
    "_": "..--.-", "''": ".-..-.", "$": "...-..-", "@": ".--.-."
}

print(logo)


def morse_code_converter():
    
    """Function to convert a string into Morse Code."""

    string_to_convert = input("Write a string to be converted into Morse Code: \n").upper()
    list_string = list(string_to_convert)

    coded_string = []

    for l_s in list_string:
        if l_s in morse_code:
            coded_string.append(morse_code[l_s])
        else:
            return "Use only Latin characters, numbers or punctuation."

    return coded_string


print("\n")
print(morse_code_converter())
