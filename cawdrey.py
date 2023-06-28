import itertools
import threading
import time
import os
from yaspin import yaspin

default_charset = 'abcdefghijklmnopqrstuvwxyz0123456789'

def generate_words(min_length, max_length, charset):
    for length in range(min_length, max_length + 1):
        for word_tuple in itertools.product(charset, repeat=length):
            yield ''.join(word_tuple)

def update_spinner(spinner, start_time, keep_updating):
    while keep_updating[0]:
        elapsed_time = time.time() - start_time
        hours, rem = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(rem, 60)
        spinner.text = f"Loading... time elapsed: {int(hours)}:{int(minutes)}:{int(seconds)}"
        time.sleep(1)

def main():
    print("""
                       _                
  ___ __ ___      ____| |_ __ ___ _   _ 
 / __/ _` \ \ /\ / / _` | '__/ _ \ | | |
| (_| (_| |\ V  V / (_| | | |  __/ |_| |
 \___\__,_| \_/\_/ \__,_|_|  \___|\__, |
                                  |___/ 
    """)

    while True:
        try:
            min_length = int(input('Enter the minimum word length: '))
            max_length = int(input('Enter the maximum word length: '))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print(f"Enter your desired charset. Just press Enter for default ({default_charset}):")
    charset = input() or default_charset
    print(f"Generating words with charset: {charset}")

    print("Enter your desired output filename without extension. Just press Enter for default (wordlist):")
    filename = input() or 'wordlist'
    
    if not filename.endswith('.txt'):
        filename += '.txt'
    
    if os.path.exists(filename):
        overwrite = input(f"The file '{filename}' already exists. Do you want to overwrite it? (y/n) ")
        if overwrite.lower() != 'y':
            return
    
    print(f"The words will be saved in a file named '{filename}'")

    try:
        with open(filename, 'w') as f:
            with yaspin(text="Loading...", color="red") as spinner:
                start_time = time.time()

                keep_updating = [True]

                threading.Thread(target=update_spinner, args=(spinner, start_time, keep_updating), daemon=True).start()

                for word in generate_words(min_length, max_length, charset):
                    f.write(word + '\n')

                keep_updating[0] = False

                spinner.text = ""
                elapsed_time = time.time() - start_time  
                hours, rem = divmod(elapsed_time, 3600)
                minutes, seconds = divmod(rem, 60)
                spinner.ok(f"Done in {int(hours)}:{int(minutes)}:{int(seconds)}")  

    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting.")
        return

if __name__ == '__main__':
    main()
