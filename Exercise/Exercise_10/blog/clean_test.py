def clean_text(text):
    # Remove leading and trailing whitespace characters
    text = text.strip()
   
    # Convert all characters to lowercase
    text = text.lower()
   
    # Remove duplicate consecutive characters
    cleaned = ''
    for i in range(len(text)):
        if i == 0 or text[i] != text[i-1]:
            cleaned += text[i]
   
    return cleaned
 
cleaned_text = clean_text("   This  Text  Needs  Cleaning  \n")
print(cleaned_text)