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

def main():
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        # Prompt the user to select the .uexp file using file explorer dialog
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(filetypes=[("Jump Force Audio", "*.uexp")])
        if not file_path:
            print("No file selected.")
            return

    start_marker = "AFS2"
    start_offset = 0

    try:
        extracted_data = extract_data(file_path, start_marker, start_offset)
        output_file = file_path + ".awb"
        with open(output_file, 'wb') as file:
            file.write(extracted_data)
        print("Audio extraction completed! Output file:", output_file)

        # Open the destination file in another file explorer window
        os.startfile(os.path.dirname(output_file))

    except FileNotFoundError:
        print("Error: File not found. Please provide a valid file path.")
    except ValueError as ve:
        print("Error:", str(ve))
    except Exception as e:
        print("An error occurred during audio extraction:", str(e))

    os.system("pause")

if __name__ == "__main__":
    main()
