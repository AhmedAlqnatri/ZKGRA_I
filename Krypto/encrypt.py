class Encrypt:

    """
    This function takes as an input a string and encrypts it by flipping the alphabet and return the decoded string.
    """
    def encrypt_a(surname: str) -> str:
        encrypted_surname: str = ""

        for letter in surname:

            if letter.isupper():
                new_unicode: int = ord("Z") - ((ord(letter) + 25) - ord("Z"))
                new_character: str = chr(new_unicode)
                encrypted_surname += new_character

            elif letter.islower():
                new_unicode: int = ord("z") - ((ord(letter) + 25) - ord("z"))
                new_character: str = chr(new_unicode)
                encrypted_surname += new_character

            else:
                encrypted_surname += letter

        return encrypted_surname

    """
    This function takes as an input a string and encrypts it by splitting the alphabet into two halfs and then flipping the alphabet in each half.
    """
    def encrypt_b(surname):

        encrypted_surname = ""

        for letter in surname:

            if letter.isupper():
                if ord(letter) <= ord("M"):

                    new_unicode = ord("M") - ((ord(letter) + 12) - ord("M"))
                    new_character = chr(new_unicode)
                    encrypted_surname += new_character

                else:

                    new_unicode = ord("Z") - ((ord(letter) + 12) - ord("Z"))
                    new_character = chr(new_unicode)
                    encrypted_surname += new_character

            elif letter.islower():
                if ord(letter) <= ord("m"):

                    new_unicode = ord("m") - ((ord(letter) + 12) - ord("m"))
                    new_character = chr(new_unicode)
                    encrypted_surname += new_character

                else:

                    new_unicode = ord("z") - ((ord(letter) + 12) - ord("z"))
                    new_character = chr(new_unicode)
                    encrypted_surname += new_character

            else:
                encrypted_surname += letter

        return encrypted_surname

    """
    This function takes as an input a string and encrypts it by taking the position of the first letter in the sring 
    and thin shift the values of positions of each letter in the string by that value and at the end it returns a decrypted string.
    """
    def encrypt_c(surname):

        if surname[0].isupper():
            shift = ord(surname[0]) - ord("A") + 1
        elif surname[0].islower():
            shift = ord(surname[0]) - ord("a") + 1
        else:
            return

        encrypted_surname = ""

        for letter in surname:

            if letter.isupper():

                new_index = ((ord(letter) - ord("A")) + shift) % 26
                new_unicode = new_index + ord("A")
                new_character = chr(new_unicode)
                encrypted_surname += new_character

            elif letter.islower():

                new_index = ((ord(letter) - ord("a")) + shift) % 26
                new_unicode = new_index + ord("a")
                new_character = chr(new_unicode)
                encrypted_surname += new_character

            else:
                encrypted_surname += letter

        return encrypted_surname
