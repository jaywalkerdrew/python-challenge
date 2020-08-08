import csv
import os

electionInput = os.path.join("Resources", "election_data.csv")
electionOutput = os.path.join("analysis", "analysis.txt")

# initialize variables
totalVotes = 0
candidateList = {}

# open CSV for read
with open(electionInput) as csvFile:
    reader = csv.reader(csvFile)

    # skip the header row
    header = next(reader)

    #loop through each row of data/each vote submitted
    for row in reader:

        # increment total votes and find who was voted for
        totalVotes = totalVotes +1
        currentCandidate = row[2]

        # check the dictionary for the candidate
        if currentCandidate not in candidateList.keys():

            # if new, start their vote count at 1 and add to the dictionary
            newCandidate = {currentCandidate: 1}
            candidateList.update(newCandidate)

        # otherwise, add 1 to their count and update the vote count     
        else:
            addVote = candidateList[currentCandidate] + 1
            voteAdded = {currentCandidate: addVote}
            candidateList.update(voteAdded)

# create a dict with the same keys, but store candidate's percent of votes
candidateVotePercent = {}

# loop through the list of candidates
for candidate in candidateList.keys():

    #calculate the percent of votes and store in the dictionary
    candidateVotes = candidateList[candidate]
    percent = candidateVotes / totalVotes
    candidateVotePercent.update({candidate: percent})

# locate the winning candidate
winner = max(candidateList, key=candidateList.get)

# obtain a sorted list of the candidates, winner to loser
sortedCandidates = sorted(candidateList, key=candidateList.__getitem__, reverse=True)

# print the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalVotes}")
print("-------------------------")
for name in sortedCandidates:
    print(str(name) + ": " + str("{:.2%}".format(candidateVotePercent[name])) + " (" + str(candidateList[name]) + ")")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# output to a text file
with open(electionOutput, "w") as out:
    out.write("Election Results\n")
    out.write("-------------------------\n")
    out.write(f"Total Votes: {totalVotes}\n")
    out.write("-------------------------\n")
    for name in sortedCandidates:
        out.write(str(name) + ": " + str("{:.2%}".format(candidateVotePercent[name])) + " (" + str(candidateList[name]) + ")\n")
    out.write("-------------------------\n")
    out.write(f"Winner: {winner}\n")
    out.write("-------------------------\n")
out.close()