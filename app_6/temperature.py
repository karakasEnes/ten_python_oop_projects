import requests
from bs4 import BeautifulSoup
class Temperature:
    headers = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    base_url = 'https://www.timeanddate.com/weather/'

    def __init__(self, country, city):
        self.city = city.replace(' ', '-')
        self.country = country.replace(' ', '-')

    def _build_url(self):
        url = self.base_url + self.country + '/' + self.city
        return url

    def _scrape(self):
        response = requests.get(self._build_url(), headers=self.headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract information from the HTML
            # For example, let's find all the links on the page

            temp = soup.select_one('#qlook div.h2')
            result = temp.text.replace(' °C', '').strip()
            return result
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

    def get(self):
        return float(self._scrape())


if __name__ == '__main__':
    temperature = Temperature(country='usa', city='san francisco').get()
    print(temperature)