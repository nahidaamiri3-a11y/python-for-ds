# List of marks
marks = [88, 74, 93, -5, 61, 47, 105, 82, 59]

# Variables to store valid marks and grade counts
valid_marks = []
count_a = 0
count_b = 0
count_c = 0
count_f = 0

# Process each mark
for mark in marks:
    # Skip invalid marks
    if mark < 0 or mark > 100:
        continue

    valid_marks.append(mark)

    # Count grades
    if mark >= 80:
        count_a += 1
    elif mark >= 70:
        count_b += 1
    elif mark >= 60:
        count_c += 1
    else:
        count_f += 1

# Calculate average
average = sum(valid_marks) / len(valid_marks)

# Display results
print("Valid marks:", valid_marks)
print(f"Grade counts: A = {count_a}, B = {count_b}, C = {count_c}, F = {count_f}")
print(f"Average: {average:.2f}")
print("Highest:", max(valid_marks))
print("Lowest:", min(valid_marks))