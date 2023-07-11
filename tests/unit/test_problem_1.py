import pytest
from problem_1 import check_duplicates

def test_provided_examples():
    assert True == check_duplicates([1,2,3,1])
    assert False == check_duplicates([1,2,3,4])
    assert True == check_duplicates([1,1,1,3,3,4,3,2,4,2])

def test_duplicates():
    result = check_duplicates([1,2,3,1])
    assert result == True

    result = check_duplicates([3,3,3,3])
    assert result == True

    result = check_duplicates([1,1,1,3,3,4,3,2,4,2])
    assert result == True

def test_no_duplicates():
    result = check_duplicates([1,2,3,4])
    assert result == False

    result = check_duplicates([3,5,8,50])
    assert result == False

    result = check_duplicates([1,80,98,45,12,4,7,158,47,19])
    assert result == False

def test_empty_list():
    result = check_duplicates([])
    assert result == False

def test_not_list():
    with pytest.raises(TypeError):
        check_duplicates("dexcom")
    with pytest.raises(TypeError):
        check_duplicates(5)

def test_list_value_not_int():
    with pytest.raises(TypeError):
        check_duplicates([1,"2",3,4])
    with pytest.raises(TypeError):
        check_duplicates(["hello","dexcom","fullstack","software"])
    with pytest.raises(TypeError):
        check_duplicates(["1,80,98,45,12,4,7,158,47,19"])


