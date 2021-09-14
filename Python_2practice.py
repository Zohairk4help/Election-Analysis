counties = ["Arapahoe","Denver","Jefferson"]
# if statement practice
print(counties)
if counties[1] == 'Denver':
    print(counties[1])
# If-Else Statements practice 
temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")
# Would you like to open the windows? [it is used for us to input in the screen for decision making]
question1 = str(input("Have you opened the windows? "))
#  How many times have i opened the windows .... it is used for us to input in the screen for decision making
times_of_windowsopening = int(input("How many times have you opened the windows today since its not that hot? "))
# Calculate the percentage of votes you received. putting the if condition:
if times_of_windowsopening <= 1:
        print("Honey, stop wasting your electricity. Go open the damn windows.")
else:
    print("good job! I am proud of you! ^_^")
# else if nested by strings 
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

    # while loop practice
    x = 0
while x <= 5:
    print(x)
    x = x + 1



candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)