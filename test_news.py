import unittest
from unittest.mock import patch, MagicMock
import news


class TestNews(unittest.TestCase):

    @patch('news.requests.get')
    def test_get_hn_stories(self, mock_get):
        # Mock response text
        mock_html = """  
        <html>  
            <body>  
                <table>  
                    <tr class="athing"><td class="titleline">  
                        <a href="https://example.com/story1" class="titlelink">Story 1</a>  
                    </td></tr>  
                    <tr class="subtext">  
                        <span class="score">300 points</span>  
                    </tr>  
                </table>  
            </body>  
        </html>  
        """
        # Prepare the mock response
        mock_response = MagicMock()
        mock_response.text = mock_html
        mock_get.return_value = mock_response

        links, subtext = news.get_hn_stories('https://news.ycombinator.com/news')

        # Test the links output
        self.assertEqual(len(links), 1)
        self.assertEqual(links[0].getText(), 'Story 1')

        # Test the subtext output
        self.assertEqual(len(subtext), 1)
        self.assertEqual(subtext[0].select('.score')[0].getText(), '300 points')

    def test_create_custom_hn_with_votes(self):
        links = [MagicMock(getText=lambda: 'Story 1', get=lambda x: 'https://example.com/story1'),
                 MagicMock(getText=lambda: 'Story 2', get=lambda x: 'https://example.com/story2')]
        subtext = [MagicMock(select=lambda x: [MagicMock(getText=lambda: '300 points')]),
                   MagicMock(select=lambda x: [MagicMock(getText=lambda: '150 points')])]

        hn = news.create_custom_hn(links, subtext)

        # Test that only the story with over 200 points is returned
        self.assertEqual(len(hn), 1)
        self.assertEqual(hn[0], 'Story 1  (300)  https://example.com/story1')

    def test_create_custom_hn_no_high_points(self):
        links = [MagicMock(getText=lambda: 'Story 1', get=lambda x: 'https://example.com/story1')]
        subtext = [MagicMock(select=lambda x: [MagicMock(getText=lambda: '150 points')])]

        hn = news.create_custom_hn(links, subtext)

        # No stories should be returned
        self.assertEqual(hn, [])


if __name__ == '__main__':
    unittest.main()
