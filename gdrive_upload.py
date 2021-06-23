#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: k.scherban@gmail.com
# license: GPL v.2 or higher

import os
import sys
import logging
from mimetypes import guess_type

from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from apiclient.errors import ResumableUploadError

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


# Log only oauth2client errors
logging.basicConfig(level="ERROR")

# Path to token and credentials json files, should be in same directory as script
token_file = sys.path[0] + "/token.json"
credentials_file = sys.path[0] + "/credentials.json"

# Check https://developers.google.com/drive/scopes for all available scopes
OAUTH_SCOPES = [
    "https://www.googleapis.com/auth/drive.file",
]


# Get mime type and name of given file
def file_ops(file_path):
    mime_type = guess_type(file_path)[0]
    mime_type = mime_type if mime_type else "text/plain"
    file_name = file_path.split("/")[-1]
    return file_name, mime_type


def authorize(token_file):
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, OAUTH_SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_file, OAUTH_SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_file, "w") as token:
            token.write(creds.to_json())
    return creds


def upload_file(file_path, file_name, mime_type, creds):
    # Create Google Drive service instance
    drive_service = build("drive", "v2", credentials=creds)
    # File body description
    media_body = MediaFileUpload(file_path, mimetype=mime_type, resumable=True)
    body = {
        "title": file_name,
        "description": "backup",
        "mimeType": mime_type,
    }
    # Permissions body description: anyone who has link can upload
    # Other permissions can be found at https://developers.google.com/drive/v2/reference/permissions
    permissions = {"role": "reader", "type": "anyone", "value": None, "withLink": True}
    # Insert a file
    file = drive_service.files().insert(body=body, media_body=media_body).execute()
    # Insert new permissions
    drive_service.permissions().insert(fileId=file["id"], body=permissions).execute()
    # Define file instance and get url for download
    file = drive_service.files().get(fileId=file["id"]).execute()
    download_url = file.get("webContentLink")
    return download_url


if __name__ == "__main__":
    # Check if file provied as argument and exists
    if len(sys.argv) != 2:
        print("One file should be provided as argument")
        sys.exit(1)
    else:
        # Path to the file to upload
        file_path = sys.argv[1]
    try:
        with open(file_path) as f:
            pass
    except IOError as e:
        print(e)
        sys.exit(1)
    # Authorize, get file parameters, upload file and print out result URL for download
    creds = authorize(token_file)
    file_name, mime_type = file_ops(file_path)
    # Sometimes API fails to retrieve starting URI, we wrap it.
    try:
        print(upload_file(file_path, file_name, mime_type, creds))
    except ResumableUploadError as e:
        print("Error occured while first upload try:", e)
        print("Trying one more time.")
        print(upload_file(file_path, file_name, mime_type))
