from pyzotero import zotero
from src.config import ZOTERO_API_KEY, ZOTERO_USER_ID

def fetch_zotero_data():
    zot = zotero.Zotero(ZOTERO_USER_ID, 'user', ZOTERO_API_KEY)
    items = zot.items()
    return items

# Example function to fetch items from a specific collection
def fetch_group_collection_items(group_id, collection_id):
    zot = zotero.Zotero(group_id, 'group', ZOTERO_API_KEY)
    items = zot.collection_items(collection_id)
    return items

def print_group_collections(group_id):
    zot = zotero.Zotero(group_id, 'group', ZOTERO_API_KEY)
    collections = zot.collections()
    for collection in collections:
        print(f"Name: {collection['data']['name']}, ID: {collection['data']['key']}")