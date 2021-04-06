from __future__ import annotations
import sqlalchemy.ext.declarative as sed


Base: sed.declarative_base = sed.declarative_base()


__all__ = (
    "Base",
)
