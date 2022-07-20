import pandas as pd
import numpy as np
import re

# 1. Write a function named is_vowel. It should accept a string as input and use a regular expression to determine if the passed string is a vowel. While not explicity mentioned in the lesson, you can treat the result of re.search as a boolean value that indicates whether or not the regular expression matches the given string.

def is_vowel(string):
    '''
    Takes a string and determines if it is a single value or not
    {Returns : Boolean}
    '''
    # Refactored the commented out block below this line of code since this is more efficient
    return bool(re.search(r'^[aeiouAEIOU]$',string))
    # if re.search(r'^[aeiouAEIOU]$',string):
    #     return True
    # else:
    #     return False

# 2. Write a function named is_valid_username that accepts a string as input. A valid username starts with a lowercase letter, and only consists of lowercase letters, numbers, or the _ character. It should also be no longer than 32 characters. The function should return either True or False depending on whether the passed string is a valid username.

def is_valid_username(string):
    '''
    Takes a string and determines if it is a valid password: 1-32 letters long, must start with lower case, can only have lower case, 0-9 and _
    {Returns : Boolean}
    '''
    re_string = r'^[a-z]\w{0,31}$' # best practice to st up the regex expression seperately
    return bool(re.search(re_string, string))
    # if re.search(r'^[a-z]\w{0,31}$', string):
    #     return True
    # else:
    #     return False

# 3. Write a regular expression to capture phone numbers. It should match all of the following: (210) 867 5309; +1 210.867.5309; 867-5309; 210-867-5309

def phone_capture(phstr):
    '''
    Determines if a given string includes a phone number that has either a xxx xxxx or xxx xxx xxxx format at its core.
    '''
    try: 
        x = re.findall(r'(\d\d\d+)',phstr)
        if (len(x[-2]) > len(x[-1])):
            return False 
        num_count = 0
        for i in x:
            if (len(i) < 3):
                return False
            if (len(i) > 4):
                return False
            num_count += len(i)
        if num_count in [7,10]:        
            return True
        else:
            return False
    except:
        return False

# 4. Use regular expressions to convert the dates below to the standardized year-month-day format: 02/04/19; 02/05/19; 02/06/19; 02/07/19; 02/08/19; 02/09/19; 02/10/19

def date_convert(date):
    '''
    Converts a date given in mm/dd/yy to yyyy-mm-dd
    '''
    if re.search(r'\d\d\/\d\d/\d\d',date):
        print(f'20{date[-2:]}-{date[:2]}-{date[3:5]}')

# 5. Write a regex to extract the various parts of these logfile lines:


