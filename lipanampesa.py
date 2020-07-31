import requests

from . import keys
from . access_token import generate_access_token
from . encode import generate_password
from .utils import get_time_stamp


def lipa_na_mpesa():
    formatted_time = get_time_stamp()
    decoded_password = generate_password(formatted_time)
    access_token = generate_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}

    request = {
        "BusinessShortCode": keys.business_short_code,
        "Password": decoded_password,
        "Timestamp": "20200730111723",
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": keys.phone_number,
        "PartyB": "",
        "PhoneNumber": keys.phone_number,
        "CallBackURL": "https://fullstackdjango.com/lipanampesa/",
        "AccountReference": "112344456 ",
        "TransactionDesc": " liquor store "
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)


lipa_na_mpesa()
