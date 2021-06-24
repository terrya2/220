from requests import request

base_url = "https://baier-api.herokuapp.com/220/"

def test(url, method, data={}, api_key='54bc1a55-6e05-44a8-80c0-9bd44b67ad8d', header={"content-type": "application/json"}, params={}):
    header.update({"x-api-key": api_key})
    return request(method=method, url=f'{base_url}{url}', headers=header, json=data, params=params)