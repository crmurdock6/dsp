# The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

path = 'football.csv'


def read(path):
    """
    Parses the football csv, calculates the difference between goals scored
    for each team and goals scored against them, and returns the team with the
    smallest difference.
    """
    with open(path, 'r') as csv_file:
        lines = csv_file.readlines()[1:]
        team_diffs = []
        for line in lines:
            line.split(',')
            team_diffs.append([line[0], line[5] - line[6]])
        return sorted(team_diffs, key=lambda x: x[1])[0][0]


read(path)
