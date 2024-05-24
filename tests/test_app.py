from playwright.sync_api import Page, expect
from lib.space import Space
from lib.space_repository import *


def test_create_user(db_connection, page, test_web_address):
    db_connection.seed("seeds/makersbnb_test.sql")
    page.goto(f"http://{test_web_address}/home")
    page.fill("input[name=new_username]", "mattd@example.com")
    # page.fill("input[name=password]", "jasonscool")
    # page.click("text='Sign Up")
    # expect(page.url).toBe(f"http://{test_web_address}/spaces")

# def test_create_user(db_connection, page, test_web_address):
#     db_connection.seed("seeds/makersbnb_test.sql")
#     page.goto(f"http://{test_web_address}/home")
#     page.fill("input[name=username]", "mattd@example.com")
#     page.fill("input[name=password]", "jasonscool")
#     page.click("text='Sign Up")
#     expect(page.url).toBe(f"http://{test_web_address}/spaces")


# def test_successful_login(db_connection, page, test_web_address):
#     db_connection.seed("seeds/makersbnb_test.sql")
#     page.goto(f"http://{test_web_address}/home")
#     page.fill("input[name=username]", "mattd@example.com")
#     page.fill("input[name=password]", "jasonscool")
#     page.click("text='Sign In")
#     expect(page.url).toBe(f"http://{test_web_address}/spaces")

    
# # def test_successful_login()


"""
test for creating a new space
should just insert values for the moment 
"""

def test_create_a_new_space(web_client,db_connection):
    db_connection.seed('seeds/makersbnb_test.sql')
    response = web_client.post('/spaces', data ={
        'description': 'lorem ipsum',
        'price': '70',
        'user_id': '7',
        'name': 'test_space',
        'fromdate': '13-01-2024',
        'todate': '15-01-2024',
    })
    all_response = web_client.get('/spaces')
    assert response.status_code == 200
    assert all_response.data.decode('utf-8') == "Space(1, house with a pool, 99.99, 1, pool house, 01-01-2024, 31-01-2024, ['01-01-2024', '02-01-2024', '03-01-2024', '04-01-2024', '05-01-2024', '06-01-2024', '07-01-2024', '08-01-2024', '09-01-2024', '10-01-2024', '11-01-2024', '12-01-2024', '13-01-2024', '14-01-2024', '15-01-2024', '16-01-2024', '17-01-2024', '18-01-2024', '19-01-2024', '20-01-2024', '21-01-2024', '22-01-2024', '23-01-2024', '24-01-2024', '25-01-2024', '26-01-2024', '27-01-2024', '28-01-2024', '29-01-2024', '30-01-2024', '31-01-2024'])\nSpace(2, house on a lake, 99.99, 2, lake house, 02-01-2024, 03-01-2024, ['02-01-2024', '03-01-2024'])\nSpace(3, house on a hill, 99.99, 3, hill house, 01-02-2024, 02-02-2024, ['01-02-2024', '02-02-2024'])\nSpace(4, lorem ipsum, 70.0, 7, test_space, 13-01-2024, 15-01-2024, ['13-01-2024', '14-01-2024', '15-01-2024'])\n"

def test_create_space_then_book(web_client,db_connection):
    db_connection.seed('seeds/makersbnb_test.sql')
    repository = SpaceRepository(db_connection)
    response = web_client.post('/spaces', data ={
        'description': 'lorem ipsum',
        'price': '70',
        'user_id': '7',
        'name': 'test_space',
        'fromdate': '13-01-2024',
        'todate': '15-01-2024',
    })
    repository.remove_date(4,"13-01-2024","15-01-2024")
    all_response = web_client.get('/spaces')
    assert response.status_code == 200
    assert all_response.data.decode('utf-8') == "Space(1, house with a pool, 99.99, 1, pool house, 01-01-2024, 31-01-2024, ['01-01-2024', '02-01-2024', '03-01-2024', '04-01-2024', '05-01-2024', '06-01-2024', '07-01-2024', '08-01-2024', '09-01-2024', '10-01-2024', '11-01-2024', '12-01-2024', '13-01-2024', '14-01-2024', '15-01-2024', '16-01-2024', '17-01-2024', '18-01-2024', '19-01-2024', '20-01-2024', '21-01-2024', '22-01-2024', '23-01-2024', '24-01-2024', '25-01-2024', '26-01-2024', '27-01-2024', '28-01-2024', '29-01-2024', '30-01-2024', '31-01-2024'])\nSpace(2, house on a lake, 99.99, 2, lake house, 02-01-2024, 03-01-2024, ['02-01-2024', '03-01-2024'])\nSpace(3, house on a hill, 99.99, 3, hill house, 01-02-2024, 02-02-2024, ['01-02-2024', '02-02-2024'])\nSpace(4, lorem ipsum, 70.0, 7, test_space, 13-01-2024, 15-01-2024, [])\n"

# since the listings page is not linked yet
# i want the outcome of the /POST request 
# to be that it returns the value from db

    # assert response.data.decode('utf-8') == "" \
        # "Space(4,  lorem ipsum, 70, 7, test_space, 13-01-2024, 15-01-2024)"
    assert response.data.decode('utf-8') == 'Listing added'
"""
test for making a booking
"""

"""
test for after booking made
date unavailable
"""

"""
test to see all spaces
"""

"""
test for approving a booking
"""


# def test_find_one_user_for_login
    


def test_construct():
    space = Space(1, "test description", 99.99, 1, "test name", '01-01-2024', '31-01-2024')
    assert space.id == 1
    assert space.description == "test description"
    assert space.price == 99.99
    assert space.user_id == 1
    assert space.name == "test name"
    assert space.free_dates == ['01-01-2024', '02-01-2024', '03-01-2024', '04-01-2024', '05-01-2024', '06-01-2024', '07-01-2024', '08-01-2024', '09-01-2024', '10-01-2024', '11-01-2024', '12-01-2024', '13-01-2024', '14-01-2024', '15-01-2024', '16-01-2024', '17-01-2024', '18-01-2024', '19-01-2024', '20-01-2024', '21-01-2024', '22-01-2024', '23-01-2024', '24-01-2024', '25-01-2024', '26-01-2024', '27-01-2024', '28-01-2024', '29-01-2024', '30-01-2024', '31-01-2024']



    # Retrieve all spaces

def test_get_all_spaces(web_client, db_connection):
    db_connection.seed('seeds/makersbnb_test.sql')
    response = web_client.get('/spaces')
    
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ("Space(1, house with a pool, 99.99, 1, pool house, 01-01-2024, 31-01-2024, ['01-01-2024', '02-01-2024', '03-01-2024', '04-01-2024', '05-01-2024', '06-01-2024', '07-01-2024', '08-01-2024', '09-01-2024', '10-01-2024', '11-01-2024', '12-01-2024', '13-01-2024', '14-01-2024', '15-01-2024', '16-01-2024', '17-01-2024', '18-01-2024', '19-01-2024', '20-01-2024', '21-01-2024', '22-01-2024', '23-01-2024', '24-01-2024', '25-01-2024', '26-01-2024', '27-01-2024', '28-01-2024', '29-01-2024', '30-01-2024', '31-01-2024'])\nSpace(2, house on a lake, 99.99, 2, lake house, 02-01-2024, 03-01-2024, ['02-01-2024', '03-01-2024'])\nSpace(3, house on a hill, 99.99, 3, hill house, 01-02-2024, 02-02-2024, ['01-02-2024', '02-02-2024'])\n")