import io
from unittest import mock

import pytest

import lib
from tasks.example_task import RandomNumbers, LeastCommonMultiple


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


@pytest.fixture
def single_file_output():
    """
    Mocks a single-file output for luigi.Task.output()

    Usage:
    >>> output_file, output_mock = single_file_output
    >>> task.output = output_mock
    >>> task.run()
    >>> value = output_file.getvalue()
    """
    output_file = io.StringIO()
    output_file.close = mock.Mock()  # StringIO.close() flushes the buffer :(

    output_mock = mock.Mock()
    output_mock.open = mock.MagicMock(return_value=output_file)

    return output_file, mock.MagicMock(return_value=output_mock)


def test_task_random_numbers_run_writes_to_output(single_file_output):
    """ RandomNumbers.run writes a csv of random numbers to self.output() """
    output_file, output_mock = single_file_output

    task = RandomNumbers(number=1)
    with mock.patch.object(task, 'output', output_mock):
        task.run()

        assert output_mock.called
        output_mock().open.assert_called_with('w')
        assert output_file.close.called

        assert output_file.getvalue()


@pytest.mark.parametrize('number', [1, 43, 759])
def test_task_random_numbers_output(number):
    """
    RandomNumbers.output matches it's unique parameters

    Luigi determines whether a task has already been completed based on
    whether it can match a task to it's output: that's a lukewarm argument
    for testing this.
    """
    task = RandomNumbers(number=number)

    output = task.output()
    assert output.path.endswith('random_{}.csv'.format(number))


def test_task_least_common_multiple_reads_from_requires(single_file_output):
    """ LeastCommonMultiples.run uses all of the _requires_ files"""
    output_mock = single_file_output[1]

    task = LeastCommonMultiple(count=3)
    task.output = output_mock

    input_files = [mock.MagicMock(), mock.MagicMock()]
    task.input = mock.Mock(return_value=input_files)

    task.run()

    for input_file in input_files:
        input_file.open.assert_called_with('r')
