
# set up variables
filename = '/tests/paragraph.txt'
text = 'If you want to jumpstart the process of talking to us about this role, here’s a little challenge: write a program that outputs the largest unique set of characters that can be removed from this paragraph without letting its length drop below 50. For example: [‘H’, ‘i’, ‘!’, ‘ ’]'
length_limit = 50
results = []

# count characters
for c in set(text):
    results.append((c,text.count(c)))

# sort list by count
sorted_list = sorted(results, key=lambda tup: tup[1])

# remove the entries from the list until the 50 count is reached
while length_limit > 0:
    x = sorted_list.pop()
    length_limit = length_limit - x[1]

# use list comprehension to output the unique list of characters to remove
print([i[0] for i in sorted_list])
