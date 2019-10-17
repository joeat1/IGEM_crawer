import os
import time
import random
import string
import requests
import logging
from lxml import html, etree
from requests_toolbelt import MultipartEncoder

def select_by_css(htmltext, css_info):
    htmltree = html.fromstring(htmltext)
    res = htmltree.cssselect(css_info)
    return res

def loginpage(username, password, Timeout=60):
    loginurl = 'https://igem.org/Login2'
    header = {  "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            "Referer": "https://igem.org/Login2",
            }
    logindata = {
        'username': username,
        'password': password,
        'Login': 'Login'
    }
    session = requests.Session()
    try:
        session.get(loginurl, timeout=Timeout)
        resp = session.post(loginurl, data=logindata, headers=header ,timeout=Timeout , allow_redirects=True)
        # print(resp.text)
        # print('You have successfully logged into the iGEM web sites.')
        if 'successfully' in resp.text:
            print('You have successfully logged into the iGEM web sites.')
        # for i in range(len(resp.history)):
        #     print(resp.history[0].headers['Location'])
    except Exception as e:
        print('[-] Something wrong when login')
        print(e)
        pass
    return session

def editpage(session, pageurl, newcode, useoldcode=False, header={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}, Timeout=60):
    editurl = 'https://2019.igem.org/wiki/index.php?title='+ pageurl[22:] +'&action=edit'
    edithtml = session.get(editurl, headers=header, timeout=Timeout)
    edittree = html.fromstring(edithtml.text)
    inputitems = edittree.cssselect('input')
    fields = {}
    for item in inputitems:
        if item.value is not None and item.name not in ['wpPreview','wpDiff']:
            fields[item.name] = item.value
    # print(fields)
    submiturl = 'https://2019.igem.org/wiki/index.php?title='+ pageurl[22:] +'&action=submit'
    if useoldcode:
        try:
            htmlcontent = edittree.cssselect('.mw-ui-input')[0].text
        except:
            print('[-] htmlcontent is invalid')
            return False
    else:
        htmlcontent = newcode
    fields['wpTextbox1'] = htmlcontent
    mencode = MultipartEncoder(
            fields = fields,
            boundary = '------' + ''.join(random.sample(string.ascii_letters + string.digits, 32)) #WebKitFormBoundaryUMKxNGGyDUU4UqAQ
            )
    # print(fields)
    header['Referer'] = editurl
    header['Content-Type'] =  mencode.content_type #multipart/form-data; boundary=----WebKitFormBoundaryUMKxNGGyDUU4UqAQ
    submithtml = session.post(submiturl, data=mencode, headers=header ,timeout=Timeout, allow_redirects=True)
    if submithtml.url==pageurl:
        print('The page is edited: '+pageurl)
        return True
    else:
        print('The page is not edited: '+pageurl+submithtml.url)
        return False

def uploadpage(session, team_name, uploadpic_path, header={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}, Timeout=60):
    # The content_type dirction
    # Reference: https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Complete_list_of_MIME_types
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
    uploadpic_type = uploadpic_path.split('.')[-1]
    print(uploadpic_path, uploadpic_type)
    if uploadpic_type not in content_type_dir.keys():
        print('[-] The filetype is not supported', uploadpic_type)
        return
    uploadurl = 'https://2019.igem.org/Special:Upload'
    uploadhtml = session.get(uploadurl, timeout=Timeout)
    uploadtree = html.fromstring(uploadhtml.text)
    uploaditems = uploadtree.cssselect('input')
    uploadfields = {}
    for item in uploaditems:
        if item.value is not None:
            uploadfields[item.name] = item.value
    
    uploadpic_name = 'T--' +team_name+ '--' + uploadpic_path.split('\\')[-1]
    uploadfields['wpDestFile'] = uploadpic_name
    uploadfields['wpUploadFile'] = ('filename', open(uploadpic_path, 'rb'), content_type_dir[uploadpic_type]) #image/svg+xml  image/jpeg
    # print(uploadfields)
    upmencode = MultipartEncoder(
        fields = uploadfields,
        boundary = '------' + ''.join(random.sample(string.ascii_letters + string.digits, 32))
        )
    header['Referer'] = uploadurl
    header['Content-Type'] =  upmencode.content_type #multipart/form-data; boundary=----WebKitFormBoundaryUMKxNGGyDUU4UqAQ
    uploadedhtml = session.post(uploadurl, data=upmencode, headers=header, timeout=Timeout, allow_redirects=True)
    uploadedtree = html.fromstring(uploadedhtml.text)
    uploadedpicurl = uploadedtree.cssselect('.internal')
    if len(uploadedpicurl) > 0 :
        dest_url = 'https://2019.igem.org' + uploadedpicurl[0].get('href')
        if 'File' in dest_url:
            print('[*] The picture has been uploaded')
            print(uploadedhtml.url, uploadedtree.cssselect('.thumbinner')[0].attrib)
            return 
        print('[+] The uploading work has been done, the url of the pictureis [' +uploadpic_path+ '] :')
        print(dest_url)
        logging.info(uploadpic_path+' : '+dest_url)
        return dest_url
    else:
        print(uploadedhtml.text) #thumbinner
        print('[-] Something is wrong when uploading the picture'+uploadpic_path)
        return None

def flush_all(session, wikipages):
    for wikipage in wikipages:
        if wikipage != '#':
            editpage(session, wikipage, newcode=None, useoldcode=True)
            time.sleep(2)

def find_ext_file(path, ext, file_list=[]):
    #find the whole file by ext
    dir = os.listdir(path)
    for i in dir:
        i = os.path.join(path, i)
        if os.path.isdir(i):
            find_ext_file(i, ext, file_list)
        else:
            if os.path.splitext(i)[1] in ext:
                file_list.append(os.path.abspath(i))
    return file_list

header={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

igem_page_list = [
    'https://2019.igem.org/Team:{}'.format(Team_name), 
    'https://2019.igem.org/Team:{}/Team'.format(Team_name), 
    'https://2019.igem.org/Team:{}/Collaborations'.format(Team_name), 
    'https://2019.igem.org/Team:{}/Description'.format(Team_name), 
    'https://2019.igem.org/Team:{}/Description'.format(Team_name), 
    'https://2019.igem.org/Team:{}/Design'.format(Team_name), 
    'https://2019.igem.org/Team:{}/Experiments'.format(Team_name), 
    'https://2019.igem.org/Team:{}/Notebook'.format(Team_name), 
    'https://2019.igem.org/Team:{}/Contribution'.format(Team_name), 
    'https://2019.igem.org/Team:{}/Results'.format(Team_name), 
    'https://2019.igem.org/Team:{}/Demonstrate'.format(Team_name), 
    'https://2019.igem.org/Team:{}/Improve'.format(Team_name), 
    'https://2019.igem.org/Team:{}/Attributions'.format(Team_name), 
    'https://2019.igem.org/Team:{}/Parts'.format(Team_name), 
    'https://2019.igem.org/Team:{}/Parts_Overview'.format(Team_name), 
    'https://2019.igem.org/Team:{}/Basic_Parts'.format(Team_name), 
    'https://2019.igem.org/Team:{}/Composite_Parts'.format(Team_name), 
    'https://2019.igem.org/Team:{}/Part_Collection'.format(Team_name), 
    'https://2019.igem.org/Team:{}/Safety'.format(Team_name), 
    'https://2019.igem.org/Team:{}/Model'.format(Team_name), 
    'https://2019.igem.org/Team:{}/Human_Practices'.format(Team_name), 
    'https://2019.igem.org/Team:{}/Public_Engagement'.format(Team_name)
]

Timeout = 60
username = 'XXX'
password = 'XXX'
Team_name = 'XXXX'
session = requests.Session()
if not editpage(session, igem_page_list[0], newcode=None, useoldcode=True):
    session = loginpage(username, password)
# flush_all(session, igem_page_list) #Can refresh all pages

imgdir_path = './img' #The image path that needs to be uploaded, which can be relative position
# imgdir_path = '.'
filelist = find_ext_file(imgdir_path, ['.png','.jpg'], []) #Get a list of images
for imgfile in filelist:
    uploadpage(session, Team_name, imgfile) #Upload all the images in the selected directory and show the path
