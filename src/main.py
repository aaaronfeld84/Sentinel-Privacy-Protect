from identity.identity_engine import IdentityEngine
from identity.identity_context import IdentityContextBuilder
from privacy.privacy_engine import PrivacyEngine

import cv2


def main():
    # --- SETUP ---
    identity = IdentityEngine()
    identity.register_user("user123")
    identity.set_active_user("user123")

    context_builder = IdentityContextBuilder(identity)
    privacy_engine = PrivacyEngine()

    # --- LOAD A TEST FRAME (placeholder) ---
    frame = cv2.imread("test_frame.jpg")  # Replace with real frame later

    # --- BUILD CONTEXT ---
    context = context_builder.build(
        user_face_box=None,       # Replace with real face box later
        source_trusted=True
    )

    # --- PROCESS FRAME ---
    safe_frame = privacy_engine.process_video_frame(frame, context)

    # --- SAVE OUTPUT ---
    cv2.imwrite("output_frame.jpg", safe_frame)
    print("Privacy‑processed frame saved as output_frame.jpg")


if __name__ == "__main__":
    main()
