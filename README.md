# foobar

Grading Student Respsonses

A class is learning to sort cards.  Each student was given five cards and asked to sort them properly.

The id for each student and the final order they sorted the cards are in the student_responses.csv file.

Your task is to score the card sorting done by each of the students

Use the foobar.py module to write a new child class that:

1. Reads the csv data
2. Scores the card sorting
3. Writes the results for each student as a row in a new CSV file

Details for the class interfaces are found in the code.

The student responses are arranged like this:

student_id, card labels

So, for the following sample entry:

lionel.messi@barcelona.com,A1,A5,A2,A3,A4

The student, Lionel Messi, sorted the five cards in the following order:
1. A1
2. A5
3. A2
4. A3
5. A4

In addition, write a unit test for new class that tests the card sorting method.
