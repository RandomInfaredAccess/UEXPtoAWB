import sys
import binascii
import os
import tkinter as tk
from tkinter import filedialog

def extract_data(file_path, start_marker, start_offset):
    with open(file_path, 'rb') as file:
        data = file.read()

    # Find the start marker position
    start_pos = data.find(start_marker.encode())

    # Check if the start marker is found
    if start_pos == -1:
        raise ValueError("Start marker not found in the file.")

    # Calculate the new start offset
    start_offset = start_pos

    # Extract the data
    extracted_data = data[start_offset:]

    return extracted_data

def extract_prior_data(file_path, start_marker, start_offset):
    with open(file_path, 'rb') as file:
        data = file.read()

    # Find the start marker position
    start_pos = data.find(start_marker.encode())

    # Check if the start marker is found
    if start_pos == -1:
        raise ValueError("Start marker not found in the file.")

    # Calculate the new start offset
    start_offset = 0

    # Extract the prior data
    prior_data = data[start_offset:start_pos]

    return prior_data

def process_file(file_path, create_bytes):
    start_marker = "AFS2"
    start_offset = 0

    try:
        extracted_data = extract_data(file_path, start_marker, start_offset)

        output_file = file_path + ".awb"
        with open(output_file, 'wb') as file:
            file.write(extracted_data)
        print("Audio extraction completed! Output file:", output_file)

        if create_bytes:
            prior_data = extract_prior_data(file_path, start_marker, start_offset)
            prior_output_file = file_path + ".REPLACEMENT BYTES.uexp"
            with open(prior_output_file, 'wb') as file:
                file.write(prior_data)
            print("Bytes created!")

        # Open the destination file in another file explorer window
        os.startfile(os.path.dirname(output_file))

    except FileNotFoundError:
        print("Error: File not found. Please provide a valid file path.")
    except ValueError as ve:
        print("Error:", str(ve))
    except Exception as e:
        print("An error occurred during audio extraction:", str(e))

def main():
    if len(sys.argv) > 1:
        # Process file paths from command line arguments
        create_choice = input("Do you want to create replacement bytes? (yes/no): ").lower().strip()
        create_bytes = create_choice == "yes"

        for file_path in sys.argv[1:]:
            process_file(file_path, create_bytes)
    else:
        # Prompt the user to select the .uexp files using file explorer dialog
        root = tk.Tk()
        root.withdraw()
        file_paths = filedialog.askopenfilenames(filetypes=[("Jump Force Audio", "*.uexp")])
        if not file_paths:
            print("No files selected.")
            return

        # Ask user if they want to create replacement bytes
        create_choice = input("Do you want to create replacement bytes? (yes/no): ").lower().strip()
        create_bytes = create_choice == "yes"

        # Process each selected file
        for file_path in file_paths:
            process_file(file_path, create_bytes)

    os.system("pause")

if __name__ == "__main__":
    main()
