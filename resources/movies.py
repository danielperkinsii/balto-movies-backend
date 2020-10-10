import models
from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict

movie = Blueprint('movies', 'movie')

@movie.route('/', methods=["GET"])
def get_hundred_movies():
    ## find the movies and change each one to a dictionary into a new array
    try:
        movies = [model_to_dict(movie) for movie in models.Movie.select().limit(100)]
        print(movies)
        return jsonify(data=movies, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})

@movie.route('/', methods=["POST"])
def create_movies():
    body = request.get_json()
    print(body)
    new_movie = models.Movie.create(**body)
    movie_data = model_to_dict(new_movie)
    return jsonify(data=movie_data, status={'code': 200, 'message': 'Success'})

@movie.route('/<id>', methods=["GET"])
def get_one_movie(id):
    print(id, 'this is the id')
    movie = models.Movie.get_by_id(id)
    movie_dict = model_to_dict(movie)
    return jsonify(data=movie_dict, status={'code': 200, 'message': 'Success'})

@movie.route('/<id>', methods=['PUT'])
def update_movie(id):
    payload = request.get_json()
    update_query = models.Movie.update(**payload).where(models.Movie.id == id)

    update_query.execute()

    update_movie = models.Movie.get_by_id(id)

    return jsonify(data=model_to_dict(update_movie), message="Successfully update movie with id {}".format(id), status={'code': 200, 'message': 'Success'})

@movie.route('/<id>', methods=['DELETE'])
def delete_movie(id):
    delete_query = models.Movie.delete().where(models.Movie.id == id)
    delete_query.execute() # you need this for delete and update
    return jsonify(
        data={},
        message="Successfully deleted movie with id {}".format(id),
        status={'code': 200, 'message': 'Success'}
    )
