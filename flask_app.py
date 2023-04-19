
# A very simple Flask Hello World app for you to get started with...

import flask
import os
from flask import Flask, request
import pickle
import spacy
# classifier = spacy.load("/home/evankozierok/orpheus-ai/combo")
# spacy.load('en_core_web_md')
# from flask_restful import Resource, Api, reqparse
# import classy_classification

app = Flask(__name__)
# api = Api(app)

# print(os.getcwd())
with open('/home/evankozierok/orpheus-ai/classifier.pickle', 'br') as f:
    classifier_old = pickle.load(f)

# spacy.require_cpu()

# parser = reqparse.RequestParser()
# parser.add_argument('lyrics', required=True, help='Lyrics cannot be blank!')

# class PredictGenre(Resource):
#     def post(self):
#         args = parser.parse_args()
#         lyrics = args['lyrics']
#         # process lyrics and predict genre
#         return {'genre': random_var}

# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}

# api.add_resource(PredictGenre, '/predict')
# api.add_resource(HelloWorld, '/')

random_var = 3.14
@app.route('/stuff', methods=['GET'])
def stuff():
    return {'genre': random_var}

@app.route('/predict', methods=['POST'])
def handle_predict():
    lyrics = request.json['lyrics']
    genres = classifier_old(lyrics)
    # genres = {'hello': 'world'}
    return genres


@app.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')


if __name__ == '__main__':
    app.debug=True
    app.run()
