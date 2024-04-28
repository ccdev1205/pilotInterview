# importing required modules 
import re
from pypdf import PdfReader 
import random
  
# creating a pdf reader object 
reader = PdfReader('PilotReview.pdf') 
  
# printing number of pages in pdf file 
# print(len(reader.pages)) 
  
# input_pages = input("Enter page range (i.e 1-5): ")
def generate(input_pages):
    i_pages = input_pages.split("-")
    start_page = int(i_pages[0]) + 19
    end_page = int(i_pages[1]) + 19

    text = ""
    for page_index in range(start_page, end_page+1):
        page = reader.pages[page_index]
        text += page.extract_text() 

    questions = re.finditer(r'\s[A-Za-z\s]*\?', text)
    count = 0
    question_list = []
    for match in questions:
        count += 1
        question_list.append({match.group(): match.span()})

    q_index = 0
    question_answer = []
    for question_dict in question_list:
        for key, val in question_dict.items():
            if q_index < len(question_list):
                if(q_index + 1 < len(question_list)):
                    next_question = question_list[q_index+1]
                    for next_q_val in next_question.values():
                        question_answer.append({key: text[val[1]: next_q_val[0]]})
                else:
                    question_answer.append({key: text[val[1]: len(text)] })
        q_index += 1

    indices = list(range(len(question_answer)))
    random.shuffle(indices)

    random_questions = [question_answer[i] for i in indices]

    return random_questions;

# for qa in random_questions:
#     for key, val in qa.items():
#         showquestion = input("**show question? ")
#         if showquestion.lower() == "yes":
#             print("QUESTION: ")
#             print(key + "\n")
#             showanswer = input("**show answer? ")
#             if showanswer.lower() == "yes":
#                 print("ANSWER: ")
#                 print(val + "\n")
            