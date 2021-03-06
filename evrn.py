# 
# A simple Evernote API script that creates a new note titled sys.argv(1) in the default notebook. 
#
# Requirements: 
# evernote SDK for python3 https://github.com/evernote/evernote-sdk-python3
# keyring: pip install keyring
#  
# Before running this, you must set your Evernote developer token with keyring as follows:
# python 
# >>> include keyring
# >>> keyring.set_password("evernote", "<consumer key>", "<developer token>")
# >>> quit()
# This secures the evernote credentials on the local machine, the script will then retrieve them using 
# keyring.get_password()
#  
# To run: python evrn.py <note title>
#

import os, sys
import keyring
import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types

from evernote.api.client import EvernoteClient

if len(sys.argv)<2:
    print('evrn: Usage: evrn.py <note title>')
    sys.exit(2)
else: 
    note_text = str(sys.argv[1])

auth_token = keyring.get_password("evernote", "sye")

# To use the production service, change sandbox=False and replace your
# developer token above with a token from https://www.evernote.com/api/DeveloperToken.action
# To access Sandbox service, set sandbox to True
# To access production (International) service, set both sandbox and china to False
# To access production (China) service, set sandbox to False and china to True

sandbox=True 
china=False

client = EvernoteClient(token=auth_token, sandbox=sandbox,china=china)

user_store = client.get_user_store()

version_ok = user_store.checkVersion(
    "Evernote EDAMTest (Python)",
    UserStoreConstants.EDAM_VERSION_MAJOR,
    UserStoreConstants.EDAM_VERSION_MINOR
)

if not version_ok:
    print("evrn: Evernote API is not up to date, exiting...") 
    exit(1)

note_store = client.get_note_store()

print()
print("evrn: Creating a new note in the default notebook")

note = Types.Note()
note.title = note_text

note.content = '<?xml version="1.0" encoding="UTF-8"?>'
note.content += '<!DOCTYPE en-note SYSTEM ' \
                '"http://xml.evernote.com/pub/enml2.dtd">'
note.content += '<en-note></en-note>'

created_note = note_store.createNote(note)

print("evrn: Successfully created a new note with GUID: ", created_note.guid)
print()