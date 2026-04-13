from dataclasses import dataclass
from typing import Optional, Tuple

import numpy as np

from .privacy_video import VideoPrivacyProcessor, PrivacyOptions


@dataclass
class RequestContext:
    """
    High-level context about the request/source/user.
    This is what the rest of the system passes in.
    """
    user_id: Optional[str] = None
    user_authorized: bool = True
    source_trusted: bool = True
    user_face_box: Optional[Tuple[int, int, int, int]] = None


class PrivacyEngine:
    """
    Orchestrates privacy enforcement for video frames.
    Other parts of the system talk to this, not directly to OpenCV.
    """

    def __init__(self, options: PrivacyOptions | None = None):
        self.options = options or PrivacyOptions()
        self.video_processor = VideoPrivacyProcessor(self.options)

    def process_video_frame(
        self,
        frame: np.ndarray,
        context: RequestContext,
    ) -> np.ndarray:
        """
        Main entry point for video privacy.
        Takes a raw frame + context, returns a privacy-safe frame.
        """

        return self.video_processor.process_frame(
            frame=frame,
            user_authorized=context.user_authorized,
            source_trusted=context.source_trusted,
            user_face_box=context.user_face_box,
        )
