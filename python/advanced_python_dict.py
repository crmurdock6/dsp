import os
import re

path = os.path.expanduser('~/ds/metis/metisgh/prework/dsp/python/faculty.csv')
title_regex = re.compile(r'(\w+\s)?professor', re.IGNORECASE)


def q6_dict(path):
    """
    Consructs a dictionary of facults names, title, degree(s), and emails.

    Args:
        path: the location of the faculty.csv file

    Returns:
        A dictionary with last name as keys and nested list of title, degree,
        and email as values for each faculty with the given last name.
    """
    faculty_dict = {}
    with open(path, 'r') as my_file:
        lines = my_file.readlines()[1:]
    for line in lines:
        line = line.replace('\n', '').split(',')
        last_name = line[0].split(' ')[-1]
        if last_name not in faculty_dict:
            faculty_dict[last_name] = []
        faculty_dict[last_name].append([line[1].lstrip(' '),
                                        re.search(title_regex,
                                        line[2]).group(), line[3]])
    for k in sorted(faculty_dict)[:3]:
        print(k, faculty_dict[k])


def q7_dict(path):
    """
    Consructs a dictionary of facults names, title, degree(s), and emails.

    Args:
        path: the location of the faculty.csv file

    Returns:
        First three items of a dictionary with first and last name (sorted by
        first name) as keys and a nested list of title, degree, and email as
        values for each name.
    """
    faculty_dict = {}
    with open(path, 'r') as my_file:
        lines = my_file.readlines()[1:]
    for line in lines:
        line = line.replace('\n', '').split(',')
        name = (line[0].split(' ')[0], line[0].split(' ')[-1])
        faculty_dict[name] = [line[1].lstrip(' '),
                              re.search(title_regex, line[2]).group(),
                              line[3]]
    for k in sorted(faculty_dict)[:3]:
        print(k, faculty_dict[k])


def q8_dict(path):
    """
    Consructs a dictionary of facults names, title, degree(s), and emails.

    Args:
        path: the location of the faculty.csv file

    Returns:
        First three items of a dictionary with first and last name (sorted by
        last name) as keys and a nested list of title, degree, and email as
        values for each name.
    """
    faculty_dict = {}
    with open(path, 'r') as my_file:
        lines = my_file.readlines()[1:]
    for line in lines:
        line = line.replace('\n', '').split(',')
        name = (line[0].split(' ')[0], line[0].split(' ')[-1])
        faculty_dict[name] = [line[1].lstrip(' '),
                              re.search(title_regex, line[2]).group(),
                              line[3]]
    for k in sorted(faculty_dict, key=lambda x: x[-1])[:3]:
        print(k, faculty_dict[k])


q6_dict(path)
q7_dict(path)
q8_dict(path)
