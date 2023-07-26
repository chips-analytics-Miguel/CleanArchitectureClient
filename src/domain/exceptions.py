from pydantic import BaseModel

class PatientException:
    class PatientNotFoundError(Exception):
        pass

    class PatientAlreadyExistError(Exception):
        pass

    class PatientContactError(Exception):
        pass

    class InvalidPatientError(Exception):
        pass
