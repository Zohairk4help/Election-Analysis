print("Hello World")
counties = ["Arapahoe","Denver","Jefferson"]
print (counties)
counties[0]
print(counties[0])
print(counties[-1])
print(counties[-2])
len(counties)
print(len(counties))
print(counties[0:2])
counties.append("El Paso")
print (counties)
counties.insert(2, "El Paso")
print (counties)
counties.remove("El Paso")
print (counties)
counties.pop(3)
print(counties)
counties[2] = "El Paso"
print(counties)
counties_tuple = ("Arapahoe","Denver","Jefferson")
print (counties_tuple)
len(counties_tuple)
print(len(counties_tuple))
print(counties_tuple[1])
counties_dict = {}
print(counties_dict)
counties_dict["Arapahoe"] = 422829
print(counties_dict)
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(counties_dict)
len(counties_dict)
print(len(counties_dict))
counties_dict.keys()
print(counties_dict.keys())
counties_dict.values()
print(counties_dict.values())
counties_dict.get("Denver")
print(counties_dict.get("Denver"))
counties_dict["Arapahoe"]
print(counties_dict["Arapahoe"])
voting_data = []
print(voting_data)
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)

# How many votes did you get? [it is used for us to input in the screen for decision making]
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election .... it is used for us to input in the screen for decision making
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("you received " + str(percentage_votes)+"% of the total votes.")
for county in counties_dict:
    print(county)

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)
