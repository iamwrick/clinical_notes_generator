"""
Speech Processing and Post-Processing Module

This module provides functions to process audio files, generate transcripts, and perform post-processing on the transcripts.

Functions:
    generate_transcript_from_file(file_path, soap=False, birp=False, instructions_file=None):
        Generate transcript from audio file and perform SOAP and/or BIRP post-processing.

    generate_soap_post_processing(transcript, instruction_file_path):
        Perform SOAP post-processing on the transcript.

    generate_birp_post_processing(transcript, instruction_file_path):
        Perform BIRP post-processing on the transcript.

    get_transcript(audio_path):
        Extract transcript from audio file using Automatic Speech Recognition (ASR).
"""

import os
import time
import subprocess
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

import modules.utils
from modules.model import query_bedrock_sonet
from modules.prompt_generator import generate_custom_birp_prompt, generate_custom_soap_prompt
from modules.utils import save_file

project_root = os.path.dirname(os.path.dirname(__file__))  # Navigate 2 levels up from the script directory
config_file_path = os.path.join(project_root, 'config.json')


def generate_soap_post_processing(transcript, instruction_file_path):
    """
    Perform SOAP post-processing on the given transcript.

    Args:
        transcript (str): The transcript to be processed.
        instruction_file_path (str): Path to the instruction file (optional).

    Returns:
        dict: SOAP response generated based on the transcript.
    """

    prompt = generate_custom_soap_prompt(transcript, instruction_file_path)
    soap_response = query_bedrock_sonet(prompt)
    print("SOAP note successfully generated....")

    return soap_response


def generate_birp_post_processing(transcript, instruction_file_path):
    """
    Perform BIRP post-processing on the given transcript.

    Args:
        transcript (str): The transcript to be processed.
        instruction_file_path (str): Path to the instruction file (optional).

    Returns:
        dict: BIRP response generated based on the transcript.
    """
    prompt = generate_custom_birp_prompt(transcript, instruction_file_path)
    birp_response = query_bedrock_sonet(prompt)
    print("BIRP note successfully generated....")

    return birp_response



def get_transcript(audio_path):
    """
    Extract transcript from audio file using Automatic Speech Recognition (ASR).

    Args:
        audio_path (str): Path to the audio file.

    Returns:
        str: Transcript extracted from the audio file.
    """
    print(f"Input file - {audio_path}")
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    config = modules.load_config_data(config_file_path)
    model_name = config['model_choice']
    model_id = model_name

    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
    )
    model.to(device)

    processor = AutoProcessor.from_pretrained(model_id)

    pipe = pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        max_new_tokens=128,
        chunk_length_s=30,
        batch_size=16,
        return_timestamps=True,
        torch_dtype=torch_dtype,
        device=device,
    )

    result = pipe(audio_path, generate_kwargs={"language": "english"})
    print("transcript successfully generated....")

    return result["text"]


def generate_transcript_from_file(file_path, soap=False, birp=False, instructions_file=None):
    """
    Generate transcript from audio file and perform SOAP and/or BIRP post-processing.

    Args:
        file_path (str): Path to the audio file.
        soap (bool): Perform SOAP post-processing if True (default is False).
        birp (bool): Perform BIRP post-processing if True (default is False).
        instructions_file (str): Path to the instruction file for post-processing (optional).

    Returns:
        str: Transcript extracted from the audio file.
    """
    # Start timer
    start_time = time.time()

    # Step1: Generate transcript
    transcript = get_transcript(file_path)

    # Step2: Apply SOAP, BIRP, or both post-processing steps if requested
    if soap:
        soap_notes = generate_soap_post_processing(transcript, instructions_file)
        soap_text = soap_notes['content'][0]['text']  # Extract the 'text' content from the dictionary
        save_file(soap_text, '')
        print("SOAP note saved....")

    if birp:
        birp_notes = generate_birp_post_processing(transcript, instructions_file)
        birp_text = birp_notes['content'][0]['text']  # Extract the 'text' content from the dictionary
        save_file(birp_text, '')
        print("BIRP note saved....")

    # End timer
    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Process completed in {elapsed_time:.2f} seconds.")
    return transcript
