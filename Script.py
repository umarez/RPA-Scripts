import requests
import json
import random

BASE_URL = 'https://uibank-api.azurewebsites.net/api'

def login():
    body = {
        'username': 'umarez',
        'password': 'umar4321'
    }

    res = requests.post(f'{BASE_URL}/users/login', json=body)
    return res.text

def getUserProfile(token: str):
    api_url = f'{BASE_URL}/accounts?filter[where][userId]={token}'

    headers:dict = {
        'Authorization': f'{token}'
    }

    res = requests.get(api_url, headers=headers)
    res = res.json()[0]

    return json.dumps(res, indent=4)


def getAllAccountSummary(token: str, userId: str):
    api_url = f'{BASE_URL}/accounts?filter[where][userId]={userId}'

    headers:dict = {
        'Authorization': f'{token}'
    }

    res = requests.get(api_url, headers=headers)
    res = res.json()

    return json.dumps(res, indent=4)

def getAccountTransaction(token: str, userId: str):
    api_url = f"{BASE_URL}/transactions?filter[where][accountId]={userId}"

    headers:dict = {
        'Authorization': f'{token}'
    }

    res = requests.get(api_url, headers=headers)

    return json.dumps(res.json(), indent=4)

def createNewAccount(token: str, name: str, type: str, account_number: int = random.randint(10000000, 99999999), initial_balance: str = 100):
    api_url = f"{BASE_URL}/accounts"

    headers:dict = {
        'Authorization': f'{token}'
    }

    body = {
        "friendlyName": name,
        "type": type,
        "accountNumber": int(account_number),
        "balance": int(initial_balance)
    }

    requests.post(api_url, headers=headers, json=body)

    return "Account Created Successfully"

def createTransferAccount(token: str, account_id: str, transfer_to_account_id: str, amount: int, description: str = "Transfer"):
    api_url = f"{BASE_URL}/transactions"

    headers:dict = {
        'Authorization': f'{token}'
    }

    body = {
        "TransfertoAccountId":  transfer_to_account_id,
        "accountId": account_id,
        "amount": amount,
        "description": description,
        "type": "transfer"
    }

    requests.post(api_url, headers=headers, json=body)

    return f"Transfered {amount} from {account_id} to {transfer_to_account_id} Successfully"


def applyForLoan(token: str, email: str, age: int, income: str, term: int, amount: int):
    api_url = f"{BASE_URL}/quotes/newquote"

    headers:dict = {
        'Authorization': f'{token}'
    }

    body = {
        "age": int(age),
        "amount": int(amount),
        "email": email,
        "income": int(income),
        "term": int(term)
    }

    res = requests.post(api_url, headers=headers, json=body)

    return  json.dumps(res.json(), indent=4)









