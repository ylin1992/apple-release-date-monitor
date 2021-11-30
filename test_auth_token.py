import json, requests
from requests.exceptions import RequestException, HTTPError, URLRequired

def main():

  # Configuration Values
  domain = 'dev-artpgixt.us.auth0.com'
  audience = f'https://{domain}/api/v2/'
  client_id = 'kcfySVTZ5c2KdAMtFYZFoEc8kUCUbNhJ'
  client_secret = '8JU7eZmuS4HQcoKbQWssX4qFe2XnTKmIZL74Rg_uo66kekMbSbJHPAgpp36flbOQ'
  grant_type = "client_credentials" # OAuth 2.0 flow to use

  # Get an Access Token from Auth0
  base_url = f"https://{domain}"
  payload =  { 
    'grant_type': grant_type,
    'client_id': client_id,
    'client_secret': client_secret,
    'audience': audience
  }
  response = requests.post(f'{base_url}/oauth/token', data=payload)
  oauth = response.json()
  print(oauth)
  access_token = oauth.get('access_token')

  # Add the token to the Authorization header of the request
  headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
  }

  # Get all Applications using the token
  try:
    res = requests.get(f'{base_url}/api/v2/clients', headers=headers)
    print(res.json())
  except HTTPError as e:
    print(f'HTTPError: {str(e.code)} {str(e.reason)}')
  except URLRequired as e:
    print(f'URLRequired: {str(e.reason)}')
  except RequestException as e:
    print(f'RequestException: {e}')
  except Exception as e:
    print(f'Generic Exception: {e}')

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
