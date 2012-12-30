Google Drive Uploader
===========

Simple script to upload files on Google Drive

# Description
Script uses predefined [Drive APIs Client ID and Client Secret](https://developers.google.com/drive/quickstart-python#step_1_enable_the_drive_api).  
It takes upload file as command line argument, uploads it and sets permissions  
that anyone who has download link can upload file.  
After file has been uploaded script prints download url.

# Requirements
  * Python >= 2.6
  * [google-api-python-client](http://code.google.com/p/google-api-python-client/)
