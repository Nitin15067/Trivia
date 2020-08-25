# Trivia
Trivia is a quiz based application where you can play quiz in different categories as per you like. You can perform CRUD operations on questions. The Platform is developed in flask for backend and react for frontend.
All backend code follows [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/).

Featuring functionalities like:
1) Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer. 
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category. 
, 
## Getting Started

### Pre-requisites and Local Development
Developers using this project should already have Python3, pip, react and node installed on their local machine.

#### Backend
From the backend folder run pip install requirements.txt. All required packages are included in the requirements file.
To migrate the postgres database file, run the following commands after creating the db with name "trivia":
```psql trivia < trivia.psql```

To run the application, run the following commands:
```export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

* Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

* Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

These commands put the application in development and directs our application to use the `__init__.py` file in our flaskr folder. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made. If running locally on Windows, look for the commands in the Flask documentation.

The applicaiton will run on `http://127.0.0.1:5000` by default.

#### Frontend
From the frontend folder, run the following commands to start the client:
```
npm install
npm start
```

Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.<br>

#### Tests
In order to run tests navigate to the backend folder and run the following commands:
```dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

The first time you run the tests, omit the dropdb command.
All tests are kept in that file and should be maintained as updates are made to app functionality.

## API Reference

### Getting Started
* Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http:127.0.0.1:5000/`
* Authentication: This version of the application does not require authentication or API keys.

### Error Handling
Errors are returned as JSON objects in the following format:
```
{
  "success": False,
  "error": 404,
  "message": "resource not found"
}
```

The API will return these error types when requests fail:
* 400: Bad Request
* 404: Not Found
* 405: Method Not Allowed
* 422: Unprocessable
* 500: Server Error

### Endpoints
##### GET /questions
* General:
  * Returns a list of questions, success, and total number of questions, categories, current category.
  * Sample: `curl http://127.0.0.1:5000/questions`
 ```
 {
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "current_category": null, 
  "questions": [
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ], 
  "success": true, 
  "total_questions": 35
}

 ```
  
##### POST /questions
* General:
  * Creates a new question using the submitted question, answer, difficulty, category.
  * Sample: `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question": "Demo Question", "answer": "Demo Answer", "difficulty": 5, "category"}'`
 ```
  {
    "success": true
  }
 ```
 
 ### Authors
 Nitin Yadav
 
 ### Acknowledgements
 Udacity Full Stack Nanodegree Program
