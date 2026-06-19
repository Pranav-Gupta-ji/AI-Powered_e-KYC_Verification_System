import time

from deepface import DeepFace

from app.core.logger import logger


def verify_faces(
    document_path: str,
    selfie_path: str
):

    start = time.time()

    logger.info(
        "Face verification started"
    )

    try:

        result = DeepFace.verify(
            img1_path=document_path,
            img2_path=selfie_path,
            model_name="ArcFace",
            detector_backend="opencv"
        )

        duration = round(
            time.time() - start,
            2
        )

        logger.info(
            f"Face verification completed "
            f"in {duration}s"
        )

        return result

    except Exception as e:

        logger.exception(
            f"Face verification error: {e}"
        )

        raise ValueError(
            str(e)
        )