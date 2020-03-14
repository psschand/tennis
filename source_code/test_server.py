import unittest
from source_code.server import app, db


class TennisTestCase(unittest.TestCase):
    """This class represents test case"""

    def setUp(self):
        """Define test variables and initialize app."""

        self.batch_tennis_data = [
            {
                "ATP": "11",
                "Court": "Brisbane International",
                "Date": "02-01-2011",
                "Location": "ATP250",
                "Loser": "Outdoor",
                "Round": "Hard",
                "Series": "1st Round",
                "Surface": "49",
                "Tournament": "Istomin D.",
                "Winner": "De Bakker T."
            },

            {
                "ATP": "12",
                "Court": "Brisbane International",
                "Date": "02-01-2011",
                "Location": "ATP250",
                "Loser": "Outdoor",
                "Round": "Hard",
                "Series": "2nd Round",
                "Surface": "49",
                "Tournament": "Berrer M.",
                "Winner": "Sela D."
            },
            {
                "ATP": "13",
                "Court": "Chennai",
                "Date": "02-01-2016",
                "Location": "ATP250",
                "Loser": "Outdoor",
                "Round": "Hard",
                "Series": "2nd Round",
                "Surface": "49",
                "Tournament": "Berdych T.",
                "Winner": "Phau B."
            }
        ]
        self.tennis_data = {
            "ATP": "1",
            "Court": "TestCourt",
            "Date": "TestDate",
            "Location": "TestLocation",
            "Loser": "TestLoser",
            "Round": "TesrRound",
            "Series": "TestSeries",
            "Surface": "TestSurface",
            "Tournament": "TestTournament",
            "Winner": "TestWinner"
        }
        db.connect()

    # def test_batch(self):
    #     """Test batch API can create a list (POST request)"""
    #     res = app.test_client().post('/batch', data=self.batch_tennis_data)
    #     self.assertEqual(res.status_code, 200)
    #     # self.assertIn('successful', str(res.data))

    def test_hello(self):
        response = app.test_client().get('/hello')
        assert response.status_code == 200
        assert response.data == b'{"hello":"world"}\n'

    # def test__delete(self):
    #     """Test API can delete DELETE ."""
    #     res: object = app.test_client().post('/batch', data=self.batch_tennis_data)
    #     self.assertEqual(res.status_code, 200)
    #     re = db.delete('1')
    #     self.assertTrue(re)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
