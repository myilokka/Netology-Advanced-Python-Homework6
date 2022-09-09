import unittest
import functions as func
from parameterized import parameterized
from unittest.mock import patch
import fixtures as fix


class TestFunctions(unittest.TestCase):

    def setUp(self) -> None:
        ...

    def tearDown(self) -> None:
        ...

    @parameterized.expand(fix.fixture_check_document_existance)
    def test_check_document_existance(self, user_doc_number, expected_result):
        self.assertIs(func.check_document_existance(user_doc_number), expected_result)

    @parameterized.expand(fix.fixture_get_doc_owner_name)
    def test_get_doc_owner_name(self, user_doc_number, expected_result):
        with patch('builtins.input', return_value=user_doc_number):
            result = func.get_doc_owner_name()
            self.assertMultiLineEqual(expected_result, result)

    @parameterized.expand(fix.fixture_test_remove_doc_from_shelf)
    def test_remove_doc_from_shelf(self, doc_number):
        expected_result = None
        shelf = None
        for directory_number, directory_docs_list in func.directories.items():
            if doc_number in directory_docs_list:
                shelf = directory_number
                expected_result = len(directory_docs_list)-1
        func.remove_doc_from_shelf(doc_number)
        result = len(func.directories[shelf])
        self.assertEqual(expected_result, result)

    @parameterized.expand(fix.fixture_add_new_shelf)
    def test_add_new_shelf(self, shelf_number, expected_result, mock_shelf_number):
        if shelf_number:
            shelf, result = func.add_new_shelf(shelf_number)
            self.assertEqual(expected_result, result)
        else:
            with patch('builtins.input', return_value=mock_shelf_number):
                shelf, result = func.add_new_shelf(mock_shelf_number)
                self.assertEqual(expected_result, result)

    @parameterized.expand(fix.fixture_append_doc_to_shelf)
    def test_append_doc_to_shelf(self, doc_number, mock_shelf_number):
        with patch('functions.add_new_shelf', return_value=mock_shelf_number):
            expected_result = len(func.directories[mock_shelf_number])+1
            func.append_doc_to_shelf(doc_number, mock_shelf_number)
            result = len(func.directories[mock_shelf_number])
            self.assertEqual(expected_result, result)

    @parameterized.expand(fix.fixture_delete_doc)
    def test_delete_doc(self, mock_doc_number, expected_result):
        with patch('builtins.input', return_value=mock_doc_number):
            result = func.delete_doc()
            self.assertEqual(expected_result, result)

    @parameterized.expand(fix.fixture_get_doc_shelf)
    def test_get_doc_shelf(self, mock_doc_number, expected_result):
        with patch('builtins.input', return_value=mock_doc_number):
            result = func.get_doc_shelf()
            self.assertEqual(expected_result, result)

    @parameterized.expand(fix.fixture_add_new_doc)
    def test_add_new_doc(self, mock_doc_number, mock_doc_type, mock_doc_owner_name, mock_shelf_number):
        with patch('builtins.input', lambda *args: (mock_doc_number, mock_doc_type, mock_doc_owner_name, mock_shelf_number)):
            expected_result = len(func.documents)+1
            func.add_new_doc()
            result = len(func.documents)
            self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
