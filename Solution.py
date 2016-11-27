import foobar
import csv
import unittest
from math import sqrt


class ChildFoo(foobar.FoobarClass):

    def __init__(self, file_read):
        self.students = []
        self.emails = []
        self.card_labels = []
        self.scores = []
        self.file_read = file_read
        self.name = "ChildFoo"
        self.code_map = {'A1': 'a', 'A2': 'b', 'A3': 'c', 'A4': 'd', 'A5': 'e', 'A6': 'f', 'A7': 'g'}
        self.answer = 'abcdefg'
        self.max_score = 28

    def read_data_child(self):
        """
        To Read CSV file
        :return:
        """

        list1=[]

        reader = csv.reader(self.file_read)

        for row in reader:
            self.students.append(row)

        # Prepare two list for email and card_label
        for i in range(len(self.students)):
            student = self.students[i]
            stu_length = len(student) -1
            #print("student len :",+stu_length)
            chk_eml = student[stu_length]
            # print("email chk :",chk_eml)

            if chk_eml in self.emails :

                pass

            else:
                list2 = []
                for j in range(len(student)):
                   #print("j:",j)
                  if j < stu_length:
                    #self.card_labels.append(student[j])
                    #print("card lables :",self.card_labels)
                    list2.append(student[j])
                    #print("list 2:",list2)
                  else:
                    self.emails.append(student[j])

                    #print("card email :", self.emails)
                       #list1.append(list2)

                # print("full list 2 :",list2)
                list1.append(list2)
            # print("list 1:",list1)
        # Distribute list in the chunk of 5
        #self.card_labels = self.split_list(self.card_labels, 5)
        self.card_labels = list1
        # print("card label list :",self.card_labels)

       # print("split list :",self.card_labels)
        # print("email ids :",self.emails)
    def compute_score(self):
        """
        To compute score for each card_label
        The output format of the csv file will be:
        <student id>, <score>
        :return:
        """
        scores = []
        for card_label in self.card_labels:
            answer_string = self.transform_card_order_to_string(card_label)

            incorrect_cards = self.levenshtein_score(answer_string)
            print("Incorect cards are:",incorrect_cards)
            #correct_cards = len(self.code_map) - incorrect_cards
            correct_cards = len(card_label) - incorrect_cards

           # print("correct card :",+correct_cards)
            #print("incorrect card:",incorrect_cards)
            score = (correct_cards * 4) - (incorrect_cards * 2)
            scores.append(score)
            print("score is:",score)
        self.scores = scores

    def write_student_scores(self):
        """
        To write score in CSV file
        :return:
        """
        #print("in file write : ",self.emails)
        with open('results.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            i = 0
            for score in self.scores:
                percent = (score / self.max_score) * 100
                # print("percent::",percent)
                spamwriter.writerow([self.emails[i]] + [str(score)] + [str(percent)])

                i += 1

    def split_list(self, alist, wanted_parts=1):
        ''' To split list in specified chunks '''
        length = len(alist)
        return [alist[i * length // wanted_parts: (i + 1) * length // wanted_parts]
                for i in range(wanted_parts)]

    def standard_deviation(self):
        """Calculates the standard deviation for a row."""

        avg = float(sum(self.scores)) / len(self.scores)
        dev = []
        for x in self.scores:
            dev.append(x - avg)

        sqr = []
        for x in dev:
            sqr.append(x * x)

        mean = sum(sqr) / len(sqr)

        standard_dev = sqrt(sum(sqr) / (len(sqr) - 1))
        print("the average  deviation is :", avg)
        print("the standard deviation ", standard_dev)




file_read = open("student_responses.csv", "r")
child_object = ChildFoo(file_read)

child_object.read_data_child()
child_object.compute_score()
child_object.write_student_scores()
child_object.standard_deviation()


# class for unit testing
class TestFooClass(unittest.TestCase):

    def test_short(self):
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()

