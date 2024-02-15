# File: test_integer_list.py
import pytest
from integer_list import IntegerList

@pytest.fixture
def integer_list():
    return IntegerList()

@pytest.mark.parametrize("num_list, expected_average", [
    ([1, 2, 3, 4, 5], 3.0),
    ([10, 20, 30, 40, 50], 30.0),
    ([], None),
])
def test_get_average(integer_list, num_list, expected_average):
    for num in num_list:
        integer_list.add_integer(num)
    result = integer_list.get_average()
    assert result == expected_average
    print(f"Test get_average réussi. Liste : {num_list}, Moyenne attendue : {expected_average}, Moyenne obtenue : {result}")

@pytest.mark.parametrize("nums_to_add, expected_integers", [
    ([1, 2, 3], [1, 2, 3]),
    ([10, 20, 30], [10, 20, 30]),
    ([], []),
])
def test_add_integer(integer_list, nums_to_add, expected_integers):
    for num in nums_to_add:
        integer_list.add_integer(num)
    result = integer_list.integers
    assert result == expected_integers
    print(f"Test add_integer réussi. Nombres à ajouter : {nums_to_add}, Liste attendue : {expected_integers}, Liste obtenue : {result}")

@pytest.mark.parametrize("nums_to_remove, expected_integers", [
    ([1, 2, 3], []),
    ([10, 20, 30], []),
    ([], []),
])
def test_remove_integer(integer_list, nums_to_remove, expected_integers):
    integer_list.integers = [1, 2, 3, 4, 5, 10, 20, 30]
    for num in nums_to_remove:
        integer_list.remove_integer(num)
    result = integer_list.integers
    assert result == expected_integers
    print(f"Test remove_integer réussi. Nombres à supprimer : {nums_to_remove}, Liste attendue après suppression : {expected_integers}, Liste obtenue : {result}")
@pytest.mark.parametrize("num_list, expected_max", [
    ([1, 2, 3, 4, 5], 5),
    ([10, 20, 30, 40, 50], 50),
    ([], None),
])
def test_get_max(integer_list, num_list, expected_max):
    for num in num_list:
        integer_list.add_integer(num)
    result = integer_list.get_max()
    assert result == expected_max
    print(f"Test get_max réussi. Liste : {num_list}, Max attendu : {expected_max}, Max obtenu : {result}")

@pytest.mark.parametrize("num_list, expected_min", [
    ([1, 2, 3, 4, 5], 1),
    ([10, 20, 30, 40, 50], 10),
    ([], None),
])
def test_get_min(integer_list, num_list, expected_min):
    for num in num_list:
        integer_list.add_integer(num)
    result = integer_list.get_min()
    assert result == expected_min
    print(f"Test get_min réussi. Liste : {num_list}, Min attendu : {expected_min}, Min obtenu : {result}")

if __name__ == '__main__':
    pytest.main()
