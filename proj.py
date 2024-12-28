class StringReverse:
    def __init__(self, input_reverse):
        self.input_reverse = input_reverse

    def reverse(self):
        return self.input_reverse[::-1]

string_to_reverse = "Ayesha and Amreen"
reverser = StringReverse(string_to_reverse)
reversed_string = reverser.reverse()

print("Original String:", string_to_reverse)
print("Reversed String:", reversed_string)