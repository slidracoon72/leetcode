def findRecurringNames(realNames, allNames):
    from collections import defaultdict

    # Initialize a dictionary to store the sorted names and their counts
    name_counts = defaultdict(int)

    # Count occurrences of each sorted name in allNames
    for name in allNames:
        for real_name in realNames:
            if sorted(real_name) == sorted(name):
                name_counts[real_name] += 1
                break

    # Initialize a list to store recurring names
    recurring_names = []

    # Iterate through the name_counts dictionary to find recurring names
    for name, count in name_counts.items():
        if count > 1:
            recurring_names.append(name)

    # Sort the recurring names in lexicographical order
    recurring_names.sort()

    # If there are no recurring names, return ["None"]
    if not recurring_names:
        return ["None"]

    return recurring_names


# Example usage:
realNames = ["alice", "bob", "terry"]
allNames = ["celia", "alice", "retry", "bob", "terry"]
print(findRecurringNames(realNames, allNames))
