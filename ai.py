#!/bin/python3
print("content:text/html")
#print("Access-Control-Allow-Origin: *")
print()
import os
import subprocess
import cgi
from flask import Flask, request
import boto3
import base64
import random

data_taker=cgi.FieldStorage()
#print("hello")
image=data_taker.getvalue("image")
#print(type(image))
#print(image)
#img = base64.b64decode(image)
#print(img)
filename="./something.jpg"
with open(filename, 'wb') as f:
    #print("aaya")
    f.write(image)
    #print("wowwwwww..image saved in server")
mypotho='something.jpg'
bucket_name="clientimages123"
region="ap-south-1"
rek = boto3.client(
    'rekognition',
    aws_access_key_id="<your_id>",
    aws_secret_access_key="<your_secret_key>",
    region_name="ap-south-1"
    
)
#print(rek)
s3=boto3.resource('s3',aws_access_key_id="<your_id>",
    aws_secret_access_key="<your_secret_key>",
)
try:
    x=s3.Object(bucket_name,"image.jpg").upload_file(Filename='./something.jpg')
    #print("success!!  ", x)
    #rek=boto3.client('rekognition')
    responce=rek.detect_faces(Image={

        'S3Object': {
        'Bucket': bucket_name,
        'Name': 'image.jpg',

                }
            },
            Attributes=['ALL']
        )

    #print(responce)
    emotions=responce['FaceDetails'][0]['Emotions']
    #print(emotions)
    i=0
    emotion=""
    x=[]
    try:
        while i<8:
            x.append(responce['FaceDetails'][0]['Emotions'][i]['Confidence'])
            i=i+1
            x.sort()
            #print(x)
        i=0
        while i<8:
            if responce['FaceDetails'][0]['Emotions'][i]['Confidence']==x[-1]:
                #print(responce['FaceDetails'][0]['Emotions'][i]['Type'])
                emotion=responce['FaceDetails'][0]['Emotions'][i]['Type']
                emotion=emotion.lower()
                break
            i=i+1

        #return '{}'.format(emotion)
        print("\n\n\n")
        if(emotion=="happy"):
            print ('''<html>
            <head><title>Happy</title></head>
            <body style="background-color:black"/>
            <center><img src='https://clientimages123.s3.ap-south-1.amazonaws.com/brooke-cagle-oTweoxMKdkA-unsplash.jpg' alt="Aunty" width="200" height="200"></center>
            <audio  autoplay>
            <source src="https://clientimages123.s3.ap-south-1.amazonaws.com/Dura+-+Daddy+Yankee-+%5BPagalWorld.NL%5D.mp3" type="audio/mpeg">
            </audio>
            <a href="https://www.metahiber.com/">Learn and Grow More </a>
            <center><h2 style="color:white;"> You Seems to be Happy..Let's Party ;)</h2></center>
            </body>
            </html>''')
        
        elif(emotion=="angry"):
            print ('''<html>
            <head><title>Angry</title></head>
             <body style="background-color:black"/>
            <center><img src='https://clientimages123.s3.ap-south-1.amazonaws.com/nsey-benajah-5_gku5Usbzk-unsplash.jpg' alt="Aunty" width="200" height="200"></center>
            <audio  autoplay>
            <source src="https://clientimages123.s3.ap-south-1.amazonaws.com/gulaal-Aarambh+hai+Prachand.mp3" type="audio/mpeg">
            </audio>
            <a href="https://www.metahiber.com/">Learn and Grow More </a>
            <center><h2 style="color:white;"> You Seems to be Angry :|</h2></center>
            </body>
            </html>''')

        elif(emotion=="sad"):
            print ('''<html>
            <head><title>Sad</title></head>
            <body style="background-color:black;"/body>
%;">
            <center><img src='https://clientimages123.s3.ap-south-1.amazonaws.com/kat-j-NPmR0RblyhQ-unsplash.jpg' alt="Aunty" width="200" height="200"></center>
            <audio  autoplay>
            <source src="https://clientimages123.s3.ap-south-1.amazonaws.com/Jhand+Ba+-+Goodluck+Jerry+320+Kbps.mp3" type="audio/mpeg">
            </audio>
            <a href="https://www.metahiber.com/">Learn and Grow More </a>
            <center><h2 style="color:white;"> You Seems to be Sad :( </h2></center>
            </body>
            </html>''')

        else:
            print ('''<html>
            <head><title>Calm</title></head>
            <body style="background-color:black"/>
            <center><img src='https://clientimages123.s3.ap-south-1.amazonaws.com/dulana-kodithuwakku-05itvO-eMvg-unsplash.jpg' alt="Aunty" width="200" height="200"></center>
            <audio  autoplay>
            <source src="https://clientimages123.s3.ap-south-1.amazonaws.com/Tere+Hawaale(PagalWorld.com.se).mp3" type="audio/mpeg">
            </audio>
            <a href="https://www.metahiber.com/">Learn and Grow More </a>
            <center><h2 style="color:white;"> You Seems to be Calm :)</h2></center>
            </body>
            </html>''')
        #print("\n  umm your emotion is -> ", emotion)
    except Exception as e:
        #print("1st")
        #return 'try_again'
        print("try_again")
        print(e)


except Exception as e:
    print("shittttt")
    print(e)
