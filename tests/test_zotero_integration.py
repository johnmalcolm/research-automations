import unittest
from src.zotero_integration import fetch_zotero_data, fetch_collection_items

class TestZoteroIntegration(unittest.TestCase):
    def test_fetch_zotero_data(self):
        data = fetch_zotero_data()
        self.assertIsInstance(data, list)
    
    def test_fetch_collection_items(self):
        collection_id = 'your_collection_id_here'
        data = fetch_collection_items(collection_id)
        self.assertIsInstance(data, list)

if __name__ == '__main__':
    unittest.main()
