import pytest

array = [1, 1, 1, 2, 2, 3, 4, 4, 1, 2, 2]
result = []

def compress_numbers(massiv):
    global result
    
    if not massiv:
        return []
    
    result = [massiv[0]]
    
    for i in range(1, len(massiv)):
        if massiv[i] != massiv[i - 1]:
            result.append(massiv[i])

    return result
    

print(compress_numbers(array)) #[1, 2, 3, 4, 1, 2]


def test_simple_numb():
    assert compress_numbers([1, 1, 2, 2, 3]) == [1, 2, 3]
    assert compress_numbers([0, 0, 1, 1, 0]) == [0, 1, 0]

def test_empty_array():
    assert compress_numbers([]) == []
    
def test_floats():
    assert compress_numbers([1.5, 1.5, 2.5, 2.5, 3, 3.5]) == [1.5, 2.5, 3, 3.5]
    
def test_no_duplicat():
    assert compress_numbers([1, 2, 3]) == [1, 2, 3]
    
def test_negative_numb():
    assert compress_numbers([-1, -1, -2, -2, 3, -3]) == [-1, -2, 3, -3]
    