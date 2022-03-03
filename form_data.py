from enum import Enum
# import requests


short_google_url = 'https://forms.gle/JDkJW39AuU6Hkjpq6'

google_url = 'https://docs.google.com/forms/d/e/1FAIpQLSewBS0POwfZVDgVEUe7IqH6zeMOvVvzL9SnKPsKj7DP83PXUQ'

response_url = google_url+'/formResponse'
referer_url = google_url+'/viewform'

request_url = 'https://docs.google.com/forms/d/e/1FAIpQLSewBS0POwfZVDgVEUe7IqH6zeMOvVvzL9SnKPsKj7DP83PXUQ/form'

questions = {
    1: 'entry.1332215879',
    2: 'entry.1076046327',
    3: 'entry.1898257194',
    4: 'entry.1320993062',
    5: 'entry.103335567',
    6: 'entry.159135518',
    7: 'entry.881679239',
    8: 'entry.570553175',
    9: 'entry.1899468534',
    10: 'entry.2103455286',
    11: 'entry.1239258303',
    12: 'entry.401379548',
    13: 'entry.1342769006',
    14: 'entry.1153259543',
    15: 'entry.2119916826'
}

questions_count = 15

questions_with_radiobuttons = [1, 2, 5, 6, 10, 11, 12, 13]
questions_with_checkboxes = [3, 4, 8, 9, 15]
questions_with_textfields = [7, 14]

questions_with_exception = [8]
questions_with_filter = [2, 15]

questions_with_single_answer = [*questions_with_radiobuttons, 14, 15]

questions_with_age_define = [13]
questions_with_age_dependency = [15]

answers_for_young = [0]
answers_for_mature = [1, 2, 4]
answers_for_old = [3]

class AgeType(Enum):
    YOUNG = 1,
    MATURE = 2,
    OLD = 3

answers_for_working = [1, 4]
answers_for_not_working = [2]
answers_for_retired = [3]

class WorkingType(Enum):
    WORKING = 1,
    NOT_WORKING = 2,
    RETIRED = 3

# first_radio_btn_question = 1
# first_checkbox_question = 3
# first_text_field_question = 7

# firsts = [
#     first_radio_btn_question, 
#     first_checkbox_question, 
#     first_text_field_question
# ]

answer_1_texts = [
    'Обращаюсь к частным гидам/экскурсоводам',
    'Приобретаю экскурсию в турфирме',
    'Пользуюсь аудиогидом',
    'Самостоятельно знакомлюсь с городом'
]

answer_1_weights = [
    50, 
    0,
    25,
    25
]

answer_2_texts = [
    'Обзорные',
    'Тематические',
    'Смешанные'
]

answer_2_weights = [
    70, 
    10,
    20
]

answer_3_texts = [
    'Получить новые знания',
    'Получить новые впечатления',
    'Организовать свой досуг',
    'Улучшить настроение',
    'Просто отдохнуть',
    'Пообщаться с людьми'
]

answer_3_weights = [
    0, 
    30,
    35,
    35,
    0,
    0
]

answer_4_texts = [
    'Один',
    'С семьёй',
    'Парой (любимый человек/супруг(а))',
    'С друзьями'
]

answer_4_weights = [
    25, 
    25,
    25,
    25
]

answer_5_texts = [
    'Да, удобно',
    'Нет, не удобно'
]

answer_5_weights = [
    85, 
    15
]

answer_6_texts = [
    'Да, был(а)',
    'Нет, не был(а), и не хотел(а) бы',
    'Нет, не был(а), но хотел(а) бы'
]

answer_6_weights = [
    15, 
    1,
    84
]

answer_7_texts = [
    'Италия', 
    'город',
    'порт',
    'Коллумб',
    'море',
    'Европа'
]

answer_7_weights = [
    30,
    30,
    10,
    10,
    15,
    15
]

answer_8_texts = [
    'Генуэзский Аквариум',
    'Старый порт',
    'Морской музей «Галата»',
    'Маяк Лантерна',
    'Площадь Феррари',
    'Храм Святого Лоренцо',
    'Дом Христофора Колумба',
    'Дворец Дожей',
    'Театр Карло Феличе',
    'Смотровая площадка «Биго»',
    'Никакие из перечисленных'
]

answer_8_weights = [
    5,
    5,
    4,
    4,
    6,
    4,
    6,
    6,
    6,
    4,
    50
]

answer_9_texts = [
    'Религиозные сооружения (храмы, монастыри и т.п.)', 
    'Объекты, связанные с военной историей',
    'Природные объекты',
    'Объекты, связанные с деятельность известных личностей',
    'Музеи',
    'Предприятия производства',
    'Архитектурные объекты (дворцы, памятники, монументы и т.п.)'
]

answer_9_weights = [
    30,
    0,
    0,
    20,
    10,
    0,
    40
]

answer_10_texts = [
    'Менее 2 часов',
    '2-3 часа',
    '3-4 часа',
    '5-6 часов',
    'Более 6 часов'
]

answer_10_weights = [
    0,
    70,
    30,
    0,
    0
]

answer_11_texts = [
    'Менее 50 евро', 
    '50 - 80 евро',
    '80 - 120 евро',
    'Более 120 евро'
]

answer_11_weights = [
    10,
    30,
    50,
    10
]

answer_12_texts = [
    'Мужской', 
    'Женский'
]

answer_12_weights = [
    0.5,
    0.5
]

answer_13_texts = [
    '18-25 лет', 
    '26-35 лет',
    '36-45 лет',
    '46 лет и старше'
]

answer_13_weights = [
    10,
    40,
    40,
    10
]

answer_14_texts = [
    'Ярославль', 
    'Москва',
    'Санкт-Петербург',
    'Кострома',
    'Рыбинск',
    'Вологда',
    'Череповец'
]

answer_14_weights = [
    30,
    30,
    20,
    5,
    5,
    5,
    5
]

answer_15_texts = [
    'Студент', 
    'Работающий',
    'Домохозяйка/временно неработающий(ая)',
    'Пенсионер',
    'Индивидуальный предприниматель'
]

answer_15_weights = [
    5,
    50,
    5,
    10,
    30
]

answer_texts = [
    answer_1_texts,
    answer_2_texts,
    answer_3_texts,
    answer_4_texts,
    answer_5_texts,
    answer_6_texts,
    answer_7_texts,
    answer_8_texts,
    answer_9_texts,
    answer_10_texts,
    answer_11_texts,
    answer_12_texts,
    answer_13_texts,
    answer_14_texts,
    answer_15_texts
]

answer_weights = [
    answer_1_weights,
    answer_2_weights,
    answer_3_weights,
    answer_4_weights,
    answer_5_weights,
    answer_6_weights,
    answer_7_weights,
    answer_8_weights,
    answer_9_weights,
    answer_10_weights,
    answer_11_weights,
    answer_12_weights,
    answer_13_weights,
    answer_14_weights,
    answer_15_weights
]


# form_data = {
#     'entry.881679239': 'Город, Италия',
#     'entry.1153259543': 'Ярославль',
#     'entry.1332215879': 'Обращаюсь к частным гидам/экскурсоводам',
#     'entry.1076046327': 'Обзорные',
#     'entry.1898257194': 'Получить новые знания',
#     'entry.1898257194': 'Получить новые впечатления',
#     'entry.1898257194': 'Организовать свой досуг',
#     'entry.1898257194': 'Улучшить настроение',
#     'entry.1898257194': 'Просто отдохнуть',
#     'entry.1898257194': 'Пообщаться с людьми',
#     'entry.1320993062': 'С семьёй',
#     'entry.1320993062': 'Парой (любимый человек/супруг(а))',
#     'entry.1320993062': 'С друзьями',
#     'entry.103335567': 'Да, удобно',
#     'entry.159135518': 'Нет, не был(а), но хотел(а) бы',
#     'entry.570553175': 'Никакие из перечисленных',
#     'entry.1899468534': 'Архитектурные объекты (дворцы, памятники, монументы и т.п.)',
#     'entry.2103455286': '2-3 часа',
#     'entry.1239258303': '80 - 120 евро',
#     'entry.401379548': 'Женский',
#     'entry.1342769006': '26-35 лет',
#     'entry.2119916826': 'Работающий'
# }

# print(form_data)

# user_agent = {'Referer':urlReferer,'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}
# req = requests.post(urlResponse, data=form_data, headers=user_agent)