from enum import Enum


class AnswerType(Enum):
    CHECKBOX = 1
    RADIOBUTTON = 2
    TEXTFIELD = 3


class Answer():
    
    def __init__(self, 
                text: str, 
                weight: float, 
                type: AnswerType) -> None:
        self._text = text
        self._weight = weight
        self._type = type
    
    def get_text(self) -> str: return self._text
    
    def get_weight(self) -> float: return self._weight
    
    def get_type(self) -> AnswerType: return self._type
    
    def set_text(self, text: str) -> None: self._text = text
    
    def set_weight(self, weight: float) -> None: self._weight = weight
    
    def set_type(self, type: AnswerType) -> None: self._type = type
        