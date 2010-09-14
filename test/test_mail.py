import unittest


class SendMailNotificationTest(unittest.TestCase):
    def testMail(self):
        post_data  = {
            'to':'voskoboynikvlad@gmail.com',
            'body':'blah_blah_blah',
            'subject':'mySubject'
        }
        response = self.client.get('http://localhost:8080/send_notification/',post_data)
        self.assertEqual(response.status_code, 200)
