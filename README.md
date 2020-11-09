# foobar

Grading Student Responses

A class is learning to sort cards.  Each student was given five cards and asked to sort them properly.

The id for each student and the final order they sorted the cards are in the student_responses.csv file.

Your task is to score the card sorting done by each of the students.

Use the foobar.py module to write a new child class that:

1. Reads the csv data

2. Scores the card sorting

3. Writes the results for each student to a new CSV file

4. Prints the average and standard deviation of the student raw scores




# Code Details

Details for the class interfaces are found in the code.  The correct sorting order is A1, A2, A3, A4, A5

The student responses are arranged in the csv file like this:

card labels, student id


So, for the following sample entry:

A1,A2,A5,A4,A3,lionel.messi@barcelona.com


The student, Lionel Messi, sorted the five cards in the following order:

1. A1

2. A2

3. A5

4. A4

5. A3

His raw score is (3 correct cards * 4 points per correct card) - 2 points for incorrect cards = 10
because two moves (moving A5 to the end and moving A3 to the third position) would be required to
change the submitted order to the correct order. This number of moves is known as the edit distance or Levenshtein Distance. 
There is a Levenshtein Distance method included in the class.

There are several test entries (the student id is test@test.com) in the csv file as well.  They should be skipped.

In addition, any repeated entries (after the first) should be skipped.  For example, if the same student id occurs in the
csv file three times, the line with the first occurrence should be scored and the other two should be skipped.

The results should be written like this:

student id, raw_score, percentage correct to two decimal places

For example:

lionel.messsi@barcelona.com, 3, 0.20


The results file should be arranged from highest score to lowest score

Finally, write a unit test for the new class.


