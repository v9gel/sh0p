from flask import Flask
from flask import make_response
from flask import jsonify
import gensim
from flask_cors import CORS, cross_origin
import random

# Товаров в базе
A = 1
B = 49690

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/api/<products>')
@cross_origin()
def show_rec(products):
	p = products.split(',')
	model1 = gensim.models.Word2Vec.load("word2vec.model")
	t = model1.wv.most_similar_cosmul(positive=p)
	array = []

	for similar, dict in t:
		array.append(similar)
	# show the user profile for that user
	ret = jsonify(array) 

	return ret


#Холодный старт
@app.route('/api/')
@cross_origin()
def show_rec_def():
	array = []

	for similar in range(1, 25):
		array.append(str(random.randint(A, B)))
	# show the user profile for that user
	return jsonify(array)


if __name__ == '__main__':
  app.run()
