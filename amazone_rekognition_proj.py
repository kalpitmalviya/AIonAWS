# open web cam  to click image
# real time image/video capture : cv2 library
import boto3
import cv2

# Internal-Webcam (0) :   External-Webcam  (1)
cap = cv2.VideoCapture(0)
myphoto = "kalpit.jpg"

# click image
ret, photo = cap.read()

# saving image in the current folder
cv2.imwrite(myphoto, photo)

# To disconnect webcam
cap.release()

# upload photo into aws cloud for storage :  S3
region = "ap-south-1"
bucket = "aiworkshopday1"
myphoto

# contacting to aws services using python lib
s3 = boto3.resource("s3")
upimage = "file.jpg"

# uploading image on s3 bucket
s3.Bucket(bucket).upload_file(myphoto, upimage)

# connect with rekognition service
rek = boto3.client('rekognition', region)

face_response = rek.detect_faces(

    Image={

        'S3Object': {
            'Bucket': bucket,
            'Name': upimage,

        }
    },
    Attributes=['ALL']
)
print(face_response['FaceDetails'][0])

# Detects instances of real-world entities within an image
# response = rek.detect_labels(

#     Image={

#         'S3Object': {
#             'Bucket': bucket,
#             'Name': upimage,

#         }
#     },
#     MaxLabels=13,
#     MinConfidence=90

# )


# for i in range(10):
#     print(response['Labels'][i]['Name'])
