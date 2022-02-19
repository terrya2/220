"""
Autumn Terry
hw5.py
Creating codes with the use of string and list methods.
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    name = str(input("enter a name (first last): "))
    name.split(" ")
    first_name = name[0]
    last_name = name[1]
    print(last_name, ",", first_name)

    name_reverse()



def company_name():
    domain = str(input("enter a domain: "))
    print(domain.split("."))

    company_name()

def initials():
    num_students = str(input("how many students are in the class? "))
    sum = 0
    for student in range (num_students):
        sum = sum + num_students
        name_student = str(input("what is the name of student", num_students + 1))
        print(name_student[0])

    initials()

def names():
    list_names = str(input("enter a list of names: "))
    print(list_names[0])

    names()


def thirds():
   num_sentences = str(input("enter the number of sentences: "))
   sum = 0
   for sentences in range(num_sentences):
    sum = sum + num_sentences
    sentence = str(input("enter sentence", sentences + 1))
    ans = sentence[0:3]
    print(ans)

    thirds()

def word_average():
    words = 0
    sentence = str(input("enter a sentence: "))
    for words in range (sentence):
        sum = words + 1
        print(len(sentence) / sum)

    word_average()


def pig_latin():
    sum = 0
    text = str(input("enter a sentence to convert to pig latin: "))
    for word in text():
        pig =  word[0] + "ay"
        print(pig)
    pig_latin()


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
