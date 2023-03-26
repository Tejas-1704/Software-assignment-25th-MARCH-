# Define an API to access public art displays
def get_art_displays():
    url = 'https://example.com/public_art_displays'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    art_displays = soup.find_all('div', class_='art_display')
    return art_displays
