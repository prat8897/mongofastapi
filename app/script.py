import json
from pymongo import MongoClient, ASCENDING, DESCENDING

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['course_database']

def create_courses_collection():
    # Create the 'courses' collection
    collection = db['courses']
    collection.create_index([('name', ASCENDING)])  # Index for sorting by course title (alphabetical)
    collection.create_index([('date', DESCENDING)])  # Index for sorting by date (descending)
    collection.create_index([('rating.total', DESCENDING)])  # Index for sorting by total course rating (descending)
    return collection

def insert_courses_data(collection, courses_data):
    # Insert course data into the 'courses' collection
    collection.insert_many(courses_data)

def parse_courses_json():
    # Read data from courses.json
    with open('courses.json') as file:
        data = json.load(file)
    
    # Extract course data
    courses_data = []
    for course in data:
        course_data = {
            'name': course['name'],
            'date': course['date'],
            'description': course['description'],
            'domain': course['domain'],
            'chapters': course['chapters'],
            'rating': {
                'total': 0,
                'count': 0,
                'average': 0
            }
        }
        courses_data.append(course_data)

    return courses_data

def main():
    # Parse courses.json
    courses_data = parse_courses_json()

    # Create courses collection and insert data
    courses_collection = create_courses_collection()
    insert_courses_data(courses_collection, courses_data)

    # Close MongoDB connection
    client.close()

if __name__ == '__main__':
    main()