"""
https://www.hackerrank.com/challenges/mars-exploration/problem
"""

received_messages = input().strip()
SOS_MSG = 'SOS'
SOS_MSG_LEN = len(SOS_MSG)


def different_chars(str1, str2):
    assert len(str1) == len(str2)
    counter = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            counter += 1
    return(counter)

letters_changed_by_radiation = 0
for i in range(0, len(received_messages), SOS_MSG_LEN):
    single_message = received_messages[i:i+SOS_MSG_LEN]
    letters_changed_by_radiation += different_chars(single_message, SOS_MSG)

print(letters_changed_by_radiation)
