import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

ZOTERO_API_KEY = os.getenv('ZOTERO_API_KEY')
ZOTERO_USER_ID = os.getenv('ZOTERO_USER_ID')
CHATGPT_API_KEY = os.getenv('CHATGPT_API_KEY')
OBSIDIAN_VAULT_PATH = os.getenv('OBSIDIAN_VAULT_PATH')
ZOTERO_GROUP_ID = os.getenv('ZOTERO_GROUP_ID')
