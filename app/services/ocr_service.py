import time

import easyocr

from app.core.logger import logger

# Load once at startup
reader = easyocr.Reader(["en"])


def extract_text(image_path: str) -> str:
    """
    Extract text using EasyOCR.
    """

    start = time.time()

    logger.info(
        f"Starting OCR: {image_path}"
    )

    result = reader.readtext(
        image_path,
        detail=0
    )

    text = "\n".join(result)

    duration = round(
        time.time() - start,
        2
    )

    logger.info(
        f"OCR completed in {duration}s"
    )

    return text