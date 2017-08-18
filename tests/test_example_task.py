import pytest

import lib


@pytest.mark.parametrize("numbers,lcm", [
    ([2, 3], 6),
    ([10, 100], 100),
    ([15, 5, 3, 88], 1320),
    ([32343577, 987954, 321654], 1713020177846591922)
])
def test_lcm(numbers, lcm):
    """ lcm finds the Least Common Multiple of it's *args """
    assert lib.lcm(*numbers) == lcm


@pytest.mark.parametrize("rows", [1, 77, 10947])
def test_rows_of_random_numbers_rows(rows):
    """ rows_of_random_numbers generates rows=x rows """
    counter = 0
    for row in lib.rows_of_random_numbers(rows=rows):
        counter += 1
    assert counter == rows


@pytest.mark.parametrize("count", [1, 3, 8])
def test_rows_of_random_numbers_count(count):
    """ rows_of_random_numbers generates rows with <count> entries """
    for row in lib.rows_of_random_numbers(count=count):
        assert len(row) == count


@pytest.mark.parametrize("minimum,maximum", [
    (288, 388), (1, 9), (4537492, 9853345)
])
def test_rows_of_random_numbers_minimum_maximum(minimum, maximum):
    """
    rows_of_random_numbers generates ints within minimum & maximum range

    Note that since these numbers are being randomly generated this test isn't
    _super_ great.
    """
    for row in lib.rows_of_random_numbers(minimum=minimum, maximum=maximum):
        for item in row:
            assert item >= minimum and item <= maximum


@pytest.mark.parametrize("iterable", [
    [(3, 9), (17, 38), (764, 985)],
    [(453, 174, 9), (435, 12, 98), (347216, 7820984, 98749)],

])
def test_generate_lcm_rows(iterable):
    """ generate_lcm_rows prepends each row with the LCM """
    for row in lib.generate_lcm_rows(iterable):
        lcm, *original_row = row
        assert lcm == lib.lcm(*original_row)
