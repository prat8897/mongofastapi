
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

   ```bash
   git clone https://github.com/your-username/fastapi-course-management.git
   
Install the required dependencies:

    pip install -r requirements.txt
    
Start the FastAPI application:

    uvicorn app.main:app --host 0.0.0.0 --port 8000
    
The application will be accessible at http://localhost:8000.

Endpoints
GET /courses: Get a list of available courses.
GET /courses/{course_name}: Get detailed information about a course.
GET /courses/{course_name}/{chapter_title}: Get information about a specific chapter within a course.
POST /courses/{course_name}/{chapter_title}/rate: Rate a chapter (positive or negative) and aggregate ratings for each course.
