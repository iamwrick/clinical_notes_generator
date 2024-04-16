import os
import json
from datetime import datetime

def check_file(file_path):
    """
    Check if the specified file exists and has a supported file format.

    Parameters:
        file_path (str): The path to the file to be checked.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If the file format is not supported.

    Supported formats: .m4a, .mp3, .webm, .mp4, .mpga, .wav, .mpeg, .avi, .flv, .mov, .wmv
    """
    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError("File not found. Please provide a valid file path.")

    # Check file extension to ensure it's supported
    valid_extensions = ('.m4a', '.mp3', '.webm', '.mp4', '.mpga', '.wav', '.mpeg', '.avi', '.flv', '.mov', '.wmv')
    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension not in valid_extensions:
        raise ValueError("Unsupported file format. Supported formats are:", ", ".join(valid_extensions))


def load_config_data(file_path):
    """
    Load configuration from a JSON file.

    Parameters:
        file_path (str): The path to the JSON configuration file containing AWS credentials.

    Returns:
        dict: A dictionary containing AWS credentials loaded from the configuration file.

    Raises:
        FileNotFoundError: If the specified file_path does not exist.
        json.JSONDecodeError: If the file is not a valid JSON format.
    """
    with open(file_path, 'r') as file:
        config = json.load(file)
    return config


def save_file(input_text, output_dir):
    """
    Save the input text to a text file in the specified output directory.

    Parameters:
        input_text (str): The text content to be saved to the file.
        output_dir (str): The directory where the file will be saved.

    Returns:
        None

    Raises:
        OSError: If the file cannot be saved due to an operating system-related error.
    """
    # Generate filename based on current date and time
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"transcript_{current_datetime}.txt"

    # Construct full path to save file in the output directory
    file_path = os.path.join(output_dir, filename)

    try:
        # Write transcript content to text file
        with open(file_path, "w") as file:
            file.write(input_text)
    except OSError as e:
        # Raise an OSError if the file cannot be saved
        raise OSError(f"Error saving file: {e}")
