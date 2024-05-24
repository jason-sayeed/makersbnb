from lib.space_repository import *
from lib.space import *

def test_all(db_connection):
    db_connection.seed('seeds/makersbnb_test.sql')
    repository = SpaceRepository(db_connection)
    spaces = repository.all()
    assert spaces == [Space(1, 'house with a pool', 99.99, 1, 'pool house', '01-01-2024', '31-01-2024', ['01-01-2024', '02-01-2024', '03-01-2024', '04-01-2024', '05-01-2024', '06-01-2024', '07-01-2024', '08-01-2024', '09-01-2024', '10-01-2024', '11-01-2024', '12-01-2024', '13-01-2024', '14-01-2024', '15-01-2024', '16-01-2024', '17-01-2024', '18-01-2024', '19-01-2024', '20-01-2024', '21-01-2024', '22-01-2024', '23-01-2024', '24-01-2024', '25-01-2024', '26-01-2024', '27-01-2024', '28-01-2024', '29-01-2024', '30-01-2024', '31-01-2024']), Space(2, 'house on a lake', 99.99, 2, 'lake house', '02-01-2024', '03-01-2024', ['01-02-2024', '02-02-2024', '03-02-2024', '04-02-2024', '05-02-2024', '06-02-2024', '07-02-2024', '08-02-2024', '09-02-2024', '10-02-2024', '11-02-2024', '12-02-2024', '13-02-2024', '14-02-2024', '15-02-2024', '16-02-2024', '17-02-2024', '18-02-2024', '19-02-2024', '20-02-2024', '21-02-2024', '22-02-2024', '23-02-2024', '24-02-2024', '25-02-2024', '26-02-2024', '27-02-2024', '28-02-2024', '29-02-2024', '01-03-2024']), Space(3, 'house on a hill', 99.99, 3, 'hill house', '01-02-2024', '02-02-2024', ['02-01-2024', '03-01-2024', '04-01-2024', '05-01-2024', '06-01-2024', '07-01-2024', '08-01-2024', '09-01-2024', '10-01-2024', '11-01-2024', '12-01-2024', '13-01-2024', '14-01-2024', '15-01-2024', '16-01-2024', '17-01-2024', '18-01-2024', '19-01-2024', '20-01-2024', '21-01-2024', '22-01-2024', '23-01-2024', '24-01-2024', '25-01-2024', '26-01-2024', '27-01-2024', '28-01-2024', '29-01-2024', '30-01-2024', '31-01-2024', '01-02-2024', '02-02-2024'])]

def test_add_space(db_connection):
    db_connection.seed('seeds/makersbnb_test.sql')
    repository = SpaceRepository(db_connection)
    space = Space(None, 'test description', 99.99, 1, 'test name', '03-02-2024', '04-02-2024')
    repository.add(space)
    result = repository.all()
    print(result)
    assert space.id == 4
    assert result == [Space(1, 'house with a pool', 99.99, 1, 'pool house', '01-01-2024', '31-01-2024', ['01-01-2024', '02-01-2024', '03-01-2024', '04-01-2024', '05-01-2024', '06-01-2024', '07-01-2024', '08-01-2024', '09-01-2024', '10-01-2024', '11-01-2024', '12-01-2024', '13-01-2024', '14-01-2024', '15-01-2024', '16-01-2024', '17-01-2024', '18-01-2024', '19-01-2024', '20-01-2024', '21-01-2024', '22-01-2024', '23-01-2024', '24-01-2024', '25-01-2024', '26-01-2024', '27-01-2024', '28-01-2024', '29-01-2024', '30-01-2024', '31-01-2024']), Space(2, 'house on a lake', 99.99, 2, 'lake house', '02-01-2024', '03-01-2024', ['02-01-2024', '03-01-2024']), Space(3, 'house on a hill', 99.99, 3, 'hill house', '01-02-2024', '02-02-2024', ['01-02-2024', '02-02-2024']), Space(4, 'test description', 99.99, 1, 'test name', '03-02-2024', '04-02-2024', ['03-02-2024', '04-02-2024'])]

def test_find_one_date(db_connection):
    db_connection.seed('seeds/makersbnb_test.sql')
    repository = SpaceRepository(db_connection)
    filtered_spaces = repository.filter("01-01-2024")
    assert filtered_spaces == [1]

def test_find_multiple_dates(db_connection):
    db_connection.seed('seeds/makersbnb_test.sql')
    repository = SpaceRepository(db_connection)
    filtered_spaces = repository.filter("02-01-2024","03-01-2024")
    assert filtered_spaces == [1,2]

def test_remove_date(db_connection):
    db_connection.seed('seeds/makersbnb_test.sql')
    repository = SpaceRepository(db_connection)
    repository.remove_date(1,"01-01-2024")
    filtered_spaces = repository.filter("01-01-2024")
    assert filtered_spaces == []

# def test_remove_space(db_connection):
#     db_connection.seed('seeds/makersbnb_test.sql')
#     repository = SpaceRepository(db_connection)
#     repository.remove_space(1)
#     spaces = repository.all()
#     assert spaces == "blah blah blah"
# Luxury feature