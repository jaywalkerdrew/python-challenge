import csv
import os

electionInput = os.path.join("Resources", "election_data.csv")
electionOutput = os.path.join("analysis", "analysis.txt")

totalVotes = 0
candidateList = {}
# create variables - totalVotes int, candidateList = {candidate: votes}

# open CSV for read
with open(electionInput) as csvFile:
    reader = csv.reader(csvFile)
    # skip the header row
    next(reader)

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

# print (totalVotes)        
# print (candidateList)

candidateVotePercent = {}
for candidate in candidateList.keys():
    candidateVotes = candidateList[candidate]
    percent = candidateVotes / totalVotes
    candidateVotePercent.update({candidate: percent})

winner = max(candidateList, key=candidateList.get)
sortedCandidates = sorted(candidateList, key=candidateList.__getitem__, reverse=True)

print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalVotes}")
print("-------------------------")
for name in sortedCandidates:
    print(str(name) + ": " + str("{:.2%}".format(candidateVotePercent[name])) + " (" + str(candidateList[name]) + ")")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

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