from fastapi.encoders import jsonable_encoder
import unittest
from src.domain.schemas import PatientSchema
import requests

pat = {
    "resourceType": "Patient",
    "active":  True,
    "name": [
        {
        "use": "OFFICIAL",
        "family": "string",
        "given": [
            "string"
        ]
        }
    ],
    "telecom": [
        {
        "system": "PHONE",
        "value": "string",
        "use": "HOME"
        }
    ],
    "gender": "MALE",
    "birthDate": "2023-07-22T18:48:40.424Z",
    "address": [
        {
        "use": "HOME",
        "line": [
            "string"
        ],
        "city": "string",
        "district": "string",
        "state": "string",
        "postalCode": "string"
        }
    ]
}

class Patient_Test_routes(unittest.TestCase):

    def test_create_patient(self):
        patient = PatientSchema(**pat)
        response = requests.post("http://localhost:5000/api/v1/patient/", json=jsonable_encoder(patient))
        self.assertEqual(response.status_code, 201)
        self.assertIn("patient_id", response.json())

    def test_delete_patient(self):
        patient_id = "64bd562c1056150a340ef2ce"
        response = requests.delete(f"http://localhost:5000/api/v1/patient/{patient_id}")
        self.assertEqual(response.status_code, 200)

    def test_get_patients(self):
        response = requests.get("http://localhost:5000/api/v1/patient/")
        self.assertEqual(response.status_code, 200)

    def test_get_patient_by_id(self):
        patient_id = "64bd599903f4180b01f64451"
        response = requests.get(f"http://localhost:5000/api/v1/patient/{patient_id}")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()


"""def test_update_patient(self):
        patient_id = "12345"
        updated_patient = {
            "name": "John Doe",
            "age": 30,
            "gender": "Male"
        }
        
        response = requests.put(f"http://localhost:5000/api/v1/patient/{patient_id}", json=jsonable_encoder(updated_patient))
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), updated_patient)
def test_update_phone_number(self):
        phone_number = "+1234567890"
        
        response = requests.patch(f"http://localhost:5000/api/v1/patient/{phone_number}")
        
        self.assertEqual(response.status_code, 200)"""