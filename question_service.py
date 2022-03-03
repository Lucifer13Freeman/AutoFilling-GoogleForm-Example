import random
import form_data
from answer import Answer, AnswerType
from question import Question


class QuestionService():
    
    @staticmethod
    def get_type_by_question_num(num: int) -> AnswerType:
        
        if (num in form_data.questions_with_radiobuttons): 
            return AnswerType.RADIOBUTTON
        elif (num in form_data.questions_with_checkboxes): 
            return AnswerType.CHECKBOX
        else: 
            return AnswerType.TEXTFIELD
    
    
    @staticmethod
    def get_answers_by_question_num(num: int) -> list[Answer]:
        
        if len(form_data.answer_weights) != len(form_data.answer_weights): return
        
        type = QuestionService.get_type_by_question_num(num=num)
        
        answers = []
        
        for i in range(len(form_data.answer_texts[num - 1])):
            answers.append(Answer(text=form_data.answer_texts[num - 1][i],
                                    weight=form_data.answer_weights[num - 1][i],
                                    type=type))
        return answers


    @staticmethod
    def get_question_by_num(num: int) -> Question:
        
        code = form_data.questions[num]
        answers = QuestionService.get_answers_by_question_num(num=num)
        return Question(num=num, code=code, answers=answers)


    @staticmethod
    def get_random_answer_by_question_num(question_num: int) -> list[Answer] | str:
        
        type = QuestionService.get_type_by_question_num(num=question_num)
        
        question = QuestionService.get_question_by_num(num=question_num)
        answers = question.get_answers()
        answer_weights = question.get_answers_weights()
        
        count = (1 if question_num in form_data.questions_with_single_answer 
                    else random.randrange(start=1, stop=len(answers)))
        random_answers = list(set(random.choices(answers, weights=answer_weights, k=count)))
        
        if question_num in form_data.questions_with_exception:
            
            question = QuestionService.get_question_by_num(num=question_num)
            length = len(question.get_answers())
            answer = question.get_answers()[length - 1]
            
            if random_answers[0].get_text() == answer.get_text():
                random_answers = [random_answers[0]]
            else:
                random_answers = [i for i in random_answers if i.get_text() != answer.get_text()]
                            
        return (random_answers 
                if type != AnswerType.TEXTFIELD 
                else str([i.get_text() for i in random_answers]).strip('[]').replace("'", ''))


    @staticmethod
    def get_answer_indexes_in_question(answers: list[Answer], 
                                       question_num: int, 
                                       type: AnswerType | None = None) -> list | int:
        
        type = QuestionService.get_type_by_question_num(num=question_num) if type == None else type
        question = QuestionService.get_question_by_num(num=question_num)
        indexes = [question.get_answers_texts().index(i.get_text()) for i in answers]
        return indexes if type == AnswerType.CHECKBOX else indexes[0]


    @staticmethod
    def get_random_answer_indexes_in_question(question_num: int) -> list | int:
        
        type = QuestionService.get_type_by_question_num(num=question_num)
        if type != AnswerType.RADIOBUTTON and type != AnswerType.CHECKBOX: return
        
        random_answers = QuestionService.get_random_answer_by_question_num(question_num=question_num)
        return QuestionService.get_answer_indexes_in_question(answers=random_answers, question_num=question_num)


    @staticmethod
    def test():
        
        for i in range(form_data.questions_count):
            
            num = i + 1
            type = QuestionService.get_type_by_question_num(num=num)
            
            if type == AnswerType.RADIOBUTTON or type == AnswerType.CHECKBOX:
                print(QuestionService.get_random_answer_indexes_in_question(question_num=num))
            elif type == AnswerType.TEXTFIELD:
                print(QuestionService.get_random_answer_by_question_num(question_num=num))
                