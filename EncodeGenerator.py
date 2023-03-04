import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://smartface-17341-default-rtdb.firebaseio.com/",
    'storageBucket': "smartface-17341.appspot.com"
})

# Importing images
folderPath = 'Images'
PathList = os.listdir(folderPath)
print(PathList)
imgList = []
personIds = []

for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    personIds.append(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

    # print(path)
    # print(os.path.splitext(path)[0])
print(personIds)

def findEncodings(imagesList):
    pass
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

print("Encoding Started...")
encodeListknown = findEncodings(imgList)
encodeListknownWithIds = [encodeListknown, personIds]
# print(encodeListknown)
print("Encoding Complete")

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListknownWithIds, file)
file.close()
print("File Saved")
