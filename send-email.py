import boto3

import json

ses = boto3.client("ses")

def handler(event, context):

   print(event)

   tabledetails = event["Records"][0]["dynamodb"]

   print(tabledetails)

   name = tabledetails["NewImage"]["Name"]["S"];

   email = tabledetails["NewImage"]["Email"]["S"];

   url = tabledetails["NewImage"]["URL"]["S"];

   messagebody = """Hi %s!

Your shopping cart on Online-Business is waiting for you.

Follow this link to return to your cart:

%s""" % (name, url)

   try:

       data = ses.send_email(

           Source="janakaud@gmail.com",

           Destination={

               'ToAddresses': [email]

           },

           Message={

               'Subject': {

                   'Data': "Your cart is waiting!"

               },

               'Body': {

                   'Text': {

                       'Data': messagebody

                   }

               }

           }

       )

   except BaseException as e:

       #print(e)

       raise(e)

   return {"message": "Successfully executed"}