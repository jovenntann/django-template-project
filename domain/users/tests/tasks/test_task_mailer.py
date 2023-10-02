from django.test import TestCase

from ...tasks.task_mailer import check_if_valid_email, send_email_verification


# Create your tests here.
class CheckIfValidEmailTestCase(TestCase):

    def test_should_return_false_for_invalid_email(self):
        """Should return False is invalid email address"""
        is_valid_email = check_if_valid_email('jovenntann')
        self.assertEqual(is_valid_email, False)

    def test_should_return_true_for_valid_email(self):
        """Should return True for valid email address"""
        is_valid_email = check_if_valid_email('joven@old.st')
        self.assertEqual(is_valid_email, True)

    def test_should_return_false_if_empty_email(self):
        """Should return False for empty email address"""
        is_valid_email = check_if_valid_email('')
        self.assertEqual(is_valid_email, False)

    # def test_should_return_false_if_no_arguments(self):
    #     """Should return False for no argument"""
    #     with self.assertRaises(Exception):
    #         check_if_valid_email()
    #
    # def test_should_raise_exception_if_data_type_of_argument_is_not_valid(self):
    #     """Should raise exception if data_type of argument is not valid"""
    #     with self.assertRaises(Exception):
    #         check_if_valid_email(None)


class SendFeedbackEmailTaskTestCase(TestCase):

    def test_should_return_false_for_invalid_email(self):
        """Should return False is invalid email address"""
        email_task = send_email_verification('jovenntann', 'Hello')
        self.assertEqual(email_task, False)

    def test_should_return_true_for_valid_email(self):
        """Should return True for valid email address"""
        email_task = send_email_verification('joven@old.st', 'Hello')
        self.assertEqual(email_task, True)

    def test_should_return_false_if_empty_email(self):
        """Should return False for empty email address"""
        email_task = send_email_verification('', 'Hello')
        self.assertEqual(email_task, False)
