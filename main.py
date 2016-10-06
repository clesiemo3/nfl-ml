import nfldb
import config  # config.py with db info and creds


if __name__ == '__main__':
    print("hello world")
    db = nfldb.connect(database=config.DB_NAME, host=config.DB_HOST,
                       user=config.DB_USER, password=config.DB_PASS)
    q = nfldb.Query(db)

    q.game(season_year=2016, season_type='Regular')
    for pp in q.sort('passing_yds').limit(25).as_aggregate():
        print pp.player, pp.passing_yds, pp.passing_yds + pp.rushing_yds
