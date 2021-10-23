class Decrypt:

    """
    This function takes as an input enrypted string and outputs a decypted string by flipping the position of the letters.
    """
    def decrypt_a(encrypted_surname):

        decrypted_surname = ""

        for letter in encrypted_surname:

            if letter.isupper():
                new_unicode = ord("Z") - ((ord(letter) + 25) - ord("Z"))
                new_character = chr(new_unicode)
                decrypted_surname += new_character

            elif letter.islower():
                new_unicode = ord("z") - ((ord(letter) + 25) - ord("z"))
                new_character = chr(new_unicode)
                decrypted_surname += new_character

            else:
                decrypted_surname += letter

        return decrypted_surname

    """
    This function takes as an input an encrypted string and decrypts it by splitting the alphabet into two halfs and then flipping the alphabet in each half.
    """
    def decrypt_b(encrypted_surname):

        decrypted_surname = ""

        for letter in encrypted_surname:

            if letter.isupper():
                if ord(letter) <= ord("M"):

                    new_unicode = ord("M") - ((ord(letter) + 12) - ord("M"))
                    new_character = chr(new_unicode)
                    decrypted_surname += new_character

                else:

                    new_unicode = ord("Z") - ((ord(letter) + 12) - ord("Z"))
                    new_character = chr(new_unicode)
                    decrypted_surname += new_character

            elif letter.islower():
                if ord(letter) <= ord("m"):

                    new_unicode = ord("m") - ((ord(letter) + 12) - ord("m"))
                    new_character = chr(new_unicode)
                    decrypted_surname += new_character

                else:

                    new_unicode = ord("z") - ((ord(letter) + 12) - ord("z"))
                    new_character = chr(new_unicode)
                    decrypted_surname += new_character

            else:
                decrypted_surname += letter

        return decrypted_surname

    """
    This function taskes as an input an encrypted string and a shifter value and then it back revrese the positions of the letter by the shift value
    and returns a decrypted string.
    """
    def decrypt_c(encrypted_surname, shift):

        decrypted_surname = ""

        for letter in encrypted_surname:

            if letter.isupper():

                new_index = ((ord(letter) - ord("A")) - shift) % 26
                new_unicode = new_index + ord("A")
                new_character = chr(new_unicode)
                decrypted_surname += new_character

            elif letter.islower():

                new_index = ((ord(letter) - ord("a")) - shift) % 26
                new_unicode = new_index + ord("a")
                new_character = chr(new_unicode)
                decrypted_surname += new_character

            else:
                decrypted_surname += letter

        return decrypted_surname

    def decrypt_all(message: str):
        list_decoded_message = []
        list_decoded_message.append(
            {"algorithm 1": Decrypt.decrypt_a(message)}
        )
        list_decoded_message.append(
            {"algorithm 2": Decrypt.decrypt_b(message)}
        )
        list_decrypted_1c = []
        for shift in range(1, 27):
            list_decrypted_1c.append(Decrypt.decrypt_c(message, shift))
        list_decoded_message.append({"algorithm 3": list_decrypted_1c})

        for decoded_message in list_decoded_message:
            print(decoded_message)
