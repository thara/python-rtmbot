from slackclient import SlackClient
import json

# instance of API client that can be accessed from other files
api_client = None


# create an instance of the api client and initialize it with a token
def init(token):
    global api_client
    api_client = SlackClient(token)
    return api_client

def get_presence(id):
    return api_client.api_call('users.getPresence', user=id)

def get_info(id):
    return api_client.api_call('users.info', user=id)

def get_users():
    return api_client.api_call('users.list')['members']

