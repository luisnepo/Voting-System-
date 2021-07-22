# Voting-System-
Coursework required on my 1st year at Bsc Computer Science
Requirements:
-Users should be able to log in using their student ID file and only be able to vote once.
  -This was acomplished by utilizing a text file where students ID would be stored so if the student tried to vote again their ID wouldn't be accepted. Since this was    a project for university there was no need to use the university database,otherwise the system would work by accesing a database and marking the students who have    already voted instead of saving their ID onto a text file since a user could enter a fake ID and still be able to enter the system.
-Users should be able to see a list of all the Candidates from who they could choose to vote. 
  -this was acomplished by utilizing a database to store every candidate name and ID and storing how many votes they had.
-After the deadline of the voting students can not log in.
  -This was accomplished by using a time function that compared the current date versus the date that was saved as the deadline.
-After deadline the program needs to show who won the elections.
  -This was accomplished by reorganizing the database,not by ID but by the number of total votes at the end of the deadline.
