import pyfiglet
from colorama import Fore, Back, Style
from rich.console import Console
from rich.markdown import Markdown

#Title
print(Fore.YELLOW + pyfiglet.figlet_format("            Decrypt  It", font = "roman", width=1000))

#Greeting
MARKDOWN = """
# Welcome to Descrypt It!
### This program will help you to convert an encrypted message back to its original and readable format.
"""
console = Console()
md = Markdown(MARKDOWN, style="bold magenta")
console.print(md, style="bold purple")


#Ask the user for the encrypted text he/she wants to decrypt
user_input = str(input(Fore.WHITE + "\nKindly enter the encrypted text that you want to decrypt: "))

#Decrypt the text by replacing/changing the following characters with their corresponding alphabet
chars_substitute = {"*": "a", "&": "e", "#": "i", "+": "o", "!":"u"}
decrypted_txt = ""
for letter in user_input:
    if letter in chars_substitute:
        decrypted_txt += chars_substitute[letter]
    else: 
        decrypted_txt += letter
print('\n')

#Processing the Output/Loading
from rich.progress import track
from time import sleep
def process_data():
    sleep(0.02)
for _ in track(range(100), description='[yellow]Processing data'):
    process_data()

#Display the decrypted text to the user
print("\n")
print("=" * 165)
from rich.console import Console
console = Console()
console.print("[bold magenta]Here is the descrypted format of your input[/bold magenta]: ", decrypted_txt)
print("=" * 165)