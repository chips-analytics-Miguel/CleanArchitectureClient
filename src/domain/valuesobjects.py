from enum import Enum


class AdministrativeGender(Enum):
    """Administrative genstringder"""

    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"
    UNKNOWN = "UNKNOWN"


class Use(str, Enum):  # noqa: WPS600
    """Use DTO."""

    HOME = "HOME"
    WORK = "WORK"
    OTHER = "OTHER"


class UseName(str,Enum):  # noqa: WPS600
    """Usename DTO."""

    OFFICIAL = "OFFICIAL"
    OTHER = "OTHER"


class Systeme(str, Enum):  # noqa: WPS600
    """System DTO."""

    PHONE = "PHONE"
    FIXE = "FIXE"
    FAX = "FAX"
    OTHER = "OTHER"


class Gender(str, Enum):  # noqa: WPS600
    """Gender DTO."""

    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"
    UNKNOWN = "UNKNOWN"
