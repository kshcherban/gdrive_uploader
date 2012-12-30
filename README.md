Google Drive Uploader
===========

Simple script to upload files on Google Drive.

# Description
Script uses predefined [Drive APIs Client ID and Client Secret](https://developers.google.com/drive/quickstart-python#step_1_enable_the_drive_api).  
It takes upload file as command line argument, uploads it and sets permissions that anyone who has download link can download the file.  
After file has been uploaded script prints download url.

# Requirements
  * Python >= 2.6
  * [google-api-python-client](http://code.google.com/p/google-api-python-client/)
  * python-httplib2

# Example
    insider@laptop:~/Documents/scripts$ echo 'this is test' > test.txt
    insider@laptop:~/Documents/scripts$ ./gdrive_upload.py test.txt 
    https://docs.google.com/a/pawned.ru/uc?id=0B3TLzHm0uDyjV3Rvc2o0eklYRG8&export=download
    insider@laptop:~/Documents/scripts$ wget -O test_downloaded.txt https://docs.google.com/a/pawned.ru/uc?id=0B3TLzHm0uDyjV3Rvc2o0eklYRG8&export=download
    [1] 5477
    insider@laptop:~/Documents/scripts$ --2012-12-30 18:41:10--  https://docs.google.com/a/pawned.ru/uc?id=0B3TLzHm0uDyjV3Rvc2o0eklYRG8
    Resolving docs.google.com (docs.google.com)... 202.69.181.216, 202.69.181.212, 202.69.181.241, ...
    Connecting to docs.google.com (docs.google.com)|202.69.181.216|:443... connected.
    HTTP request sent, awaiting response... 302 Moved Temporarily
    Location: https://doc-0k-8c-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/ebe7lq9nngg57osq2osphf1pu8dj719i/1356861600000/16139596377165396196/*/0B3TLzHm0uDyjV3Rvc2o0eklYRG8?h=12224797724442194278 [following]
    Warning: wildcards not supported in HTTP.
    --2012-12-30 18:41:13--  https://doc-0k-8c-docs.googleusercontent.com/docs/securesc/ha0ro937gcuc7l7deffksulhg5h7mbp1/ebe7lq9nngg57osq2osphf1pu8dj719i/1356861600000/16139596377165396196/*/0B3TLzHm0uDyjV3Rvc2o0eklYRG8?h=12224797724442194278
    Resolving doc-0k-8c-docs.googleusercontent.com (doc-0k-8c-docs.googleusercontent.com)... 74.125.128.132, 2404:6800:4005:c00::84
    Connecting to doc-0k-8c-docs.googleusercontent.com (doc-0k-8c-docs.googleusercontent.com)|74.125.128.132|:443... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 13 [text/plain]
    Saving to: `test_downloaded.txt'

    100%[===============================================================================================================================>] 13          --.-K/s   in 0s      

    2012-12-30 18:41:15 (3.16 MB/s) - `test_downloaded.txt' saved [13/13]


    [1]+  Done                    wget -O test_downloaded.txt https://docs.google.com/a/pawned.ru/uc?id=0B3TLzHm0uDyjV3Rvc2o0eklYRG8
    insider@laptop:~/Documents/scripts$ cat test_downloaded.txt 
    this is test
