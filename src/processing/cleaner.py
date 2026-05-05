def clean_txt(text):
    text = text.replace("\n\n", "\n")  # Replace multiple newlines with a single newline
    text = text.strip()  # Remove leading and trailing whitespace
    return text