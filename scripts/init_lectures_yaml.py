import yaml
from datetime import date, timedelta

# date(year, month, day)
current_year = 2022
start_date = date(current_year, 8, 25)
end_date = date(current_year, 12, 1)
semester_delta = end_date - start_date

no_lecture_titles = {"No lecture", "Midterm 1", "Midterm 2", "Thanksgiving"}
titles_and_text = [
        { 'title': "No lecture" },
        { 'title': "Introduction, Big-O Notation, Arithmetic",
            'reading_text': ["0", "1.1"] },
        { 'title': "Divide-and-Conquer (Part I)",
            'reading_text': ["2.1", "2.2", "2.3"] },
        { 'title': "Divide-and-Conquer (Part II)",
            'reading_text': ["2.4", "2.5", "2.6"] },
        { 'title': "Fast Fourier Transform",
            'reading_text': ["2.6"] },
        { 'title': "Graph decomposition",
            'reading_text': ["3"] },
        { 'title': "Paths in graphs (Part I)",
            'reading_text': ["4.1", "4.2", "4.3", "4.4"] },
        { 'title': "Paths in graphs (Part II)",
            'reading_text': ["4.4", "4.5", "4.6", "4.7"] },
        { 'title': "Minimum Spanning Trees",
            'reading_text': ["5.1"] },
        { 'title': "Greedy Algorithms",
            'reading_text': ["5", "5.4"] },
        { 'title': "Union Find",
            'reading_text': ["5.1.4"] },
        { 'title': "Dynamic Programming (Part I)",
            'reading_text': ["6"] },
        { 'title': "Midterm 1" },
        { 'title': "Dynamic Programming (Part II)",
            'reading_text': ["6"] },
        { 'title': "Linear Programming",
            'reading_text': ["7.2"] },
        { 'title': "Network Flow (Part I)",
            'reading_text': ["7.4"] },
        { 'title': "Network Flow (Part II)",
            'reading_text': ["7.4"] },
        { 'title': "Zero-Sum Games",
            'reading_text': ["7.5"] },
        { 'title': "Multiplicative Updates" },
        { 'title': "Reductions, Bipartite Matching",
            'reading_text': ["7.3"] },
        { 'title': "Midterm 2" },
        { 'title': "Search Problems",
            'reading_text': ["8.1"] },
        { 'title': "NP-Completeness",
            'reading_text': ["8.2", "8.3"] },
        { 'title': "Coping with NP-completeness",
            'reading_text': ["9"] },
        { 'title': "Randomized Algorithms",
            'reading_text': ["1.3"] },
        { 'title': "Sketching, Streaming",
            'reading_text': ["1.5"] },
        { 'title': "Lower bounds" },
        { 'title': "Thanksgiving" },
        { 'title': "Hashing" },
        { 'title': "Special topic" }
]

yaml_data = []
if start_date.weekday() == 2:
    # start date is a Tuesday
    tue_date = start_date
    thu_date = start_date + timedelta(days=2)
else:
    # start date is a Thursday
    tue_date = start_date - timedelta(days=2)
    thu_date = start_date

# Generate lectures
index = 0
youtube_index = 1
for week in range(1, semester_delta.days // 7 + 2):
    lec_info = titles_and_text[index]
    tue = {
            'type': 'lec',
            'date': f"{tue_date.month}/{tue_date.day}",
            'week': week,
            'title': lec_info['title']
            }
    if 'reading_text' in lec_info:
        tue['reading_text'] = lec_info['reading_text']
    yaml_data.append(tue)
    index += 1
    tue_date = tue_date + timedelta(weeks=1)

    lec_info = titles_and_text[index]
    thu = {
            'type': 'lec',
            'date': f"{thu_date.month}/{thu_date.day}",
            'week': week,
            'title': lec_info['title']
            }
    if 'reading_text' in lec_info:
        thu['reading_text'] = lec_info['reading_text']
    yaml_data.append(thu)
    index += 1
    thu_date = thu_date + timedelta(weeks=1)

# Write to a YAML file
output = yaml.dump(yaml_data)
with open('lectures.yaml', 'w') as f:
    f.write(output)

