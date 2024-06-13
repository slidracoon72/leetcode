# def min_trips(packageweight):
#     # Count the frequency of each package weight
#     package_counts = {}
#     for weight in packageweight:
#         package_counts[weight] = package_counts.get(weight, 0) + 1
#
#     # Sort the package weights in descending order
#     weights_sorted = sorted(package_counts.keys(), reverse=True)
#
#     # Count the number of trips required
#     trips = 0
#     remaining_packages = len(packageweight)
#     while remaining_packages > 0:
#         found_trip = False
#         # Try to form trips with three packages of the same weight
#         for weight in weights_sorted:
#             if package_counts.get(weight, 0) >= 3:
#                 trips += 1
#                 package_counts[weight] -= 3
#                 remaining_packages -= 3
#                 found_trip = True
#                 break
#         # If not possible, try to form trips with two packages of the same weight
#         if not found_trip:
#             for weight in weights_sorted:
#                 if package_counts.get(weight, 0) >= 2:
#                     trips += 1
#                     package_counts[weight] -= 2
#                     remaining_packages -= 2
#                     found_trip = True
#                     break
#         # If neither 3 nor 2 packages of the same weight are available, it's not possible
#         if not found_trip:
#             return -1
#
#     return trips
#
#
# # Test the function
# packageweight = [1, 8, 5, 8, 8, 5, 1, 1]
# print("Minimum trips required:", min_trips(packageweight))

from collections import Counter


def min_trips(packageweight):
    # Count the frequency of each package weight
    package_counts = Counter(packageweight)

    # Sort the package weights in descending order
    sorted_weights = sorted(package_counts.keys(), reverse=True)

    trips = 0
    remaining_packages = len(packageweight)

    while remaining_packages > 0:
        found_trip = False

        # Try to form trips with three packages of the same weight
        for weight in sorted_weights:
            if package_counts[weight] >= 3:
                trips += 1
                package_counts[weight] -= 3
                remaining_packages -= 3
                found_trip = True
                break

        if not found_trip:
            # Try to form trips with two packages of the same weight
            for weight in sorted_weights:
                if package_counts[weight] >= 2:
                    trips += 1
                    package_counts[weight] -= 2
                    remaining_packages -= 2
                    found_trip = True
                    break

        if not found_trip:
            # If neither 3 nor 2 packages of the same weight are available, it's not possible
            return -1

    return trips


# Test cases
packageweight1 = [2, 4, 6, 6, 2, 4]
print("Minimum trips required:", min_trips(packageweight1))  # Output: 3

packageweight2 = [2, 2, 2, 2, 2, 2, 3, 3, 3, 3]
print("Minimum trips required:", min_trips(packageweight2))  # Output: 4

packageweight3 = [1, 2, 3, 4, 5]
print("Minimum trips required:", min_trips(packageweight3))  # Output: -1
