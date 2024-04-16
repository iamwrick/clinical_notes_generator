import argparse

def generate_custom_birp_prompt(transcript, instructions_file=None):
    # Define the prompt template with placeholders
    prompt_template = f"""<s>[INST] 
    You are an AI assistant trained to provide resources for clinicians to document behavioral therapy sessions using the BIRP (Behavior, Intervention, Response, Plan) format based on a given transcript. 
    Your task is to generate BIRP note using the following transcript, including placeholders for each section (Behavior, Intervention, Response, Plan), but do not include any specific patient details or scenarios.
    A BIRP note is a healthcare documentation used by clinicians, therapists, and other healthcare professionals to summarize a patient's session or visit.The acronym "BIRP" stands for:
    
    Behavior: Describes the patient's observable actions or behaviors during the session.
    Intervention: Outlines the interventions or techniques used by the clinician to address the patient's needs or concerns.
    Response: Records the patient's response to the interventions or how they reacted to the session.
    Plan: Outlines the plan for future sessions or next steps in the patient's treatment or care.
    
    <Transcript>
    \n{transcript}\n
    </Transcript>
    
    Here below is an example BIRP from a patient encounter. The output should be exactly like the example but based of the input transcript.
    <example>
    BIRP Note

    Patient Name: John Doe
    Date of Session: April 12, 2024
    Therapist: Dr. Smith
    
    Behavior:
    During today's session, John appeared restless and anxious, frequently tapping his foot and avoiding eye contact. He expressed feeling overwhelmed by work-related stressors and reported difficulty sleeping due to racing thoughts.
    
    Intervention:
    Utilized deep breathing exercises and guided imagery to help John relax and reduce his anxiety levels. Discussed cognitive-behavioral techniques for managing stress, including identifying and challenging negative thought patterns.
    
    Response:
    John responded positively to the relaxation exercises, reporting a decrease in muscle tension and a sense of calmness. He engaged actively in the discussion of stress management strategies and expressed willingness to practice techniques outside of therapy sessions.
    
    Plan:
    Agreed to continue practicing relaxation techniques daily and to monitor stress levels using a mood journal. Scheduled a follow-up appointment in two weeks to assess progress and further refine coping skills. Provided resources for additional support, including online stress management workshops and relaxation apps.
    
    </example> 
    """

    # Add instructions from file if provided
    if instructions_file:
        with open(instructions_file, "r") as file:
            instructions = file.read()
        prompt_template += instructions + "\n"
    else:
        prompt_template += "Special Instructions-\n"

    prompt_template += """In your example, include details that align with the information provided in the transcript, such as observable behaviors, therapeutic interventions used, client responses, and proposed plans. However, do not disclose any specific patient details beyond what is stated in the transcript itself.  

    Throughout your response, ensure the following:
    - Do not provide generic examples. Use the Transcript and provide crisp response for each section in the BIRP Note.
    - Use terminology consistent with behavioral therapy and mental health practices.
    - Emphasize the importance of maintaining confidentiality and compliance with ethical guidelines and regulations.
    [/INST]"""

    #print(prompt_template)
    return prompt_template


def generate_custom_soap_prompt(transcript, instructions_file=None):
    prompt_template = f"""<s>[INST]
    Please write a SOAP note for a patient encounter based on the following information and the provided transcript below:

    - Subjective (S): Describe the patient's chief complaint(s), symptoms, and relevant history in their own words.
    
    - Objective (O): Document your observations, including vital signs, physical examination findings, and any relevant test results.
    
    - Assessment (A): Provide your analysis of the patient's condition, including potential diagnoses or differential diagnoses.
    
    - Plan (P): Outline your treatment plan, including any medications prescribed, follow-up instructions, referrals, or additional tests ordered.
    
    Please follow the SOAP format and provide a comprehensive yet concise note.
    """

    # Add instructions from file if provided
    if instructions_file:
        with open(instructions_file, "r") as file:
            instructions = file.read()
        prompt_template += instructions + "\n"
    else:
        prompt_template += "Special Instructions-\n"

    prompt_template +=f"""    
    Additional information you may want to include:
    
    
    Patient's name, age, and gender
    Relevant medical history, including allergies and current medications
    Timing and duration of symptoms
    Pertinent positive and negative findings from the physical exam
    Diagnostic test results (if available)
    Rationale for your assessment and treatment plan
    Remember to maintain confidentiality by avoiding the use of identifiable patient information.
    
    <Transcript>
    \n{transcript}\n
    </Transcript>
    
    You may refer to the following SOAP note as an example while generating one with the provided transcript - 
    
    <example>
    Subjective (S): Mrs. Jane Doe, a 68-year-old female, presents with a 3-day history of severe abdominal pain, nausea, and vomiting. She reports the pain started suddenly and is located in the right lower quadrant of her abdomen. She has had no bowel movements for the past 2 days.

    Objective (O): Vital signs: Temperature 101.2°F, Blood Pressure 142/88 mmHg, Pulse 96 bpm, Respiratory Rate 18 breaths/min. Physical exam reveals a soft, distended abdomen with marked tenderness and guarding in the right lower quadrant. Bowel sounds are hypoactive. No masses are palpated.
    
    Assessment (A): Acute appendicitis is the leading diagnosis based on the patient's symptoms, physical exam findings, and fever. The differential diagnosis includes diverticulitis, bowel obstruction, or ovarian pathology.
    
    Plan (P): 1. Obtain CT scan of the abdomen and pelvis with IV contrast to confirm the diagnosis and rule out other causes.
    2. Start IV fluids and keep NPO (nothing by mouth).
    3. Administer IV antibiotics (cefoxitin and metronidazole) to cover for potential appendiceal perforation.
    4. Consult general surgery for possible appendectomy.
    5. Provide analgesics (morphine) for pain control.
    6. Admit to hospital for observation and further management.


    </example>
   
    [/INST]
"""
    return prompt_template
