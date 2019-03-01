import hashlib
import binascii
import sys
import os
#from progress.bar import Bar


hashTypes = ['SHA256','MD5', 'SHA1']

filePath = input("specify exact file path: \n\n")

fileType = input("specify checksum type: \n")

if(fileType not in hashTypes):
   print("Invalid file type \n\n")
fileSize = os.path.getsize(filePath)

print("file is: " + str(fileSize) + " bytes")


def SHA256(filePath):
   """"This function returns the SHA-1 hash
   of the file passed into it"""
   print("Processing SHA256...")

   # make a hash object
   h = hashlib.sha256()

   # open file for reading in binary mode
   with open(filePath,'rb') as file:
  
       # loop till the end of the file
      chunk = 0
      iteration = 0
      onePercent = fileSize / 100
      while chunk != b'':
           if iteration == onePercent:
              print(iteration)
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           #every 1024 bytes
           iteration += 1024     
           h.update(chunk)
           

   # return the hex representation of digest
   return h.hexdigest()


message = SHA256(filePath)

print("SHA256:\n" + message + "\n")

def MD5(filePath):
   print("processing MD5...")
   
   h = hashlib.md5()

   with open(filePath, 'rb') as file:
      
      chunk = 0
      
      while chunk != b'':
         
         chunk = file.read(1024)
         h.update(chunk)
         
      return h.hexdigest()
message = MD5(filePath)
print("MD5:\n" + message + "\n")

def SHA1(filePath):
   print("SHA1 processing")

   h = hashlib.sha1()

   with open(filePath, 'rb') as file:

      chunk = 0
      
      while chunk != b'':
         
         chunk = file.read(1024)
         h.update(chunk)
         
      return h.hexdigest()
message = SHA1(filePath)
print("SHA1:\n" + message + "\n")


#----------------------------------------------------------------------

#with open(filePath, 'rb') as afile:
#   buf = afile.read(BLOCKSIZE)
#   while len(buf) > 0:
#       hasher.update(buf)
#       buf = afile.read(BLOCKSIZE)
#       if(buf != BLOCKSIZE):
#           print(hasher.hexdigest)
# ---------------------------------------------------------------------
#string = binascii.hexlify(f)
#print(string)

#def sha256(f):
#   hash_sha256 = hashlib.sha256()
#   with open(f, "rb") as f:
#       for chunk in iter(lambda: f.read(4096), b""):
#           hash_sha256.update(chunk)
#   return hash_sha256.hexdigest()



