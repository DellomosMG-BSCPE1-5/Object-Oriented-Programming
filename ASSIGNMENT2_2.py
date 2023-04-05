while True:
    import pyfiglet
    from colorama import Fore, Back, Style
    from rich.console import Console
    from pyboxen import boxen

    #Title
    print(Fore.BLUE + pyfiglet.figlet_format("  The  Vigenère  Cipher   ", font = "xsansb", width=500))

    #Greeting
    print(
        boxen(
            "This program will help you in converting plaintext and keyword into ciphertext using the Vigenère Cipher.",
            color="bold blue",
        )
    )

    #Ask the user the message string and the key string
    print(Fore.BLUE + Style.BRIGHT + "✨ Message " + Fore.LIGHTCYAN_EX + Style.NORMAL + "\nKindly enter a plain text message in all uppercase letters with no spaces: ", end = "")
    message_input = input(Fore.WHITE + "")
    print(Fore.BLUE + Style.BRIGHT + "\n✨ Key " + Fore.LIGHTCYAN_EX + Style.NORMAL + "\nKindly enter a plain text key in all uppercase letters with no spaces: ", end = "")
    key_input = input(Fore.WHITE + "")

    #List the letter values that will be used in translating the plaintext inputted by the user
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    index_letters = []
    for letter in letters:
        index_letters.append(letters.index(letter))

    #Use the number substitute to turn each element by its corresponding number
    new_message_string = []
    for letter in message_input:
        new_message_string.append(letters.index(letter))

    new_key_string = []
    for letter in key_input:
        new_key_string.append(letters.index(letter))

    #Get the sum of each elements from message and key which are aligned in column, then the mod 26 of each sum
    mod = []
    for i in range(len(new_message_string)):
        mod.append((new_message_string[i] + new_key_string[i % len(new_key_string)]) % 26)

    #Encrypt
    encrypted_txt = ""
    for i in mod:
        if i in index_letters:
            encrypted_txt += letters[i]
        else: 
            encrypted_txt += i

    #Processing the Output/Loading
    print('\n')
    from rich.progress import track
    from time import sleep
    def process_data():
        sleep(0.01)
    for _ in track(range(100), description='[blue]Processing data'):
        process_data()
        
    #Display the decrypted text to the user
    print("\n")
    print(Fore.BLUE + "=" * 105)
    console = Console()
    console.print("[cyan]Message[cyan]: ", message_input.upper())
    console.print("[cyan]Key[cyan]: ", key_input.upper())
    console.print("[cyan]Here is the encrypted format of your input[cyan]: ", encrypted_txt)
    print(Fore.BLUE + "=" * 105)

    #Ask the user if he/she wants to try again the program.
    check = input(Fore.YELLOW + "\nDo you want to start again? enter Y to restart or press another key to end: ")  # Asking the user if he/she wants to try/start again.
    if check.upper() == "Y":  
        continue
    break
