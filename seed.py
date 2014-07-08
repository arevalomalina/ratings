import model
import csv
import datetime

def load_users(session):
    # use u.user
    with open('seed_data/u.user', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        for row in reader:
            #print row
            user = model.User(id=row[0], age=row[1], zipcode=row[4])
            session.add(user)
        session.commit()

def load_movies(session):
    with open('seed_data/u.item', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        for row in reader:
            if row[2] == '':
                continue
            released = datetime.datetime.strptime(row[2], "%d-%b-%Y")
            title_decoded = row[1].decode("latin-1")
            movie = model.Movie(
                id=row[0],
                name=title_decoded, 
                released_at=released, 
                imdb_url=row[4]
            )
            session.add(movie)
        session.commit()

def load_ratings(session):
    with open('seed_data/u.data', 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            rating = model.Rating(
                movie_id=row[1],
                user_id=row[0],
                rating=row[2]
            )
            session.add(rating)
        session.commit()
    # use u.data
    

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    #load_users(session)
    #load_movies(session)
    load_ratings(session)

if __name__ == "__main__":
    s= model.connect()
    main(s)
