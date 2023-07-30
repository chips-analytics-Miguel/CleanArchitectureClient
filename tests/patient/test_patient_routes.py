from fastapi.encoders import jsonable_encoder
import unittest
from src.domain.commands import CreatePatient
import requests

pat = {
  "family_name": "string",
  "given_name": [
    "string"
  ],
  "phone_number": "string",
  "gender": "string",
  "birthdate": "2023-07-26"
}

class Patient_Test_routes(unittest.TestCase):

    def test_create_patient(self):
        patient = CreatePatient(**pat)
        response = requests.post("http://localhost:5000/api/v1/patient/", json=jsonable_encoder(patient))
        self.assertEqual(response.status_code, 201)
        self.assertIn("patient_id", response.json())

    def test_delete_wrong_patient_id(self):
        patient_id = "64c20cfbaf71d882a704a90b"
        response = requests.delete(f"http://localhost:5000/api/v1/patient/{patient_id}")
        self.assertEqual(response.status_code, 400)

    def test_get_patients(self):
        response = requests.get("http://localhost:5000/api/v1/patient/")
        self.assertEqual(response.status_code, 200)

    def test_get_patient_by_id(self):
        patient_id = "64c14c315cd4506667f61b86"
        response = requests.get(f"http://localhost:5000/api/v1/patient/{patient_id}")
        self.assertEqual(response.status_code, 200)
    
    def test_get_patient_by_wrong_id(self):
        patient_id ="64c20cfbaf71d882a704a90b"
        response = requests.get(f"http://localhost:5000/api/v1/patient/{patient_id}")
        self.assertEqual(response.status_code, 400)

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