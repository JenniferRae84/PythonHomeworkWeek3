#PyPoll Challenge

import os
import csv
import operator

total_votes = 0
candidates_list = []

election_data_csv = os.path.join("..", "election_data.csv")
with open(election_data_csv, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        total_votes += 1
        candidates_list.append(row[2])

khan_total_votes = (candidates_list.count("Khan"))
correy_total_votes = (candidates_list.count("Correy"))
li_total_votes = (candidates_list.count("Li"))  
otool_total_votes = (candidates_list.count("O'Tooley"))

khan_percent = round((khan_total_votes / total_votes) * 100, 2)
correy_percent = round((correy_total_votes / total_votes) * 100, 2)
li_percent = round((li_total_votes / total_votes) * 100, 2)
otool_percent = round((otool_total_votes / total_votes) * 100, 2)

final_tally = {
    "Khan": khan_total_votes,
    "Correy": correy_total_votes,
    "Li": li_total_votes,
    "O'Tooley": otool_total_votes
}
winner = max(final_tally.items(), key=operator.itemgetter(1))[0]

with open('output_PyPoll.txt', 'w') as f:

    f.write("                  \n")
    f.write("Election Results \n")
    f.write("------------------------ \n")
    f.write(f"Total Votes: {total_votes} \n")
    f.write("------------------------ \n")
    f.write(f"Khan: {khan_percent}% ({khan_total_votes}) \n")
    f.write(f"Correy: {correy_percent}% ({correy_total_votes}) \n")
    f.write(f"Li: {li_percent}% ({li_total_votes}) \n")
    f.write(f"O'Tooley: {otool_percent}% ({otool_total_votes}) \n")
    f.write("------------------------ \n")
    f.write(f"Winner: {winner} \n")
    f.write("------------------------ \n")
