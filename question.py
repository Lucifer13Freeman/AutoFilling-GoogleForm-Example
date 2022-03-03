from answer import Answer


class Question():
    
    def __init__(self,
                num: int, 
                code: str,
                answers: list[Answer]) -> None:
        self._num = num
        self._code = code
        self._answers = answers
    
    def get_num(self) -> int: return self._num
    
    def get_code(self) -> str: return self._code
    
    def get_answers(self) -> list[Answer]: return self._answers
    
    def set_num(self, num) -> None: self._num = num
    
    def set_code(self, code) -> None: self._code = code
    
    def set_answers(self, answers) -> None: self._answers = answers
    
    def get_answers_texts(self) -> list[str]:
        return [i.get_text() for i in self.get_answers()]
    
    def get_answers_weights(self) -> list[float]:
        return [i.get_weight() for i in self.get_answers()]
    
    def get_answers_count(self) -> int:
        return len(self.get_answers())