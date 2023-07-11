import pytest
from problem_2 import binary_search

def test_provided_examples():
    assert 2 == binary_search([1,3,5,6], 5)
    assert 1 == binary_search([1,3,5,6], 2)
    assert 4 == binary_search([1,3,5,6], 7)

def test_found():
    assert 5 == binary_search([1,3,5,6,8,10,16], 10)
    assert 3 == binary_search([1,3,5,6,8,10,16], 6)
    assert 6 == binary_search([1,3,5,6,8,10,16], 16)
    assert 0 == binary_search([1,3,5,6,8,10,16], 1)

def test_not_found():
    assert 0 == binary_search([1,3,5,6,8,9,10,14,16], 0)
    assert 7 == binary_search([1,3,5,6,8,10,16], 17)
    assert 4 == binary_search([1,3,5,6,8,10,16], 7)
    assert 6 == binary_search([1,3,5,6,8,10,16], 13)

def test_empty_list():
    assert 0 == binary_search([], 17)

def test_not_list():
    with pytest.raises(TypeError):
        binary_search(15, 17)

    with pytest.raises(TypeError):
        binary_search("15", 17)

def test_target_not_int():
    with pytest.raises(TypeError):
        binary_search([1,2,3,4,5], "")

    with pytest.raises(TypeError):
        binary_search([1,2,3,4,5], [])

def test_list_value_not_int():
    with pytest.raises(TypeError):
        binary_search([1,2,"3",4,5], 3)

    with pytest.raises(TypeError):
        binary_search([1,2,3,[],5], 4)


