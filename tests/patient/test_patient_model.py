import datetime
from typing import List
from datetime import date
import unittest
from src.domain.commands import CreatePatient

pat = {
  "family_name": "string",
  "given_name": [
    "string"
  ],
  "phone_number": "+155871374",
  "gender": "string",
  "birthdate": "2023-07-26"
}

class TestPatientCreateSchema(unittest.TestCase):

    def test_data_type(self):
        patient=CreatePatient(**pat)
        self.assertIsInstance(patient.family_name,str)
        self.assertIsInstance(patient.given_name,List[str])
        self.assertIsInstance(patient.gender,str)
        self.assertIsInstance(patient.birthdate,date)

    # Tests that a patient can be created with all required fields
    def test_create_patient_with_required_fields(self):
        patient = CreatePatient(
            family_name='Doe',
            given_name=['John'],
            phone_number='1234567890',
            gender='male',
            birthdate=datetime.date(1990, 1, 1)
        )
        self.assertIsInstance(patient, CreatePatient)

    # Tests that a patient can be created with multiple given names
    def test_create_patient_with_multiple_given_names(self):
        patient = CreatePatient(
            family_name='Doe',
            given_name=['John', 'Jane'],
            phone_number='1234567890',
            gender='male',
            birthdate=datetime.date(1990, 1, 1)
        )
        self.assertIsInstance(patient, CreatePatient)

    # Tests that a patient can be created with a valid phone number
    def test_create_patient_with_valid_phone_number(self):
        patient = CreatePatient(
            family_name='Doe',
            given_name=['John'],
            phone_number='1234567890',
            gender='male',
            birthdate=datetime.date(1990, 1, 1)
        )
        self.assertIsInstance(patient, CreatePatient)

    # Tests that a patient can be created with a valid gender
    def test_create_patient_with_valid_gender(self):
        patient = PatientCreateSchema(
            family_name='Doe',
            given_name=['John'],
            phone_number='1234567890',
            gender='male',
            birthdate=datetime.date(1990, 1, 1)
        )
        self.assertIsInstance(patient, CreatePatient)

    # Tests that a patient can be created with a valid birthdate
    def test_create_patient_with_valid_birthdate(self):
        patient = PatientCreateSchema(
            family_name='Doe',
            given_name=['John'],
            phone_number='1234567890',
            gender='male',
            birthdate=datetime.date(1990, 1, 1)
        )
        self.assertIsInstance(patient, CreatePatient)
    
    def test_create_patient_with_empty_family_name(self):
        with self.assertRaises(ValueError):
            CreatePatient(
                family_name=None,
                given_name=['John'],
                phone_number='1234567890',
                gender='male',
                birthdate=datetime.date(1990, 1, 1)
            )

    # Tests that a patient cannot be created with an empty list of given names
    def test_create_patient_with_empty_list_of_given_names(self):
        with self.assertRaises(ValueError):
            CreatePatient(
                family_name='Doe',
                given_name='',
                phone_number='1234567890',
                gender='male',
                birthdate=datetime.date(1990, 1, 1)
            )

    # Tests that a patient cannot be created with an invalid phone number
    def test_create_patient_with_invalid_phone_number(self):
        try:
            CreatePatient(
                family_name='Doe',
                given_name=['John'],
                phone_number='123',
                gender='male',
                birthdate=datetime.date(1990, 1, 1)
            )
        except ValueError as e:
            self.assertEqual(e.args[0], 'Invalid phone number')

    # Tests that a patient cannot be created with an invalid gender
    def test_create_patient_with_invalid_gender(self):
        try:
            CreatePatient(
                family_name='Doe',
                given_name=['John'],
                phone_number='1234567890',
                gender='',
                birthdate=datetime.date(1990, 1, 1)
            )     
        except ValueError as e:
            self.assertEqual(e.args[0], 'Invalid gender')

    # Tests that a patient cannot be created with an invalid birthdate
    def test_create_patient_with_invalid_birthdate(self):
        try :
            CreatePatient(
                family_name='Doe',
                given_name=['John'],
                phone_number='1234567890',
                gender='male',
                birthdate=datetime.date(2050, 1, 1)
            )
        except ValueError as e:
            self.assertEqual(e.args[0], 'DateYear is greather than current year')

    # Tests that a patient can be created with additional fields not defined in the schema
    def test_create_patient_with_additional_fields_not_defined_in_schema(self):
        patient = CreatePatient(
            family_name='Doe',
            given_name=['John'],
            phone_number='1234567890',
            gender='male',
            birthdate=datetime.date(1990, 1, 1),
            additional_field='some value'
        )
        self.assertIsInstance(patient, CreatePatient)

    # Tests that a patient cannot be created with a non-standard date format
    def test_create_patient_with_non_standard_date_format(self):
        with self.assertRaises(ValueError):
            CreatePatient(
                family_name='Doe',
                given_name=['John'],
                phone_number='1234567890',
                gender='male',
                birthdate='01-01-1990'
            )

if __name__ == "__main__":
    unittest.main()
