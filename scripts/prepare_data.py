# Setting up Imports
import requests
import hashlib
import zipfile


# Setting the URLs
url_wine_zip = 'https://archive.ics.uci.edu/static/public/109/wine.zip'

# Manual calculated the SHA-256
hash_zip = '2bae62c4481220623579d4c4fb36b55652b6b75e06e49fa1981b8198362dfdab'
# Using Requests to Download the Files

# Creating function which downloads the file and checks file integrity
def prepare_data(url_var,hash_compare,filename):
    print('Initializing')
    response = requests.get(url_var)
    with open(filename, mode='wb') as f:
        f.write(response.content)
    print('URL: '+url_var+'\nFile downloaded')
    with open(filename, 'rb')as f:
        data = f.read()
        sha256hash = hashlib.sha256(data).hexdigest()
    if hash_compare != sha256hash:
        print('Computed hash does not match expected hash')
    else:
        print('Computed hash matches expected hash')

# feedback: check if the "data" and the "data/folktables" folders are in the current directory. if not, create them
import os
path = "data/"
# Check whether the specified path exists or not
isExist = os.path.exists(path)
if not isExist:
# Create a new directory because it does not exist
    os.makedirs(path)

# feedback: from the instruction, the downloaded data should be store in the "data" folder (-1). 
# feedback: The adult.zip should be at data/, and the adult_reconstruction.csv should be at data/folktables/ 

# verify the integrity of the files based on stored pre-computed hashes of each file
prepare_data(url_wine_zip,hash_zip,os.path.join(path,'wine.zip'))

#extract all of the data from the zip file.
with zipfile.ZipFile(os.path.join(path,'wine.zip')) as z:
    z.extractall(os.path.join(path,'wine/'))

