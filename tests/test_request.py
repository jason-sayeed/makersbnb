from lib.request import *
from datetime import date

def test_construct_request():
    request = Request(1, 1, 2024-1-1, 1, 2, False)
    assert request.id == 1
    assert request.spaceid == 1
    assert request.date == 2024-1-1
    assert request.guestid == 1
    assert request.hostid == 2
    assert request.approved == False

def test_format_request():
    request = Request(1, 1, date(2024, 1, 1), 1, 2, False)
    assert str(request) == 'Request(1, 1, 2024-01-01, 1, 2, False)'

def test_equality_request():
    request1 = Request(1, 1, date(2024, 1, 1), 1, 2, False)
    request2 = Request(1, 1, date(2024, 1, 1), 1, 2, False)
    assert request1 == request2