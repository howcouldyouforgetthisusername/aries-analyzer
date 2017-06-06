import slate
import re

# First, find the file.

# Then, extract text from the file.
with open('streamPDF.pdf', 'rb') as f:
    raw = slate.PDF(f)
    #print(raw[0])

# Parse the text.

students = []
for page in raw:
    name = re.search("Progress Report For (\D*) \(", page).group(1)
    students.append({'name': name})
print(students)

# Analyze the text.

# Display results.
