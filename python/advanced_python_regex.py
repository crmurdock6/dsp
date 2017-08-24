import os
import re

path = os.path.expanduser('~/ds/metis/metisgh/prework/dsp/python/faculty.csv')
title_regex = re.compile(r'(\w+\s)?professor', re.IGNORECASE)
emailRegex = re.compile(r'''(
    \w+                    # username
    @                      # symbol
    [a-zA-Z0-9.-]+         # domain name
    \.[a-zA-Z]{2,4}        # dot something
    )''', re.VERBOSE)
domainRegex = re.compile(r'@(\S+)')


def diff_degrees(path):
    """
    Determines the degrees for the faculty as well as their frequency.

    Args:
        path: the location of the faculty.csv file

    Returns:
        A dictionary with the degrees as keys and their frequencies as values
    """
    degrees = {}
    with open(path, 'r') as my_file:
        lines = my_file.readlines()[1:]
    for line in lines:
        split_lines = line.split(',')
        degree_for_each_faculty = (split_lines[1].lower().replace('.', '').
                                   replace('0', 'unknown').lstrip(' ').
                                   split(' '))
        for degree in degree_for_each_faculty:
            if degree not in degrees:
                degrees[degree] = 1
            else:
                degrees[degree] += 1
    return degrees


def get_titles(path):
    """
    Determines the different titles for the faculty and their frequency.

    Args:
        path: the location of the faculty.csv file

    Returns:
        A dictionary with the titles as keys and their frequencies as values
    """
    titles = {}
    with open(path, 'r') as my_file:
        lines = my_file.readlines()[1:]
    for line in lines:
        split_lines = line.split(',')
        match = re.search(title_regex, split_lines[2])
        if match.group() not in titles:
            titles[match.group()] = 1
        else:
            titles[match.group()] += 1
    return titles


def get_emails(path):
    """
    Determines the email addresses for the faculty.

    Args:
        path: the location of the faculty.csv file

    Returns:
        A list containing all email addresses
    """
    with open(path, 'r') as csv_file:
        lines = csv_file.readlines()[1:]
    return emailRegex.findall(''.join(lines))


def email_domains(path):
    """
    Determines the different email domains for the faculty and their frequency.

    Args:
        path: the location of the faculty.csv file

    Returns:
        A list of the unique email domains
    """
    unique_domains = []
    with open(path, 'r') as csv_file:
        lines = csv_file.readlines()[1:]
    domains = domainRegex.findall(''.join(lines))
    for domain in domains:
        if domain not in unique_domains:
            unique_domains.append(domain)
        else:
            continue
    return unique_domains


diff_degrees(path)
get_titles(path)
get_emails(path)
email_domains(path)
