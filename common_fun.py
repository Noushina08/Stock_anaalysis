import nsepy
import boto3
import os
def get_historycal_data(sy,s,e):
    return nsepy.get_history(symbol=sy,start=s,end=e)

def upload_to_s3(file,path,bucket):
    session=boto3.Session(aws_access_key_id="ASIAU7RKNZHK4MM2KHTE",aws_secret_access_key="T4lOMCpPVGZu8O3zh4127ASEwhduZoVbsyhK0TpH",aws_session_token="FwoGZXIvYXdzELf//////////wEaDPjq4c08eh7fu52INiK5AeHYqRsxHsFSNeWED6RcG3C6ZVY1eko7/ZnS3/PInfjzFyG03Y4hRLmv5U6hAuCGE4GA2GyOwVamFPcij4rS+s3VOeB368FsDuoW63UIjFblgWK0CRos4VHsg7zJ0IC3dHmyt20PL+xQ5g5SjQMcavulPc60w1t9Zwh/L9c9aWbUglmVDFeyNqfQDKtguvkoT5A7C+RwkhWhrfi2BZi3OC60FOxl2RP76i9hUQSYjXxpu8j0zJCyJGANKJvi/p4GMi1+bzxspGZMDKoi3wvcers8w3n1xRBki2i4tMoRMK3VwcaWw949fy1meAcGMvU=")
    s3=session.resource('s3')
    s3.Bucket(bucket).upload_file(file,path)
    print("uploaded file" +file)
def remove_file(filename):
    os.remove(filename)
    print("remove file"+filename)

