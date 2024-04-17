# Clinical Notes Generator

This Python project utilizes OpenAI's Whisper speech recognition model to generate transcripts from audio or video files, and then leverages Anthropic's Sonnet LLM (Large Language Model) to generate structured medical notes such as SOAP (Subjective, Objective, Assessment, Plan) or BIRP (Background, Impression, Recommendation, Plan) notes based on the transcripts.

## Features

- Generate transcripts from audio or video files using Whisper
- Prompt Anthropic's Sonnet LLM to generate SOAP or BIRP notes from the transcripts
- Customize prompts and templates for different note formats
- Save generated notes as text files

## Requirements

- Python 3.10 or higher
- OpenAI Whisper (for speech recognition) via HuggingFace
- Anthropic Sonnet LLM (for text generation) via Amazon Bedrock API
- Additional Python libraries: `boto3`, `transformers`, `torch`, `accelerate`

## Installation

1. Clone the repository:

```bash
git clone https://github.com/iamwrick/clinical_notes_generator.git
cd clinical_notes_generator
```

2. Install the required Python libraries:

```bash
pip install -r requirements.txt
```
Set up the necessary API keys and credentials for Amazon Bedrock. 
You will need additional access to Anthropic Sonnet LLM.

3. Usage:

Place your audio or video files in the input_files directory.
Run the main script: run.py
```bash
python run.py
```

3. Follow the prompts to provide the input file(s) and specify the desired note format (SOAP or BIRP). 
4. The generated notes will be saved in the output_notes directory.

## Customization
You can customize the prompt template used for generating SOAP or BIRP notes by providing a text file as input with clear instruction.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

## Acknowledgments
OpenAI Whisper for speech recognition model
Anthropic Sonnet LLM for text generation model
Python and the open-source Python community
