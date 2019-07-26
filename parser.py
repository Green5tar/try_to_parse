import urllib.request
from bs4 import BeautifulSoup
import csv

burl="https://www.bbc.com/news/science_and_environment"

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', class_='gs-c-promo-body gs-u-mt@xxs gs-u-mt@m gs-c-promo-body--primary gs-u-mt@xs gs-u-mt@s gs-u-mt@m gs-u-mt@xl gel-1/3@m gel-1/2@xl gel-1/1@xxl')

    projects = []

    for mainn in div.find_all('div'):
        other = div.find('a')

    projects.append({
        'Head':other.h3.text
    })

    for project in projects:
        print(project)

    return projects

def save(projects, path):

    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(('Name - ',))

        writer.writerows(
            (project['Head'],) for project in projects
        )


def main():
    projects = []

    projects.extend(parse(get_html(burl)))

    save(projects, 'pars.csv')

if __name__ == '__main__':
    main()


