import re
# Print a welcome message to the user, explaining the Madlib process and command line interactions
multi_line ='''
**************************************
**   Welcome to my Mad Libs Game!   **
**                                  **
**    Please enter the requested    **
**  when prompted. Your given words ** 
**     will be added to a story     **
**      and make it sound wacky.    **
**                                  **
**      To quit at any time,        **
**       type "IWantToQuit"         **
**************************************
'''
print(multi_line)

# Read a template Madlib file, and parse that file into usable parts.

# Going to have to pull in the whole text then maybe splice it all and pull the "{}"" as a list. Then display each part of that list 1 by 1 to the user, save those answers to a list. Insert those answers only at the correct spots then display it to the user.

# VARIABLES
user_input_list = []

# FUNCTIONS
# Regex finds words that are indside of {}
def find_matching_words(words_to_match):
  matches = re.findall('{.+?}', str(words_to_match))
  return matches

def replace_matching_words(words_to_match):
  matches = re.findall('{.+?}', str(words_to_match))
  for i in range(len(matches)):
    while matches == i:
      matches[i] = user_input_list[i]

  # return replaced_words

# prompts user for input of requested word types
def get_user_input():
  for i in matched_words:
    user_input = input('Please enter a {}'.format(i))
    user_input_list.append(user_input)
  return user_input_list

# Opening the mad libs text file
with open('madlibs_cli/assets/dark_and_stormy_night_template.txt') as template:
  parsed_list = []
  contents = template.readlines()
# parses contents and splits the words into a list, then finds words that are inside of {}
  for line in contents:
    for parsed_text in line.split():
      parsed_list.append(parsed_text)
      matched_words = find_matching_words(parsed_list)

# Prompt the user to submit a series of words to fit each of the required components of the Madlib template.
get_user_input()
  
# With the collected user inputs, populate the template such that each provided input is placed into the correct position within the template.
with open('madlibs_cli/assets/dark_and_stormy_night_template.txt') as to_be_replaced:
  parsed_list_in_replace = []
  contents_again = to_be_replaced.readlines()
  for line in contents_again:
    for parsed_text in line.split():
      parsed_list_in_replace.append(parsed_text)
    replaced_words = replace_matching_words(parsed_list_in_replace)

# After the resulting Madlib has been completed, provide the completed response back to the user in the command line.
# Write the completed text (Example)to a new file on your file system (in the repo).
