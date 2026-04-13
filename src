# src/main.py

from identity.identity_engine import IdentityEngine
from privacy_video.privacy_processor import VideoPrivacyProcessor, PrivacyOptions

def main():
    print("Sentinel Privacy Protect — System Booting")

    # Initialize identity engine
    identity = IdentityEngine()
    identity.register_user("user_001", {"role": "owner"})

    # Initialize privacy processor
    options = PrivacyOptions()
    processor = VideoPrivacyProcessor(options)

    print("System initialized successfully.")

if __name__ == "__main__":
    main()
