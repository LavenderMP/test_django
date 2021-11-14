import requests


def check_status(request):
    if request.status_code == 200:
        return request.status_code, request.json()
    else:
        return request.status_code, None


def post_url(url, **kwargs):
    body_data = kwargs
    headers = {
        'Content-type': 'application/json',
        'Accept': 'application/json'
    }
    r = requests.post(
        url=url,
        json=body_data,
        headers=headers
    )
    return check_status(r)


def get_id(url, user_id):
    r = requests.get(url=url, params={'idUser': user_id})
    return check_status(r)
