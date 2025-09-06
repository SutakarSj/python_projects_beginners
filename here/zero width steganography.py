# Function to encrypt plain text into hidden zero-width characters
def encrypt(txt):
    # Convert each character into 8-bit binary
    binary = ''.join(format(ord(char), '08b') for char in txt)
    
    # Mapping: 0 -> Zero Width Non-Joiner (U+200C), 1 -> Zero Width Joiner (U+200D)
    mp = {'0': '\u200C', '1': '\u200D'}
    
    ans = []
    # Replace each binary digit with hidden character
    for i in binary:
        ans.append(mp[i])
    
    # Save the binary form to a file (optional debug step)
    f = open("dummy.txt", "w")
    f.write(binary)
    f.close()
    
    # Create hidden text string with zero-width characters
    hidden_txt = ''.join(mp[bit] for bit in binary)
    return hidden_txt, ans


# Function to decrypt hidden zero-width characters back into text
def decrypt(hidden):
    # Reverse mapping: hidden characters back to binary digits
    mp = {'\u200C': '0', '\u200D': '1'}
    
    # Extract binary from hidden characters
    binary = ''.join(mp[char] for char in hidden if char in mp)
    
    # Convert every 8 bits into a character
    return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))


# Main function to run the program
def main():
    # Take user input
    text = input("Enter plain text : ")
    
    # Encrypt into hidden characters
    hidden, ans = encrypt(text)
    print("\nHidden text:", hidden, " (invisible characters)")
    print("\nHidden values (list):", ans)
    
    # Decrypt back into original text
    decoded = decrypt(hidden)
    print("\nDecoded text:", decoded)


# Entry point
if __name__ == "__main__":
    main()
