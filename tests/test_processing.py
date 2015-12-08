# content of test_processing.py

from reversal.processing import process_google_finance_history

def test_process_google_finance_history():
    np_arr = process_google_finance_history('tests/mock/google_finance.csv')

    # verify if the shape is in (3 rows, 6 columns)
    assert np_arr.shape == (3, 6)

    # verify the values in the first row
    for i, val in enumerate([1133933400.0, 62.5, 63.5, 61.9, 62.5, 41492000.0]):
        assert np_arr[0][i] == val

    # verify the relative timestamp is converted correctly
    for i in range(3):
        assert np_arr[i][0] == 1133933400.0 + i*86400