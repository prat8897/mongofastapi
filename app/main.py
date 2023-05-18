from fastapi import FastAPI, Query
from pymongo import MongoClient, ASCENDING, DESCENDING
import json
from bson import ObjectId, json_util


app = FastAPI()

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Assuming your MongoDB container is named 'mongodb'
db = client['course_database']
courses_collection = db['courses']


def to_json_serializable(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    return obj

@app.get("/courses")
async def get_courses(sort: str = "alphabetical", domain: str = None):
    allowed_sorts = {
        "alphabetical": [("name", ASCENDING)],
        "date": [("date", DESCENDING)],
        "rating": [("rating.total", DESCENDING)]
    }

    # Set the sort criteria based on the requested sort option
    sort_criteria = allowed_sorts.get(sort, [("name", ASCENDING)])

    # Build the filter query if a domain is specified
    filter_query = {}
    if domain:
        filter_query = {"domain": domain}

    # Retrieve the courses based on the sort criteria and filter query
    courses = courses_collection.find(filter_query).sort(sort_criteria)

    # Convert the courses to a JSON-serializable format
    response = json.loads(json_util.dumps(list(courses)))
    return response

@app.get("/courses/{course_name}")
async def get_course_overview(course_name: str):
    # Retrieve the course based on the provided course name
    course = courses_collection.find_one({"name": course_name})

    # Convert the course to a JSON-serializable format
    #course_json = json.dumps(course, default=to_json_serializable)
    response = json.loads(json_util.dumps(course))

    # Return the course overview as JSON
    #return course_json
    return response

@app.get("/courses/{course_name}/{chapter_title}")
async def get_chapter_info(course_name: str, chapter_title: str):
    # Retrieve the course based on the provided course name
    course = courses_collection.find_one({"name": course_name})

    # Find the chapter with the matching title
    chapter = next((ch for ch in course["chapters"] if ch["name"] == chapter_title), None)

    # Return the chapter information
    return chapter

@app.post("/courses/{course_name}/{chapter_title}/rate")
async def rate_chapter(course_name: str, chapter_title: str, rating: int):
    # Retrieve the course based on the provided course name
    course = courses_collection.find_one({"name": course_name})

    # Find the chapter with the matching title
    chapter = next((ch for ch in course["chapters"] if ch["name"] == chapter_title), None)

    if chapter:
        # Update the chapter rating
        chapter["rating"]["total"] += rating
        chapter["rating"]["count"] += 1
        chapter["rating"]["average"] = chapter["rating"]["total"] / chapter["rating"]["count"]

        # Update the course rating
        course["rating"]["total"] += rating
        course["rating"]["count"] += 1
        course["rating"]["average"] = course["rating"]["total"] / course["rating"]["count"]

        # Update the course and chapter data in MongoDB
        courses_collection.update_one({"name": course_name}, {"$set": course})

        # Return the updated chapter information
        return chapter

    return {"message": "Chapter not found"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
