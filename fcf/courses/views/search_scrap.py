import requests
from bs4 import BeautifulSoup
import random

def get_udacity_course_details(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    # Make a GET request to the course URL with custom headers
    response = requests.get(url, headers=headers)

    # Parse the HTML content of the response
    soup = BeautifulSoup(response.content, "html.parser")

    platform = 'Udacity'

    # Find the course title element in the HTML
    title = soup.find("h1", class_="course-hero_courseTitle__xKGzg")
    if title:
        title = title.text.strip()

    #title = title.h1.text.strip()

    # Find the course description element in the HTML
    description = soup.find("div", class_="course-overview_courseSummary__JvVdf")
    if description:
        description =description.text.strip()

    # Find the course provider element in the HTML
    provider = soup.find("a", class_="course-org-link d-inline-block mr-4")
    #provider = provider.img.get("alt")

    # Find the course length element in the HTML
    data = soup.find("div", class_="course-overview_detailsStats__a_46m")
    counter = 0
    value = None
    length = None
    if data:
        for leng in data:
            if counter==0:
                value = leng.text.strip()
                counter+=1
            elif counter==1:
                length = leng.text.strip()
                counter += 1
            else:
                break

    # Find the course value element in the HTML
    #value = soup.find("button", class_="button--primary")

    # Extract the course value text
    #value = value.text if value else None

    # Return a dictionary of the course details
    return {
        "url": url,
        "title": title,
        "description": description,
        "provider": provider,
        "length": length,
        "value": value,
        "Platform": platform
    }

# Function to get the course details from Udemy
def get_swayam_course_details(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    # Make a GET request to the course URL with custom headers
    response = requests.get(url, headers=headers)

    # Parse the HTML content of the response
    soup = BeautifulSoup(response.content, "html.parser")

    platform = 'Swayam'

    # Find the course title element in the HTML
    title = soup.find("h1", class_="courseTitle")
    if title:
        title = title.text.strip()

    # Find the course description element in the HTML
    description = soup.find("div", class_="marginTop25 previewContent")
    if description:
        description = description.text.strip()

    # Find the course provider element in the HTML
    provider = 'NPTEL'

    length = None

    # Find the course value element in the HTML
    value = 'free'

    # Return a dictionary of the course details
    return {
        "url": url,
        "title": title,
        "description": description,
        "provider": provider,
        "length": length,
        "value": value,
        "Platform": platform
    }

# Function to get the course details from Udemy
def get_edx_course_details(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    # Make a GET request to the course URL with custom headers
    response = requests.get(url, headers=headers)

    # Parse the HTML content of the response
    soup = BeautifulSoup(response.content, "html.parser")

    platform = 'Edx'

    # Find the course title element in the HTML
    title = soup.find("div", class_="col-md-7")
    if title:
        title = title.h1.text.strip()

    # Find the course description element in the HTML
    description = soup.find("div", class_="mt-2 lead-sm html-data")
    if description:
        description = description.text.strip()

    # Find the course provider element in the HTML
    provider = soup.find("a", class_="course-org-link d-inline-block mr-4")
    if provider:
        provider = provider.img.get("alt")
        if 'Logo' in provider:
            provider = provider.replace('Logo', '')

    # Find the course length element in the HTML
    length = soup.find("div", class_="ml-3")
    if length:
        length = length.text.strip()

    # Find the course value element in the HTML
    value = soup.find("div", class_="d-flex align-items-start col-12 pt-4 pt-md-0 col-md-4")

    # Extract the course value text
    value = value.text if value else None

    # Return a dictionary of the course details
    return {
        "url": url,
        "title": title,
        "description": description,
        "provider": provider,
        "length": length,
        "value": value,
        "Platform": platform
    }

# Function to get the course details from coursera
def get_coursera_course_details(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    # Make a GET request to the course URL with custom headers
    response = requests.get(url, headers=headers)

    # Parse the HTML content of the response
    soup = BeautifulSoup(response.content, "html.parser")

    platform = 'Coursera'

    # Find the course title element in the HTML
    title = soup.find("h1", class_="banner-title banner-title-without--subtitle m-b-0")
    if not title:
        title = soup.find("h1", class_="banner-title m-b-0")
    if title:
        title = title.text.strip()

    # Find the course description element in the HTML
    description = soup.find("div", class_="description")
    if not description:
        description = soup.find("div", class_="content-inner")
    if description:
        description = description.text.strip()

    # Find the course provider element in the HTML
    provider = soup.find("img", class_="_1g3eaodg")
    if provider:
        provider = provider.get("alt")

    # Find the course length element in the HTML
    data = soup.find("div", class_="ProductGlance _9cam1z p-t-2")
    length = None

    # Find the course value element in the HTML
    value = soup.find("div", class_="EnrollButton")

    # Extract the course value text
    value = value.text if value else None

    # Return a dictionary of the course details
    return {
        "url": url,
        "title": title,
        "description": description,
        "provider": provider,
        "length": length,
        "value": value,
        "Platform": platform
    }


def search_google(query):

    img = ''
    if 'physics' in query.lower():
        img = random.choice(physics)
    elif 'machine learning' in query.lower():
        img = random.choice(machine_learning)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    # Format the Google search URL with the query
    if 'course' not in query:
        query = query + 'cours'
    search_url = "https://www.google.com/search?q={}".format(query.replace(" ", "+"))

    # Make a GET request to the Google search URL with custom headers
    response = requests.get(search_url, headers=headers)

    # Parse the HTML content of the response
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the search result elements in the HTML
    results = soup.find_all("div", class_="yuRUbf")

    # Extract the URLs from the search results
    urls = [result.find("a")["href"] for result in results[:10]]

    course_details = {'d1': {'url': [], 'Title': [], 'Description': [], 'Provider': [], 'Length': [], 'Value': [], 'Platform': []},
                      'd2': {'url': [], 'Title': [], 'Description': [], 'Provider': [], 'Length': [], 'Value': [], 'Platform': []},
                      'd3': {'url': [], 'Title': [], 'Description': [], 'Provider': [], 'Length': [], 'Value': [], 'Platform': []},
                      'd4': {'url': [], 'Title': [], 'Description': [], 'Provider': [], 'Length': [], 'Value': [], 'Platform': []}}

    counter = 0

    for url in urls:
       if 'coursera' in url:
           details = get_coursera_course_details(url)
           if details['value'] and details['url']:
                if 'Free' in details["value"]:
                    course_details['d1']["url"].append(details['url'])
                    course_details['d1']["Title"].append(details['title'])
                    course_details['d1']["Description"].append(details['description'])
                    course_details['d1']["Provider"].append(details['provider'])
                    course_details['d1']["Length"].append(details['length'])
                    course_details['d1']["Value"].append(details['value'])
                    course_details['d1']["Platform"].append(details['Platform'])
                    counter+=1

       elif 'edx' in url:
           details = get_edx_course_details(url)
           if details['value'] and details['url']:
                if 'Free' in details["value"]:
                    course_details['d2']["url"].append(details['url'])
                    course_details['d2']["Title"].append(details['title'])
                    course_details['d2']["Description"].append(details['description'])
                    course_details['d2']["Provider"].append(details['provider'])
                    course_details['d2']["Length"].append(details['length'])
                    course_details['d2']["Value"].append(details['value'])
                    course_details['d2']["Platform"].append(details['Platform'])
                    counter+=1

       elif 'nptel' in url:
           details = get_swayam_course_details(url)
           if details['value'] and details['url']:
                if 'Free' in details["value"]:
                    course_details['d3']["url"].append(details['url'])
                    course_details['d3']["Title"].append(details['title'])
                    course_details['d3']["Description"].append(details['description'])
                    course_details['d3']["Provider"].append(details['provider'])
                    course_details['d3']["Length"].append(details['length'])
                    course_details['d3']["Value"].append(details['value'])
                    course_details['d3']["Platform"].append(details['Platform'])
                    counter+=1
       elif 'udacity' in url:
           details = get_udacity_course_details(url)
           if details['value'] and details['url']:
                if 'Free' in details["value"]:
                    course_details['d4']["url"].append(details['url'])
                    course_details['d4']["Title"].append(details['title'])
                    course_details['d4']["Description"].append(details['description'])
                    course_details['d4']["Provider"].append(details['provider'])
                    course_details['d4']["Length"].append(details['length'])
                    course_details['d4']["Value"].append(details['value'])
                    course_details['d4']["Platform"].append(details['Platform'])
                    counter+=1

    return course_details,counter,img



physics = ['https://i.postimg.cc/Xqm4v0S9/dna-cover1.jpg',
               'https://i.postimg.cc/CKmLQBMH/57d679e4-a080-4fc3-8b2f-38deb8a50aca-8b7d9400f8bf-small.jpg',
               'https://i.postimg.cc/X7ZDn45R/image.jpg',
               'https://i.postimg.cc/MZhK6Z4R/image.jpg']
machine_learning = ['https://i.postimg.cc/pT0PgFsG/image.jpg',
                        'https://i.postimg.cc/BQpfMT1F/AI-and-ML-in-Trading.jpg',
                        'https://i.postimg.cc/CLJbchTc/4c70ad9b-9602-49af-bf00-83fa4bf47708-dc4566d15250-small.jpg',
                        'https://i.postimg.cc/fyfZN71m/ml-e1610553826718-768x470.jpg',
                        'https://i.postimg.cc/GpxqWGnw/computer-vision-bg-eeaf360f05584fbcf2e7ade39dfa08ae1ecbdff9a1706132b38198c246230cf2.jpg']

# Example usage
#query = "Intro to Machine Learning course"
#d1,d2,d3,d4 = search_google(query)
#print(d1)
