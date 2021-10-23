import timeit
import inquirer
from encrypt import Encrypt
from decrypt import Decrypt

status = True
while status:
    questions = [
        inquirer.List('test_type',
                      message="What test do you want to run?",
                      choices=['Test a', 'Test b',
                               'Test c', 'Test All', 'Exit Testing'],
                      ),
    ]
    answers = inquirer.prompt(questions)

    if answers['test_type'] == 'Test a':

        string = input("Enter your message: ")
        start = timeit.default_timer()

        encrypted_surname = Encrypt.encrypt_a(surname=string)

        end = timeit.default_timer()

        print("Encrypted message: ", encrypted_surname)
        print("---  seconds for encrypting ---", end-start)

        start = timeit.default_timer()

        decrypted_surname = Decrypt.decrypt_a(encrypted_surname)

        end = timeit.default_timer()

        print("Decrypted message: ", decrypted_surname)
        print("---  seconds for decrypting ---", end-start)

    elif answers['test_type'] == 'Test b':

        string = input("Enter your message: ")
        start = timeit.default_timer()

        encrypted_surname = Encrypt.encrypt_b(string)

        end = timeit.default_timer()

        print("Encrypted message: ", encrypted_surname)
        print("---  seconds for encrypting ---", end-start)

        start = timeit.default_timer()

        decrypted_surname = Decrypt.decrypt_b(encrypted_surname)

        end = timeit.default_timer()

        print("Decrypted message: ", decrypted_surname)
        print("---  seconds for decrypting ---", end-start)

    elif answers['test_type'] == 'Test c':

        string = input("Enter your message: ")
        start = timeit.default_timer()

        encrypted_surname = Encrypt.encrypt_c(string)
        end = timeit.default_timer()
        print("Encrypted message: ", encrypted_surname)
        print("---  seconds for encrypting ---", end-start)

        if encrypted_surname != None:
            list_decrypted_surname = []
            start = timeit.default_timer()

            for shift in range(1, 27):
                result = Decrypt.decrypt_c(encrypted_surname, shift)
                list_decrypted_surname.append(result)

            end = timeit.default_timer()
            print("List of all possible decryptions...")
            for surname in list_decrypted_surname:
                print(surname)

            print("---  seconds for decrypting ---", end-start)

    elif answers['test_type'] == 'Test All':

        string = input("Enter your message: ")
        start = timeit.default_timer()
        Decrypt.decrypt_all(string)
        end = timeit.default_timer()
        print("---  seconds for decrypting all 3 ways ---", end-start)

    elif answers['test_type'] == 'Exit Testing':

        status = False
