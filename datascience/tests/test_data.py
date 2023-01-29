import unittest

# Write test case for method from data.py
class TestLibs(unittest.TestCase):

    # Write test case for download_data
    def test_download_data(self):
        from data import download_data
        import pathlib as pl
        # Write test case for download_data
        file_path = download_data()
        if not pl.Path(file_path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(file_path))

    # Write test case for remove_data
    def test_remove_data(self):
        from data import remove_data
        import pathlib as pl
        file_path = "src/titanic.csv"
        remove_data(file_path)
        if pl.Path(file_path).resolve().is_file():
            raise AssertionError("File still exists: %s" % str(file_path))