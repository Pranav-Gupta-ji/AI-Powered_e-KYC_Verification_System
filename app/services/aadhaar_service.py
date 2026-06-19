import re

from app.core.logger import logger

# ==================================
# Aadhaar Extraction
# ==================================

def extract_aadhaar(text: str):

    patterns = [

        r"\d{4}\s\d{4}\s\d{4}",

        r"\d{4}-\d{4}-\d{4}",

        r"\d{12}"
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text
        )

        if match:

            aadhaar = re.sub(
                r"\D",
                "",
                match.group()
            )

            logger.info(
                f"Aadhaar extracted: {aadhaar}"
            )

            return aadhaar

    logger.warning(
        "Aadhaar number not found"
    )

    return None

IGNORE_WORDS = {
    "government",
    "india",
    "aadhaar",
    "authority",
    "uidai",
    "male",
    "female",
    "dob",
    "birth",
    "year",
    "of"
}


def clean_name(name):

    name = re.sub(
        r'[^A-Za-z\s]',
        ' ',
        name
    )

    name = " ".join(
        name.split()
    )

    return name.strip()


def is_valid_name(line):

    if not line:
        return False

    words = line.split()

    if len(words) < 2:
        return False

    for word in words:

        if word.lower() in IGNORE_WORDS:
            return False

    return True

def extract_kyc_details(
    text: str
):

    result = {
        "name": None,
        "dob": None,
        "gender": None
    }

    lines = [

        line.strip()

        for line in text.split("\n")

        if line.strip()
    ]

    # -----------------
    # DOB
    # -----------------

    dob_pattern = (
        r"\d{2}[/-]\d{2}[/-]\d{4}"
    )

    for i, line in enumerate(lines):

        dob_match = re.search(
            dob_pattern,
            line
        )

        if dob_match:

            result["dob"] = (
                dob_match.group()
            )

            for j in range(
                i - 1,
                -1,
                -1
            ):

                candidate = clean_name(
                    lines[j]
                )

                if is_valid_name(
                    candidate
                ):

                    result["name"] = (
                        candidate
                    )

                    break

            break

    # -----------------
    # Gender
    # -----------------

    for line in lines:

        gender_match = re.search(
            r"\b(Male|Female)\b",
            line,
            re.IGNORECASE
        )

        if gender_match:

            result["gender"] = (
                gender_match.group()
                .title()
            )

            break

    logger.info(
        f"Extracted Details: {result}"
    )

    return result