import urllib.request, urllib.parse, urllib.error
import keys
import urllib.request, urllib.parse, urllib.error
import twurl

import ssl



def augment(url, parameters):
    secrets = keys.secretkeys()
    consumer = OAuthConsumer(secrets['consumer_key'],
                                   secrets['consumer_secret'])
    token = OAuthToken(secrets['token_key'], secrets['token_secret'])

    oauth_request = OAuthRequest.from_consumer_and_token(consumer,
                    token=token, http_method='GET', http_url=url,
                    parameters=parameters)
    oauth_request.sign_request(OAuthSignatureMethod_HMAC_SHA1(),
                               consumer, token)
    return oauth_request.to_url()


def test_me():
    print('* Calling Twitter...')
    url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
                  {'screen_name': 'ranadheer314', 'count': '2'})
    print(url)
    connection = urllib.request.urlopen(url)
    data = connection.read()
    print(data)
    headers = dict(connection.getheaders())
    print(headers)


print('* Calling Twitter...')
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
              {'screen_name': 'ranadheer314', 'count': '2'})
print(url)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

connection = urllib.request.urlopen(url, context=ctx)
data = connection.read()
print(data)

print ('======================================')
headers = dict(connection.getheaders())
print(headers)

