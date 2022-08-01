def emoiji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😃",
        ":(": "😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoiji_converter(message))
