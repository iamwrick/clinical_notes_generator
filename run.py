"""
Generate SOAP and/or BIRP notes based on an audio file transcript.

Usage:
1. Run the script.
2. Enter the path to the audio file.
3. Specify whether SOAP notes are desired (yes/no).
4. Specify whether BIRP notes are desired (yes/no).
5. Optionally, provide the path to an instruction file for additional guidance.
6. The script will generate and print SOAP and/or BIRP notes based on the provided transcript.

Note:
- SOAP notes stand for Subjective, Objective, Assessment, and Plan notes.
- BIRP notes stand for Behavior, Intervention, Response, and Plan notes.

Output:
- The transcript is displayed in the console. You may use it for further processing.
- The SOAP and/or BIRP notes are saved as file in the local directory
"""

# Importing necessary functions from custom modules
from modules import generate_transcript_from_file
from modules.utils import check_file

# Prompting user for file path and preferences
file_path = input("Enter the file path: ")
soap_preference = input("Do you want SOAP notes? (yes/no): ").lower() == "yes"
birp_preference = input("Do you want BIRP notes? (yes/no): ").lower() == "yes"
instruction_file_path = input("Enter the path to the instruction file (leave blank if none): ").strip()

try:
    # Check if the provided file exists
    check_file(file_path)

    # Generate transcript and SOAP/BIRP notes based on preferences
    transcript = generate_transcript_from_file(file_path, soap=soap_preference, birp=birp_preference,
                                               instructions_file=instruction_file_path)

    # Print the generated transcript or notes
    print(transcript)
except Exception as e:
    # Print error message if an exception occurs
    print("Error:", e)