from django.http import HttpResponse
from django.conf import settings as setting
import requests, json
from rest_framework.views import APIView
from sales import settings
from rest_framework.response import Response
from .models import *
from .serializers import *


# from .models import OauthToken

#To fetch and store data from Salesforce API
class SalesForceAuth(APIView):

    def get(self,request):
        auth_url = 'https://login.salesforce.com/services/oauth2/token'

        # we send a post request to salesforce with needed creds
        response = requests.post(auth_url, data = {
                            'client_id':settings.Consumer_Key,
                            'client_secret':settings.Consumer_Secret,
                            'grant_type':'password',
                            'username':settings.SF_Username,
                            'password':settings.SF_Password,
                            })

        # get response in json format
        json_res = response.json()
        # print(json_res)

        #fetch access token from response
        access_token = json_res['access_token']
        auth = {'Authorization':'Bearer ' + access_token}

        # Extracting just in case it is not same
        instance_url = json_res['instance_url']

        # get the needed information
        url = instance_url + '/services/data/v45.0/query?q=SELECT+name,+description,+Industry,+phone+from+Account'
        url1 = instance_url + '/services/data/v45.0/query?q=SELECT+FirstName,+fax,+email,+MobilePhone,+LastName+from+Contact'
        url2 = instance_url + '/services/data/v45.0/query?q=SELECT+Name,+Country,+email,+Phone,+Username+from+User'
        

        # url = instance_url + '/services/data/v45.0/sobjects/Account/describe'
        #Accounts
        account1 = requests.get(url, headers=auth)
        
        acc = account1.json()
        list1=acc['records']
        for obj in list1:
            flag,created= Account.objects.get_or_create(name=obj['Name'],description=obj['Description'],industry=obj['Industry'],phone=(obj['Phone']))
            flag.save()

        #Contacts
        contact1=requests.get(url1, headers=auth)

        con=contact1.json()
        list2=con['records']
        for obj in list2:
            flag,created= Contact.objects.get_or_create(first_name=obj['FirstName'],last_name=obj['LastName'],fax=obj['Fax'],phone=(obj['MobilePhone']),email=obj['Email'])
            flag.save()
            pass

        #Users
        user1=requests.get(url2, headers=auth)

        userobj=user1.json()
        list3=userobj['records']
        for obj in list3:
            flag,created= User.objects.get_or_create(name=obj['Name'],country=obj['Country'],username=obj['Username'],phone=(obj['Phone']),email=obj['Email'])
            flag.save()
            pass

        # print(userobj)
        return Response({"Message":"Data collected and stored"})

class GetData(APIView):
    def get(self, request):
        account1=Account.objects.all()
        # print(account1)
        accountdata=AccountSerializer(account1,many=True).data

        contact1=Contact.objects.all()
        contactdata=ContactSerializer(contact1,many=True).data

        user1=User.objects.all()
        userdata=UserSerializer(user1,many=True).data

        serializer_data={"Account" : accountdata, "Contact" :contactdata, "User" : userdata}
        return Response(serializer_data)