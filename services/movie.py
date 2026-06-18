from typing import List

from django.db.models import QuerySet

from db.models import Movie


def get_movies(
        genres_ids: List[int] = None,
        actors_ids: List[int] = None
) -> QuerySet[Movie]:
    if genres_ids is not None and actors_ids is not None:
        return Movie.objects.filter(
            genres__id__in=genres_ids,
            actors__id__in=actors_ids
        ).all().distinct()
    if genres_ids is not None and actors_ids is None:
        return Movie.objects.filter(
            genres__id__in=genres_ids
        ).all().distinct()
    if genres_ids is None and actors_ids is not None:
        return Movie.objects.filter(
            actors__id__in=actors_ids
        ).all().distinct()
    return Movie.objects.all().distinct()


def get_movie_by_id(movie_id: int) -> QuerySet[Movie]:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: List[int] = None,
        actors_ids: List[int] = None
) -> QuerySet[Movie]:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids is not None:
        movie.genres.set(genres_ids)
    if actors_ids is not None:
        movie.actors.set(actors_ids)
    return movie
