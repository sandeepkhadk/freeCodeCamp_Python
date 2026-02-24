import re

# Sample medical records
medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]

def find_invalid_records(patient_id, age, gender, diagnosis, medications, last_visit_id):
    """
    Checks individual fields of a medical record against validation constraints.
    
    Returns:
        A list of keys for fields that are invalid.
    """
    constraints = {
        # patient_id must be a string and match 'P' followed by digits (case-insensitive)
        'patient_id': isinstance(patient_id, str)
                      and re.fullmatch('p\d+', patient_id, re.IGNORECASE),
        # age must be an integer and >= 18
        'age': isinstance(age, int) and age >= 18,
        # gender must be a string and either 'male' or 'female' (case-insensitive)
        'gender': isinstance(gender, str) and gender.lower() in ('male', 'female'),
        # diagnosis must be a string or None
        'diagnosis': isinstance(diagnosis, str) or diagnosis is None,
        # medications must be a list of strings
        'medications': isinstance(medications, list) and all(isinstance(i, str) for i in medications),
        # last_visit_id must be a string and match 'V' followed by digits (case-insensitive)
        'last_visit_id': isinstance(last_visit_id, str)
                         and re.fullmatch('v\d+', last_visit_id, re.IGNORECASE)
    }

    # Return keys where the constraint failed
    return [key for key, value in constraints.items() if not value]

def validate(data):
    """
    Validates a sequence of medical records.
    
    Prints error messages for invalid records and returns True if all are valid.
    
    Args:
        data: List or tuple of dictionaries, each representing a medical record.
        
    Returns:
        True if all records are valid, False otherwise.
    """
    # Ensure data is a sequence
    if not isinstance(data, (list, tuple)):
        print('Invalid format: expected a list or tuple.')
        return False

    is_invalid = False
    # Expected keys in each record
    key_set = {'patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id'}

    # Iterate over each record
    for index, dictionary in enumerate(data):
        # Check that each record is a dictionary
        if not isinstance(dictionary, dict):
            print(f'Invalid format: expected a dictionary at position {index}.')
            is_invalid = True
            continue

        # Check that dictionary contains all required keys
        if set(dictionary.keys()) != key_set:
            print(f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.')
            is_invalid = True
            continue

        # Find invalid fields
        invalid_records = find_invalid_records(**dictionary)
        for key in invalid_records:
            val = dictionary[key]
            print(f"Unexpected format '{key}: {val}' at position {index}.")
            is_invalid = True

    if is_invalid:
        return False

    print('Valid format.')
    return True

# Run validation on the sample medical records
validate(medical_records)
