import random
import time
from selenium.webdriver.remote.webelement import WebElement

from question_service import QuestionService
from answer import AnswerType
import form_data


class FormService:
    
    def __init__(self,
                # service: Service,
                # web_driver: WebDriver,
                toggles: list[WebElement],
                text_fields: list[WebElement],
                submit: WebElement) -> None:
        # self.__service = service
        # self.__web_driver = web_driver
        self.__toggles = toggles
        self.__text_fields = text_fields
        self.__submit = submit
        self.__prev_toggle_idx = 0
    
    
    def __get_answers_indexes_for_toggles_by_question_num(self, num: int) -> dict:
    
        self.__prev_toggle_idx
        
        type = QuestionService.get_type_by_question_num(num=num)
        if type == AnswerType.TEXTFIELD: return
        
        start_idx = self.__prev_toggle_idx
        count = QuestionService.get_question_by_num(num=num).get_answers_count()
        end_idx = start_idx + count
        
        next_start_idx = end_idx
        if num in form_data.questions_with_filter: next_start_idx += 1
        
        self.__prev_toggle_idx = next_start_idx
        
        return { 
            'start': start_idx, 
            'end': end_idx 
        }


    def __get_answers_by_question_num(self, num: int) -> list[WebElement]:
        
        type = QuestionService.get_type_by_question_num(num=num)
        toggles_indexes = self.__get_answers_indexes_for_toggles_by_question_num(num=num)
        
        answers = []
        
        if (type == AnswerType.RADIOBUTTON 
            or type == AnswerType.CHECKBOX):
            answers = self.__toggles[toggles_indexes['start']:toggles_indexes['end']]
        elif type == AnswerType.TEXTFIELD:
            answers = self.__text_fields[form_data.questions_with_textfields.index(num)]
        
        return answers


    def __get_answers_on_questions(self) -> list:
        return [self.__get_answers_by_question_num(num=i + 1) for i in range(form_data.questions_count)]


    def test(self) -> None:
        
        questions = self.__get_answers_on_questions()
        
        for idx, answers in enumerate(questions):
            
            num = idx + 1
            type = QuestionService.get_type_by_question_num(num=num)
            
            print(num)
            print(str(type))
            print([i.get_text() for i in QuestionService.get_answers_by_question_num(num=num)])
            
            if (type == AnswerType.RADIOBUTTON 
                or type == AnswerType.CHECKBOX):
                for i in answers: 
                    i.click() 
                    time.sleep(1)
            elif type == AnswerType.TEXTFIELD:
                answers.send_keys('Test text')
                time.sleep(1)
                

    def __define_working_type(self, answers: list[int]) -> form_data.WorkingType:
        
        working_type = None
        
        for answer in answers:
            if answer in form_data.answers_for_working:
                working_type = form_data.WorkingType.WORKING
                break
            elif answer in form_data.answers_for_not_working:
                working_type = form_data.WorkingType.NOT_WORKING
                break
            elif answer in form_data.answers_for_retired:
                working_type = form_data.WorkingType.RETIRED
                break
        
        return working_type


    def __define_age_type(self, answer: int) -> form_data.AgeType:
        
        age_type = None
        
        if answer in form_data.answers_for_young: age_type = form_data.AgeType.YOUNG
        elif answer in form_data.answers_for_mature: age_type = form_data.AgeType.MATURE
        elif answer in form_data.answers_for_old: age_type = form_data.AgeType.OLD
        
        return age_type
        

    def __correct_random(self,
                        random_answers: list[int], 
                        question_num: int,
                        age_type: form_data.AgeType,
                        working_type: form_data.WorkingType) -> list[WebElement]:
        
        if question_num not in form_data.questions_with_age_dependency: return random_answers
        
        is_young = age_type == form_data.AgeType.YOUNG
        is_mature = age_type == form_data.AgeType.MATURE
        is_old = age_type == form_data.AgeType.OLD
        
        is_working = working_type == form_data.WorkingType.WORKING
        is_not_working = working_type == form_data.WorkingType.NOT_WORKING
        is_retired = working_type == form_data.WorkingType.RETIRED
        
        
        if is_young and is_working:
                        
            for i in random_answers:
                if i in [*form_data.answers_for_retired, 
                        *form_data.answers_for_not_working, 
                        *form_data.answers_for_mature,
                        *form_data.answers_for_old]:
                    random_answers.remove(i)
            if random_answers == []:
                random_answers = random.choices(form_data.answers_for_working)  
                            
        elif is_young and is_not_working:
            
            for i in random_answers:
                if i in [*form_data.answers_for_retired, 
                        *form_data.answers_for_working, 
                        *form_data.answers_for_mature,
                        *form_data.answers_for_old]:
                    random_answers.remove(i)
            if random_answers == []:
                random_answers = random.choices(form_data.answers_for_not_working)
                
        elif is_mature and is_working:
            
            for i in random_answers:
                if i in [*form_data.answers_for_retired, 
                        *form_data.answers_for_not_working, 
                        *form_data.answers_for_young,
                        *form_data.answers_for_old]:
                    random_answers.remove(i)
            if random_answers == []:
                random_answers = random.choices(form_data.answers_for_working)
                
        elif is_mature and is_not_working:
            
            for i in random_answers:
                if i in [*form_data.answers_for_retired, 
                        *form_data.answers_for_not_working, 
                        *form_data.answers_for_young,
                        *form_data.answers_for_old]:
                    random_answers.remove(i)
            if random_answers == []:
                random_answers = random.choices(form_data.answers_for_not_working)
                
        elif is_old and is_working:
            
            for i in random_answers:
                if i in [*form_data.answers_for_not_working,
                        *form_data.answers_for_young,
                        *form_data.answers_for_mature]:
                    random_answers.remove(i)
            if random_answers == []:
                random_answers = random.choices(form_data.answers_for_retired)
                
        elif is_old and is_not_working:
            
            for i in random_answers: 
                if i in [form_data.answers_for_working,
                        *form_data.answers_for_young,
                        *form_data.answers_for_mature]:
                    random_answers.remove(i)
            if random_answers == []:
                random_answers = random.choices(form_data.answers_for_retired)
        
        return random_answers
                

    def get_random_answers(self):
        
        questions = self.__get_answers_on_questions()
        
        age_type = None
        working_type = None
        
        for idx, answers in enumerate(questions):
            
            num = idx + 1
            type = QuestionService.get_type_by_question_num(num=num)
            
            if type == AnswerType.RADIOBUTTON:
                
                random_answer = QuestionService.get_random_answer_indexes_in_question(question_num=num)
                
                if num in form_data.questions_with_age_define:
                    age_type = self.__define_age_type(answer=random_answer)
                
                answers[random_answer].click() 
                
            elif type == AnswerType.CHECKBOX:
                
                random_answers = QuestionService.get_random_answer_indexes_in_question(question_num=num)
                
                if num in form_data.questions_with_age_dependency:
                    working_type = self.__define_working_type(answers=random_answers)
                    
                    # print('age_type: ' + str(age_type))
                    # print('working_type: ' + str(working_type))
                    
                    random_answers = self.__correct_random(random_answers=random_answers, 
                                                        question_num=num, 
                                                        age_type=age_type,
                                                        working_type=working_type)
                    # print(random_answers)
                    
                for i in random_answers: answers[i].click() 
                    
            elif type == AnswerType.TEXTFIELD:
                
                random_answer = QuestionService.get_random_answer_by_question_num(question_num=num)
                answers.send_keys(random_answer)