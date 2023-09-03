## UEXPtoAWB - How it works

**TLDR**: In summary, UEXPtoAWB simplifies the extraction of audio data from UEXP files in Jump Force. It does so by locating the "ASF2" marker, extracting audio data, and creating AWB files. Developers and modders can use this tool to work more efficiently with Jump Force audio data, without the need for manual hex data manipulation.

Below is a step-by-step explanation of how the script functions:


**1. Locating the Start of Audio Data (ASF2):**
- The script searches for the "ASF2" marker within the binary data. This marker indicates the beginning of the audio data.
- Once the "ASF2" marker is found, the script identifies its position in the file.

**3. Extracting Audio Data:**
- With the position of the "ASF2" marker known, the script extracts the audio data starting from that point.
- This extraction includes all data from the "ASF2" marker to the end of the file.

**4. Creating an AWB File:**
- After successfully extracting the audio data, the script proceeds to create an AWB file.
- The AWB file format is suitable for use with tools such as Eternity Audio Tool.
- The script writes the extracted audio data into the newly created AWB file.

**5. Optional Backup (Replacement Bytes):**
- UEXPtoAWB provides an optional feature to create a backup of the data prior to the "ASF2" marker. This data is essentially the portion of the UEXP file before the audio data.
- This backup can be useful for preserving the original data in case it is needed for any reason.

**6. User Interaction:**
- The script offers two modes of operation:
  - **Drag and Drop Mode:** Users can simply drag a UEXP file onto the script's executable or Python script file. This initiates the extraction process, and users receive feedback upon completion.
  - **Opening the Program:** Users can run the script directly and select a UEXP file through a file dialog. The script then processes the selected file and provides feedback.



