import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

'''
Helper Functions
'''

def paginate_questions(request, selection):
  page = request.args.get('page', 1, type=int)
  start = (page - 1) * QUESTIONS_PER_PAGE
  end = start + QUESTIONS_PER_PAGE

  questions = [question.format() for question in selection]
  return questions[start:end]

def formatCategories(categories):
  response = {}
  for category in categories:
    c = category.format()
    response[c['id']]=c['type']
  return response



def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app, resources={r"/*": {"origins": "*"}})

  # CORS settings
  @app.after_request
  def after_request(response):
    if 'Access-Control-Allow-Origin' not in response.headers:
      response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

  '''
  API Endpoints
  '''

  # get all categories
  @app.route('/categories', methods=['GET'])
  def categories():
    categories = Category.query.all()
    if len(categories) == 0:
      abort(404)

    return jsonify({
      'success': True,
      'categories': formatCategories(categories)
    })

  # get all questions, post a question
  @app.route('/questions', methods=['GET', 'POST'])
  def get_questions():
    if request.method == 'GET':
      question_collection = Question.query.all()
      
      if request.args.get('page') and len(question_collection) <= QUESTIONS_PER_PAGE*(int(request.args.get('page'))-1):
        abort(404)

      questions = paginate_questions(request, question_collection)
      categories = Category.query.all()
      
      return jsonify({
        'success': True,
        'questions': questions,
        'categories': formatCategories(categories),
        'total_questions': len(question_collection),
        'current_category': None
      })

    elif request.method == 'POST':
      data = request.get_json()
      try:
        question = Question(
          data.get('question', None),
          data.get('answer', None),
          data.get('category', None),
          data.get('difficulty', None)
        )

        question.insert()
        return jsonify({
          'success': True
        })
      except:
        abort(422)

  # delete a question
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    try:
      question = Question.query.filter_by(id=question_id).one_or_none()

      if question is None:
        abort(404)

      question.delete()

      return jsonify({
        'success': True
      })

    except:
      abort(422)

  # search for a keyword
  @app.route('/search', methods=['POST'])
  def search_questions():
    search_term = "%{}%".format(request.get_json().get('searchTerm'))
    questions = Question.query.filter(Question.question.like(search_term)).all()
    formatted_questions = [question.format() for question in questions]

    if len(questions) == 0:
      abort(404)

    return jsonify({
      'success': True,
      'questions': formatted_questions,
      'total_questions': len(questions),
      'current_category': None 
    })

  # get all question respective to category
  @app.route('/categories/<int:category_id>/questions', methods=['GET'])
  def get_category_questions(category_id):
    category = Category.query.filter_by(id=category_id).one_or_none()

    if category is None:
      abort(404)

    formatted_questions = [question.format() for question in category.questions]
    return jsonify({
      'success': True,
      'questions': formatted_questions,
      'total_questions': len(formatted_questions),
      'current_category': category.format()
    })

  # get next question or return None in next question
  @app.route('/quizzes', methods=['POST'])
  def play_quiz():
    data = request.get_json()
    previousQuestions = data.get('previous_questions', [])
    quizCategory = data.get('quiz_category', None)
    print(quizCategory['id'])
    if quizCategory:
      next_question = Question.query.filter_by(category=quizCategory['id']).filter(Question.id.notin_(previousQuestions)).order_by(func.random()).first()
    else:
      next_question = Question.query.filter(Question.id.notin_(previousQuestions)).order_by(func.random()).first()
    
    if next_question is not None:
      next_question = next_question.format()
    return jsonify({
      'success': True,
      'question': next_question
    })

  '''
  Error Handlers
  '''
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      'success': False,
      'error': 404,
      'message': 'resource not found'
    }), 404

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      'success': False,
      'error': 422,
      'message': 'unprocessable'
    }), 422

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      'success': False,
      'error': 400,
      'message': 'bad request'
    }), 400

  @app.errorhandler(405)
  def method_not_allowed(error):
    return jsonify({
      'success': False,
      'error': 405,
      'message': 'method not allowed'
    }), 405

  @app.errorhandler(500)
  def server_error(error):
    return jsonify({
      'success': False,
      'error': 500,
      'message': 'server error'
    }), 500


  return app

    