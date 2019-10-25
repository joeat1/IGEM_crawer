# IGEM_tools
> https://2019.igem.org/Resources/Wiki_Editing_Help
> https://igem.org/2019_Judging_Form?team=XXX
## word2html
+ pandoc  XXX.doc -o XXXX.html
+ https://wordhtml.com/
+ https://word2cleanhtml.com/
## crawer
Get some team name from the IGEM according to whether the abstracts of work contain the key words

## elements
Here are some common elements collected.

## igem_upload
> How to use: please set the following items(username; password; Team_name) in the python script at first.
> flush_all(session, igem_page_list) #Can refresh all pages
> uploadpage(session, Team_name, imgfile) #Upload all the images in the selected directory and show the path
I analyzed the communication process uploaded by igem.org's wiki. In the network message, I found several key URLs.
+ `https://igem.org/Login2`
    Landing sites are required before page modifications, file uploads, or access to information is required.During the login process, the service will perform three page jumps.
    The login function has been implemented in the function `loginpage` in the igem_upload.py, you should set your own username and password for it.

+ `https://2019.igem.org/wiki/index.php?title='+ pageurl +'&action=edit`
    To modify the content of the webpage, you need to log in first. Then you can set a new webpage code or refresh the original content.It should be noted that the web page is generated after compilation. Once the template is modified, it is generally necessary to resubmit all web pages that have called the template. MultipartEncoder is used in this part.
    The edit function has been implemented in the function `editpage` in the igem_upload.py.
    
+ `https://2019.igem.org/Special:Upload`
    Currently this script only supports the following types of files, If you need to add a new file type, you need to add a key value to this dictionary.：
    ```
        content_type_dir = {
        'png': 'image/png',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'bmp': 'image/bmp',
        'svg': 'image/svg+xml',
        'gif': 'image/gif',
        'zip':'application/zip',
        'mp3': 'audio/mpeg',
        'webm': 'video/webm'
    }
    ```
    The function has been implemented in the function `uploadpage` in the igem_upload.py.


