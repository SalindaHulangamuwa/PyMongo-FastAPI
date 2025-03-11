import re

text = "PERSON_ABC's"

# With capturing groups
pattern1 = r"(PERSON_ABC)('s)"
match1 = re.search(pattern1, text)
print(match1.group(0))  # Full match: "PERSON_ABC's"
print(match1.group(1))  # Box 1: "PERSON_ABC"
print(match1.group(2))  # Box 2: "'s"

# With non-capturing group
pattern2 = r"(PERSON_ABC)(?:'s)"
match2 = re.search(pattern2, text)
print(match2.group(0))  # Full match: "PERSON_ABC's"
print(match2.group(1))  # Box 1: "PERSON_ABC"
# There is no match2.group(2)! It would cause an error