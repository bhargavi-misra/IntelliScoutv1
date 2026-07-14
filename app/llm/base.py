from abc import ABC, abstractmethod


class BaseLLM(ABC):

    @abstractmethod
    def generate(self, system: str, user: str) -> str:
        pass