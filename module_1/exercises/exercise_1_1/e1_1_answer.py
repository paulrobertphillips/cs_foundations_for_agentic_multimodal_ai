import pprint

def all_pairs(seq):
    pairs = []
    for a in seq:
        for b in seq:
            pairs.append((a,b))
    
    return pairs

actions = ["A", "B", "C"]

results = all_pairs(actions)

# Print individual sequences
pprint.pprint(results)

# Print total count of unique sequences
print('\nTotal Count: '+str(len(results)))

