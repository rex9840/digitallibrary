import random

# Course data
courses = [
    "CS601", "CND401", "WD501", "DL701", "CSF701", "NLP901", "DBMS701", "RA701", "QC101", "MAD501",
    "EHT401", "CS602", "CND402", "WD502", "DL702", "CSF702", "NLP902", "DBMS702", "RA702", "QC102",
    "MAD502", "EHT402", "CS603", "CND403", "WD503", "DL703", "CSF703", "NLP903", "DBMS703", "RA703",
    "QC103", "MAD503", "EHT403", "CS604", "CND404", "WD504", "DL704", "CSF704", "NLP904", "DBMS704",
    "RA704", "QC104", "MAD504", "EHT404", "CS605", "CND405", "WD505", "DL705", "CSF705", "NLP905",
    "DBMS705", "RA705", "QC105", "MAD505", "EHT405", "CS606", "CND406", "WD506", "DL706", "CSF706",
    "NLP906", "DBMS706", "RA706", "QC106", "MAD506", "EHT406", "CS607", "CND407", "WD507", "DL707",
    "CSF707", "NLP907", "DBMS707", "RA707", "QC107", "MAD507", "EHT407", "CS608", "CND408", "WD508",
    "DL708", "CSF708", "NLP908", "DBMS708", "RA708", "QC108", "MAD508", "EHT408", "CS609", "CND409",
    "WD509", "DL709", "CSF709", "NLP909", "DBMS709", "RA709", "QC109", "MAD509", "EHT409", "CS610",
    "CND410", "WD510", "DL710", "CSF710", "NLP910", "DBMS710", "RA710", "QC110", "MAD510", "EHT410",
    "DS101"
]

# Generate user data
users_data = []

for user_id in range(1, 101):
    num_courses = random.randint(2, 4)
    courses_selected = random.sample(courses, num_courses)
    for course_id in courses_selected:
        rating = round(random.uniform(3.5, 4.8), 1)
        users_data.append((user_id, course_id, rating))

# Output the data to CSV format
with open('user_course_ratings.csv', 'w') as f:
    f.write('user_id,course_id,rating\n')
    for user_data in users_data:
        f.write(','.join(map(str, user_data)) + '\n')

print("Dataset generated successfully.")
