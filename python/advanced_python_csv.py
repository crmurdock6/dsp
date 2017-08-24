import os
import re

path = os.path.expanduser('~/ds/metis/metisgh/prework/dsp/python/faculty.csv')
output_path = os.path.expanduser('~/ds/metis/metisgh/prework/dsp/'
                                 'python/emails.csv')
emailRegex = re.compile(r'''(
    \w+                    # username
    @                      # symbol
    [a-zA-Z0-9.-]+         # domain name
    \.[a-zA-Z]{2,4}        # dot something
    )''', re.VERBOSE)


def get_emails(path):
    """
    Determines the email addresses for the faculty and writes them to a csv.

    Args:
        path: the location of the faculty.csv file

    Returns:
        A csv containing one email address per line
    """
    with open(path, 'r') as csv_file:
        lines = csv_file.readlines()[1:]
    emails = emailRegex.findall(''.join(lines))
    csv_string = ''
    for email in emails:
        csv_string += email + '\n'
    with open(output_path, 'w') as output_file:
        output_file.write(csv_string)


get_emails(path)
