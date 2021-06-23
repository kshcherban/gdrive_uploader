Google Drive Uploader
===========

Simple script to upload files on Google Drive.

# Description
Script uses predefined [Drive APIs Client ID and Client Secret](https://developers.google.com/drive/v2/web/quickstart/python#step_1_turn_on_the_api_name)

It takes upload file as command line argument, uploads it and sets permissions that anyone who has download link can download the file.  
After file has been uploaded script prints download url.

# Requirements
  * Python >= 3.6
  * [google-api-python-client](http://code.google.com/p/google-api-python-client/)
  * google-auth-oauthlib
  * google-auth-httplib2

```bash
pip install -r requirements.txt
```

# Configuration
 - use the [wizard](https://console.cloud.google.com/flows/enableapi?apiid=drive&angularJsUrl=%2Fflows%2Fenableapi%3Fapiid%3Ddrive&project=&folder=&organizationId=) to enable drive API.
 - [create OAuth client ID credentials](https://console.cloud.google.com/apis/credentials), choose **Desktop app** application type
 - save generated credentials as `credentials.json` in the script directory

# Usage

```bash
echo 'this is test' > test.txt
python gdrive_upload.py test.txt
https://docs.google.com/a/pawned.ru/uc?id=0B3TLzHm0uDyjV3Rvc2o0eklYRG8&export=download
wget -q -O - "https://docs.google.com/a/pawned.ru/uc?id=0B3TLzHm0uDyjV3Rvc2o0eklYRG8&export=download"
this is test
```
