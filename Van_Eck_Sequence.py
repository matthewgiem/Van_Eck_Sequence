# initital conditions
sequence = [0]
to_append = 0

# add the first 100 terms
while len(sequence) < 100:
    if to_append in sequence:
        next = sequence.index(to_append) + 1
        sequence.insert(0,to_append)
        to_append = next
    else:
        sequence.insert(0,to_append)
        to_append = 0

sequence.reverse()
print(sequence)
