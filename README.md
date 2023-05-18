
# FastAPI Course Management Project

This is a sample project showcasing a course management system built with FastAPI.

## Description

The FastAPI Course Management Project provides a RESTful API for managing courses, chapters, and ratings. It allows users to retrieve a list of courses, get detailed information about individual courses and chapters, and rate chapters.

## Features

- Retrieve a list of available courses
- Get detailed information about a course
- Get information about specific chapters within a course
- Rate chapters (positive or negative) and aggregate ratings for each course

## Installation

1. Clone the repository:
               
         git clone https://github.com/prat8897/mongofastapi.git
   
2. Install the required dependencies:

         pip install -r requirements.txt
         
3. Set up MongoDB:

Install MongoDB: Follow the installation instructions for your operating system from the official MongoDB documentation: MongoDB Installation

Start MongoDB: Start the MongoDB server by running the appropriate command for your system. For example:

    mongod
4. Import the course data to MongoDB:

Ensure MongoDB is running.

Run the provided script to parse the course information from courses.json, create the appropriate databases and collections in MongoDB, and add the course data:

    python script.py
The script.py script assumes the courses.json file is in the same directory and connects to a local MongoDB instance.
    
5. Start the FastAPI application:

         uvicorn app.main:app --host 0.0.0.0 --port 8000
    
The application will be accessible at http://localhost:8000.

Endpoints


GET /courses: Get a list of available courses.


GET /courses/{course_name}: Get detailed information about a course.


GET /courses/{course_name}/{chapter_title}: Get information about a specific chapter within a course.


POST /courses/{course_name}/{chapter_title}/rate: Rate a chapter (positive or negative) and aggregate ratings for each course.
