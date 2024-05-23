import sys
import os

# Add the parent directory of src to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.config import ZOTERO_GROUP_ID

from zotero_integration import fetch_zotero_data, print_group_collections
# from chatgpt_integration import get_chatgpt_response
# from obsidian_integration import list_obsidian_notes, read_obsidian_note

def main():
    # Fetch data from Zotero
    zotero_data = print_group_collections(ZOTERO_GROUP_ID)
    print("Zotero Data:", zotero_data)
    
    # # Get a response from ChatGPT
    # prompt = "Summarize the following data:\n" + str(zotero_data)
    # chatgpt_response = get_chatgpt_response(prompt)
    # print("ChatGPT Response:", chatgpt_response)
    
    # # List and read notes from Obsidian
    # notes = list_obsidian_notes()
    # print("Obsidian Notes:", notes)
    
    # if notes:
    #     note_content = read_obsidian_note(notes[0])
    #     print("First Note Content:", note_content)

if __name__ == "__main__":
    main()
