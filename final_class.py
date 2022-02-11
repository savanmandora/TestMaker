
import random
from fpdf import FPDF


class TestMaker:
    def __init__(self, question_no, operator, test_name):
        # self.digit_system = digit_system
        self.question_no = question_no
        self.operator = operator
        self.test_name = test_name


    def __str__(self):
        return "This is Test Maker class in which you need to add required details of test and you will get your test paper in pdf format."


    def printDetails(self):
        # print(self.digit_system)
        print(self.question_no)
        print(self.operator)
        print(self.test_name)


    def makeTestForTwoDigit(self):
        lst = []
        lst_1 = []
        
        question_for_two_digit = FPDF()
        answer_for_two_digit = FPDF()

        while len(lst) <= self.question_no:
            n = random.randint(10 , 99)
            lst.append(n)

        while len(lst_1) <= self.question_no:
            n = random.randint(10 , 99)
            lst_1.append(n)
            
        question_for_two_digit.add_page()
        answer_for_two_digit.add_page()

        question_for_two_digit.set_font("Arial", size = 16)
        answer_for_two_digit.set_font("Arial", size = 16)
            
        question_for_two_digit.cell(200, 10, txt="Questions", ln=1, align="C")
        answer_for_two_digit.cell(200, 10, txt="Answers", ln=1, align="C")
        
        for i in range(0, len(lst)):
            # f.write(str(i) + "]  {} {} {} = ______ \n".format(lst[i], self.operator, lst_1[i]))
            question_for_two_digit.write(10,"{} ]  {} {} {} = _______ \n".format(i+1, lst[i], self.operator, lst_1[i]))
            

        for i in range(0, len(lst)):
            if self.operator == '+':
                ans = lst[i] + lst_1[i]
                # f.write("Ans.{} = {}\n".format(i+1, ans))
                answer_for_two_digit.write(10,"Ans.{} = {} \n".format(i+1, ans))
            
            elif self.operator == '*':
                ans = lst[i] * lst_1[i]
                answer_for_two_digit.write(10,"Ans.{} = {} \n".format(i+1, ans))
                # f.write("Ans.{} = {}\n".format(i+1, ans))
                
                
            elif self.operator == '-':
                ans = lst[i] - lst_1[i]
                answer_for_two_digit.write(10,"Ans.{} = {} \n".format(i+1, ans))
                # f.write("Ans.{} = {}\n".format(i+1, ans))
                
                
            elif self.operator == '/':
                ans = lst[i] / lst_1[i]
                answer_for_two_digit.write(10,"Ans.{} = {} \n".format(i+1, ans))
                # f.write("Ans.{} = {}\n".format(i+1, ans))
                
        question_for_two_digit.output("Questions_for_two_digit.pdf")
        answer_for_two_digit.output("Answers_for_two_digit.pdf")
            
            
    def makeTestForThreeDigit(self):
        lst = []
        lst_1 = []
        
        question_for_three_digit = FPDF()
        answer_for_three_digit = FPDF()

        while len(lst) <= self.question_no:
            n = random.randint(100 , 999)
            lst.append(n)

        while len(lst_1) <= self.question_no:
            n = random.randint(100 , 999)
            lst_1.append(n)
            
        question_for_three_digit.add_page()
        answer_for_three_digit.add_page()

        question_for_three_digit.set_font("Arial", size = 16)
        answer_for_three_digit.set_font("Arial", size = 16)
            
        question_for_three_digit.cell(200, 10, txt="Questions", ln=1, align="C")
        answer_for_three_digit.cell(200, 10, txt="Answers", ln=1, align="C")
        
        for i in range(0, len(lst)):
            # f.write(str(i) + "]  {} {} {} = ______ \n".format(lst[i], self.operator, lst_1[i]))
            question_for_three_digit.write(10,"{} ]  {} {} {} = _______ \n".format(i+1, lst[i], self.operator, lst_1[i]))
            

        for i in range(0, len(lst)):
            if self.operator == '+':
                ans = lst[i] + lst_1[i]
                # f.write("Ans.{} = {}\n".format(i+1, ans))
                answer_for_three_digit.write(10,"Ans.{} = {} \n".format(i+1, ans))
            
            elif self.operator == '*':
                ans = lst[i] * lst_1[i]
                answer_for_three_digit.write(10,"Ans.{} = {} \n".format(i+1, ans))
                # f.write("Ans.{} = {}\n".format(i+1, ans))
                
                
            elif self.operator == '-':
                ans = lst[i] - lst_1[i]
                answer_for_three_digit.write(10,"Ans.{} = {} \n".format(i+1, ans))
                # f.write("Ans.{} = {}\n".format(i+1, ans))
                
                
            elif self.operator == '/':
                ans = lst[i] / lst_1[i]
                answer_for_three_digit.write(10,"Ans.{} = {} \n".format(i+1, ans))
                # f.write("Ans.{} = {}\n".format(i+1, ans))
                
        question_for_three_digit.output("Questions_for_Three_Digit.pdf")
        answer_for_three_digit.output("Answers_for_Three_Digit.pdf")
            
            
    def makeTestForFourDigit(self):
        lst = []
        lst_1 = []
        
        question_for_four_digit = FPDF()
        answer_for_four_digit = FPDF()

        while len(lst) <= self.question_no:
            n = random.randint(1000 , 9999)
            lst.append(n)

        while len(lst_1) <= self.question_no:
            n = random.randint(1000 , 9999)
            lst_1.append(n)
            
        question_for_four_digit.add_page()
        answer_for_four_digit.add_page()

        question_for_four_digit.set_font("Arial", size = 16)
        answer_for_four_digit.set_font("Arial", size = 16)
            
        question_for_four_digit.cell(200, 10, txt="Questions", ln=1, align="C")
        answer_for_four_digit.cell(200, 10, txt="Answers", ln=1, align="C")
        
        for i in range(0, len(lst)):
            # f.write(str(i) + "]  {} {} {} = ______ \n".format(lst[i], self.operator, lst_1[i]))
            question_for_four_digit.write(10,"{} ]  {} {} {} = _______ \n".format(i+1, lst[i], self.operator, lst_1[i]))
            

        for i in range(0, len(lst)):
            if self.operator == '+':
                ans = lst[i] + lst_1[i]
                # f.write("Ans.{} = {}\n".format(i+1, ans))
                answer_for_four_digit.write(10,"Ans.{} = {} \n".format(i+1, ans))
            
            elif self.operator == '*':
                ans = lst[i] * lst_1[i]
                answer_for_four_digit.write(10,"Ans.{} = {} \n".format(i+1, ans))
                # f.write("Ans.{} = {}\n".format(i+1, ans))
                
                
            elif self.operator == '-':
                ans = lst[i] - lst_1[i]
                answer_for_four_digit.write(10,"Ans.{} = {} \n".format(i+1, ans))
                # f.write("Ans.{} = {}\n".format(i+1, ans))
                
                
            elif self.operator == '/':
                ans = lst[i] / lst_1[i]
                answer_for_four_digit.write(10,"Ans.{} = {} \n".format(i+1, ans))
                # f.write("Ans.{} = {}\n".format(i+1, ans))
                
        question_for_four_digit.output("Questions_for_four_digit.pdf")
        answer_for_four_digit.output("Answers_for_four_digit.pdf")



physics_test = TestMaker(100, '*', "Pythagoars Test")
physics_test.makeTestForTwoDigit()
# physics_test.makeTestForThreeDigit()
# physics_test.makeTestForFourDigit()