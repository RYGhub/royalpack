from __future__ import annotations
from ._imports import *


class Rage(Base):
    __tablename__ = "rage"

    id = s.Column(s.Integer, primary_key=True)

    reason = s.Column(s.Text, nullable=False)


__all__ = (
    "Rage",
)
