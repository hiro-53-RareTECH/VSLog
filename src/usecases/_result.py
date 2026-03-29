from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar('T')

@dataclass(frozen=True)
class Result(Generic[T]):
    ok: bool
    message: str = ''
    value: Optional[T] = None

    @staticmethod
    def success(value: Optional[T] = None) -> Result[T]:
        return Result(ok=True, value=value)
    
    @staticmethod
    def failure(message: str) -> Result[T]:
        return Result(ok=False, message=message)
