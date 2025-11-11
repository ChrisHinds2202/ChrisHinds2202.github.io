#Christopher Hinds
#11 Nov 25
#P4HW1
#get scores from user, display and remove the lowest score, find average of list after dropping lowest score

scores = []

while True:
    numScores = int(input("How many scores do you want to enter? "))
    if numScores <= 0:
            print("Enter a number above 0")
    break

for i in range(numScores):
    while True:
        userInput = float(input(f"Enter score #{i + 1} (0-100): "))
            
        if 0 <= userInput <= 100:
            scores.append(userInput)
            break
        else:
            print(f"INVALID score entered!!!!")
            i += 1

lowestScore = min(scores)
print("Lowest score entered: " + str(lowestScore))

updatedScores = scores[:]
updatedScores.remove(lowestScore)
print(f"Scores after removing the lowest score: {updatedScores}")

average = sum(updatedScores) / len(updatedScores)
print(f"the average of the list is: {average:.2f}")

grade = ''
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"The calculated letter grade is: {grade}")