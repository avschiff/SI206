# Your name: Avery Schiff
# Your student id: 35947681
# Your email: avschiff@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT): some ChatGPT
# If you worked with generative AI also add a statement for how you used it.  
"""
I asked ChatGPT for help when I was unsure of where to go next or when I had an issue debugging code.
For example, I used ChatGPT to create line 92 because I was not sure how to create that line. I tried
using a for loop but it was not working so I asked AI and studied its output! I also used it to debug
when one of my tests did not work. I found out that if I changed the question in the test, it would work.
This is likely because previous tests were interfering with that test. I have indicated the locations I used
ChatGPT in my code.
"""

import random

# create a Digital Book of Answers
class DigitalBookofAnswers():

    # create the constructor (__init__) method 
    # ARGUMENTS: 
    #       self: the current object
    #       answers: a list of potential answers
    # RETURNS: None
    def __init__(self, answers):
        self.book_answer_list = answers
        self.questions_asked_list = []
        self.answered_list = []

    # Create the __str__ method
    # ARGUMENTS: 
    #       self: the curent object
    # RETURNS: a string
    def __str__(self):
        if self.book_answer_list:
            return " - ".join(self.book_answer_list)
        else:
            return ""
        
    # Creates the check_get_answer method
    # ARGUMENTS:
    #       self: the current object
    #       question: the question the user wants to ask the digital book of answers
    # RETURNS: a string
    def check_get_answer(self, question):
        if question in self.questions_asked_list:
            answer_index = self.questions_asked_list.index(question) #used ChatGPT to learn .index
            if answer_index < len(self.answered_list):
                answer = self.book_answer_list[self.answered_list[answer_index]]
                return f"I've already answered this question. The answer is: {answer}"
            else:
                return "Error: Unable to retrieve the answer."
        
        if not self.book_answer_list:
            return "The book of answers is empty. No answers available."

        answer_index = random.randint(0, len(self.book_answer_list) - 1) #got help from ChatGPT for this
        answer = self.book_answer_list[answer_index]

        self.questions_asked_list.append(question)
        self.answered_list.append(answer_index)

        return answer

    # Creates open_book method
    # ARGUMENTS:
    #   self: the current object
    # RETURNS: None
    def open_book(self):
        turn = 1
        while True:
            question = input(f"Turn {turn} - Please enter your question: ")
            if question == "Done":
                print("Goodbye! See you soon.")
                break
            answer = self.check_get_answer(question)
            print(answer)
            turn += 1

    # Create the answer_log method
    # ARGUMENTS: 
    #       self: the curent object
    # RETURNS: a list
    def answer_log(self):
        if not self.answered_list:
            return []

        answer_count = {}
        for index in self.answered_list:
            answer = self.book_answer_list[index].lower()
            if answer in answer_count:
                answer_count[answer] += 1
            else:
                answer_count[answer] = 1

        sorted_log = sorted([f"{count} - {answer}" for answer, count in answer_count.items()], reverse=True) #used ChatGPT to help write this line
        return sorted_log

def test():
    answers_list = ['Believe in Yourself', 'Stay Open to the Future', 'Enjoy It']
    book = DigitalBookofAnswers(answers_list)

    print("Test __init__:")
    print(f"Answer History List: Expected: {[]}, Actual: {book.answered_list}")
    print(f"Question History List: Expected: {[]}, Actual: {book.questions_asked_list}")
    print(" ")

    print("Test __str__:")
    expected = "Belive in Yourself - Stay Open to the Future - Enjoy It"
    print(f"Expected: {expected}, Actual: {str(book)}")
    print(" ")
    
    empty_book = DigitalBookofAnswers([])
    print("Test __str__: when it's an empty book without possible answers")
    expected = ""
    print(f"Expected: {expected}, Actual: {str(empty_book)}")
    print(" ")

    print("Testing return value of check_get_answer:")
    res = book.check_get_answer('test question')
    print(f"Expected: {str}, Actual: {type(res)}")
    print(" ")

    print("Testing check_get_answer")
    book.book_answer_list = ['Go For It']
    res = book.check_get_answer('test question 2')
    print(f"Expected: {'Go For It'}, Actual: {res}")
    print(" ")

    # THIS TEST WAS ACTING WEIRD FOR ME SO I CHANGED THE QUESTION FROM "TEST QUESTION 2" TO "TEST QUESTION 2.5"
    print("Testing that check_get_answer adds answer index to answered_list:")
    book.book_answer_list = ['Go For It']
    book.answered_list = []
    book.check_get_answer('test question 2.5')
    expected = [0]
    res = book.answered_list
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")

    print("Testing that check_get_answer does not add 'I've already answered this question' part to answered_list:")
    book.book_answer_list = ['Believe In Yourself']
    book.answered_list = [0]
    book.questions_asked_list = ['test question 3']
    book.check_get_answer('test question 3')
    expected = [0]
    res = book.answered_list
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")

    print("Testing return value answer_log")
    book.book_answer_list = ['Follow Your Inner Voice', 'Stay Positive', 'Go For It']
    book.answered_list = [0, 0, 0, 1, 1, 2]
    res = type(book.answer_log())
    print(f"Expected: {list}, Actual: {res}")
    print(" ")

    print("Testing return value answer_log elements")
    book.answered_list = [0, 0, 0, 1, 1, 2]
    res = type(book.answer_log()[0])
    print(f"Expected: {str}, Actual: {res}")
    print(" ")

    print("Testing answer_log")
    book.answered_list = [0, 0, 0, 1, 1, 2]
    res = book.answer_log()
    expected = ['3 - follow your inner voice', '2 - stay positive', '1 - go for it']
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")

    print("Testing empty answer_log")
    book.answered_list = []
    res = book.answer_log()
    expected = []
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")

# Extra Credit
def my_test():
    answers_list = ['Yes', 'No', 'Maybe']
    book = DigitalBookofAnswers(answers_list)
    
    print("Testing type for 'Will it be sunny tomorrow?'")
    res = book.check_get_answer('Will it be sunny tomorrow?')
    print(f"Expected: <class 'str'>, Actual: {type(res)}")
    print(" ")

    print("Testing 'Will it be sunny tomorrow?'")
    expected = ['Yes', 'No', 'Maybe']
    print(f"Expected to be one of {expected}, Actual: {res}")
    print(" ")

    answers_list = []
    book = DigitalBookofAnswers(answers_list)

    print("Testing when the book is empty")
    res = book.check_get_answer('simple test question')
    print(f"Expected: The book of answers is empty. No answers available., Actual: {res}")
    print(" ")

def main():
    answers_list = ['Believe in Yourself', 'Stay Open to the Future', 'Enjoy It', 'Follow Your Inner Voice', 'Stay Positive', 'Go For It']
    book = DigitalBookofAnswers(answers_list)
    
    print("Book Answers:")
    print(book)
    
    book.open_book()
    
    print("Answer Log:")
    print(book.answer_log())

# Only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    test() 
    my_test() #TODO: Uncomment if you do the extra credit
    main()

    