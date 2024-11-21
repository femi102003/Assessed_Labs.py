def decrypt_cypher_text(text, key):
    """
    This function decrypts a given text using a specified key.

    Parameters:
    ----------
    text : str
        The text to be decrypted.
    key : int
        A positive integer used as the key for decryption.

    Returns: sss
    -------
    str:
        The decrypted text as a single string.
    """
    decrypted_text = ""
    for char in text:
        ascii_code = ord(char)
        decrypted_ascii = (ascii_code - key) % 256
        decrypted_char = chr(decrypted_ascii)
        decrypted_text += decrypted_char

    return decrypted_text

# Example usage
text = "Hdfk#huuru#|rx#pdnh#lq#surjudpplqj#lv#dq#rssruwxqlw|#wr#ehfrph#d#ehwwhu#ghyhorshu$"  # Encrypted text
key = 3
print("The decrypted text is:", decrypt_cypher_text(text, key))  # Expected output: "Hello World"