import cv2
import numpy as np
from dataclasses import dataclass

@dataclass
class PrivacyOptions:
    blur_user_face: bool = True
    blur_all_faces: bool = True
    blur_license_plates: bool = True
    blur_if_unauthorized: bool = True
    blur_everything_for_untrusted_source: bool = True

class VideoPrivacyProcessor:
    """
    Frame-level privacy processor.
    You pass in a frame (OpenCV BGR image) and flags about the context,
    and it returns a privacy-safe frame.
    """

    def __init__(self, options: PrivacyOptions | None = None):
        self.options = options or PrivacyOptions()

        # Use OpenCV's built-in Haar cascades
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )
        self.plate_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_russian_plate_number.xml"
        )

    def _blur_region(self, frame, x, y, w, h):
        region = frame[y:y+h, x:x+w]
        blurred = cv2.GaussianBlur(region, (51, 51), 0)
        frame[y:y+h, x:x+w] = blurred
        return frame

    def process_frame(
        self,
        frame: np.ndarray,
        user_authorized: bool = True,
        source_trusted: bool = True,
        user_face_box: tuple | None = None,
    ) -> np.ndarray:

        # Reject invalid frames
        if frame is None or not hasattr(frame, "shape"):
            return frame

        # Blur everything if source is untrusted
        if self.options.blur_everything_for_untrusted_source and not source_trusted:
            return cv2.GaussianBlur(frame, (99, 99), 0)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        plates = self.plate_cascade.detectMultiScale(gray, 1.3, 5)

        # Blur everything if user is unauthorized
        if self.options.blur_if_unauthorized and not user_authorized:
            return cv2.GaussianBlur(frame, (99, 99), 0)

        # Blur user's own face
        if self.options.blur_user_face and user_face_box:
            x, y, w, h = user_face_box
            frame = self._blur_region(frame, x, y, w, h)

        # Blur all faces
        if self.options.blur_all_faces:
            for (x, y, w, h) in faces:
                frame = self._blur_region(frame, x, y, w, h)

        # Blur license plates
        if self.options.blur_license_plates:
            for (x, y, w, h) in plates:
                frame = self._blur_region(frame, x, y, w, h)

        return frame
