# Cawdrey

## Prerequisites

Ensure you have Python 3.6 or higher installed. You can download Python from the official site: [Download Python](https://www.python.org/downloads/)

## Step 1: Installing Dependencies

You need to install `yaspin`, a terminal spinner library for Python. Open your terminal and run:

```bash
pip install yaspin
```

## Step 2: Save the Script

Copy the Wordlist Generator script and save it into a Python file (e.g., `cawdrey.py`).

## Step 3: Run the Script

Navigate to the directory where you saved the script and run:

```bash
python cawdrey.py
```

## Step 4: Provide the Inputs

The script will ask you for the following inputs:

- `Minimum word length`: Enter the minimum length of the words you want to generate.
- `Maximum word length`: Enter the maximum length of the words you want to generate.
- `Charset`: Enter the characters you want the words to be made up of. If you press Enter without typing anything, it will use the default charset (i.e., all lowercase letters and digits).
- `Output filename`: Enter the name of the file where the words will be saved. If you press Enter without typing anything, it will use the default name 'wordlist'. The '.txt' extension will be added automatically if you don't include it.

## Step 5: Wait for the Generation to Complete

The script will start generating words and writing them to the output file. A spinner will be shown on the terminal along with the elapsed time. When the operation is complete, the total elapsed time will be displayed.

The resulting file with the generated words will be saved in the same directory where your script resides.

**Note**: Generating words with large lengths and/or charsets can take a considerable amount of time and disk space. Be aware of this before starting the operation.
