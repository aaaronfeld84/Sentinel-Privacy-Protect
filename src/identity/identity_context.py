from dataclasses import dataclass
from typing import Optional, Tuple

@dataclass
class IdentityContext:
    """
    The identity information the rest of the system needs.
    This is what PrivacyEngine receives.
    """
    user_id: Optional[str] = None
    authorized: bool = True
    source_trusted: bool = True
    user_face_box: Optional[Tuple[int, int, int, int]] = None


class IdentityContextBuilder:
    """
    Builds IdentityContext objects for the privacy engine.
    This does NOT replace your RBAC IdentityEngine.
    """

    def __init__(self, identity_engine):
        self.identity_engine = identity_engine

    def build(
        self,
        user_face_box: Optional[Tuple[int, int, int, int]] = None,
        source_trusted: bool = True,
    ) -> IdentityContext:

        user_id = self.identity_engine.active_user_id
        authorized = (
            user_id in self.identity_engine.authorized_users
            if user_id
            else False
        )

        return IdentityContext(
            user_id=user_id,
            authorized=authorized,
            source_trusted=source_trusted,
            user_face_box=user_face_box,
        )
