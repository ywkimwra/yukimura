"""
# slightly smiling face
print("\U0001F642")
# slightly frowning face
print("\U0001F641")
"""

def convert(text):
    text = text.replace(":(", "\U0001F641")
    text = text.replace(":)", "\U0001F642")
    return text


def main():
    user_input = input("Enter your text: ")
    converted_text = convert(user_input)
    print("Converted text:", converted_text)

main()