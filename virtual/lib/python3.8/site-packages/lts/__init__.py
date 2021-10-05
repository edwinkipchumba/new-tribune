def lts(text, separator=" "): # List to string function.
    output = ""
    for i in text:
        output += i + separator
    return output[:-1]
