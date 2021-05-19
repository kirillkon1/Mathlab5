from abc import ABC, abstractmethod


class AbstractMethod(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def begin(self, dots: list, num) -> float:
        pass
