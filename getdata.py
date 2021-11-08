import requests
from geturl import get_url

def get_data():
    data_url = get_url()
    data = requests.get(data_url)
    data_html = data.text

    return data_html

if __name__ == '__main__':
    get_data()