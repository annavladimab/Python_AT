from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Films(Base):
    __tablename__ = 'films'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    director = Column(String)
    release_year = Column(Integer)

    def __init__(self, title, director, release_year):
        self.title = title
        self.director = director
        self.release_year = release_year

    @classmethod
    def display_all(cls, session):
        movies = session.query(cls).all()
        print('\nSelect All movies:')
        for film in movies:
            print(f'{film.title}, {film.director}, {film.release_year}')
        print('')

    @classmethod
    def delete_all(cls, session):
        session.query(cls).delete()
        session.commit()

    @classmethod
    def add_movies(cls, session, movie_list):
        for movie in movie_list:
            session.add(movie)
        session.commit()

    @classmethod
    def update_films(cls, session, title, new_title=None, new_director=None, new_release_year=None):
        movie_to_update = session.query(cls).filter(cls.title == title).first()

        if movie_to_update:
            if new_title:
                movie_to_update.title = new_title
            if new_director:
                movie_to_update.director = new_director
            if new_release_year:
                movie_to_update.release_year = new_release_year

            session.commit()
            print(f'Updated movie with title "{title}"')
        else:
            print(f'Movie with title "{title}" not found')


engine = create_engine('sqlite:///films.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


#Add queries
film1 = Films("The Goodfather", "Francis Coppola", 1972)
film2 = Films("Shindler's List", "Steven Spilberg", 1993)
film3 = Films("Forest Gump", "Robert Zemeckis", 1994)

Films.add_movies(session, [film1, film2, film3])

#Update  query
Films.update_films(session, "The Godfather 2", new_director="Francis Coppola II", new_release_year=1974)

#Select query
Films.display_all(session)

#Delete
Films.delete_all(session)

session.close()


