from django.conf import settings
import requests, json


def getEventInfo():
    r = requests.get(settings.FACEBOOK_API_URL+settings.FACEBOOK_EVENT_ID, params={'access_token': settings.FACEBOOK_API_KEY})
    return json.loads(r.text)

def newPostsIDs():
    r = requests.get(settings.FACEBOOK_API_URL+settings.FACEBOOK_EVENT_ID+'/feed', params={'access_token': settings.FACEBOOK_API_KEY})
    posts = json.loads(r.text)
    while len(posts['data']) > 0:
        yield [d['id'] for d in posts['data']]
        r = requests.get(posts['paging']['next'])
        posts = json.loads(r.text)

def getHashtagsOfPost(postid):
    r = requests.get(settings.FACEBOOK_API_URL+postid)
    message = json.loads(r.text)['message']
    substrs = message.split(' ')
    hashtags = []
    for substr in substrs:
        if substr.startswith('#'):
            hashtags.append(substr)
    return hashtags
