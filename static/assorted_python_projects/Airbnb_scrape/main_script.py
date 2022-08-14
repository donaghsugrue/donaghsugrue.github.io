########## TO DO ##########

# Install Beautiful Soup - Allows easy extraction of data from HTML
# Install Selenium - A multi purpose tool for automating web browser actions
# What's WSL?
# Just pulling from Airbnb isn't enough - we need to pull from booking.com etc too
# How to organise the data effectively so that it's uniform across platforms
# If function - if longitude / latitude data is within rent pressure zone - save it
# If no "next page", then save file and end

########################### 

### Mostly taken from here https://smithio.medium.com/scraping-airbnb-website-with-python-beautiful-soup-and-selenium-8ec86e327b6c


# NOTES
# https://tripeanddrisheen.substack.com/p/airbnb-in-cork-how-big-a-role-is?s=r&utm_campaign=post&utm_medium=web&utm_source=direct

# https://www.citizensinformation.ie/en/housing/owning_a_home/home_owners/renting_your_property_for_shortterm_lets.html

# https://mobile.twitter.com/ShamingDeValera/status/1519603210130006016?cxt=HHwWgIC9tbDE25YqAAAA



# ______________________________________________________________________________________________________________________________________________________________________________________
# GET URL
#

services = {        # URL                                               # Chunk for next page       # ID's and tags to cycle through
    "Airbnb"    :   ["https://www.airbnb.ie/s/Cork--Ireland/homes",     "&items_offset=20",         {"class": "c4mnd7m dir dir-ltr"}],
    "Booking"   :   ["booking.com",                                     "",                         {}],
    "Trivago?"  :   ["",                                                "",                         {}]
    ### Add any and all other services in here, and we'll just cycle through all of them.
}

def master_func() :
    for i in services:
        page_url = services[i][0]
        scrape_page(page_url)
    return



# ______________________________________________________________________________________________________________________________________________________________________________________
# SCAN LISTINGS
#

def scrape_page(page_url):
    """
    Extracts HTML from a webpage
    """

    answer = requests.get(page_url)
    content = answer.content
    soup = BeautifulSoup(content, features = "html.parser")

    text = soup.find("div", {"class": "foober"}).get_text()


    return soup



# ______________________________________________________________________________________________________________________________________________________________________________________
# Click on each and extract data

def extract_listing(page_url):
    """
    Extract listings from an Airbnb search page
    """

    page_soup = scrape_page(page_url)
    listings = page_soup.findAll("div", div_spec)

    return listings



# ______________________________________________________________________________________________________________________________________________________________________________________
# create all of the urls for the different pages of results to search through

def build_urls(url: str, listings_per_page: int = 20, pages_per_location: int = 15):
    """
    Builds links for all search pages for a given location
    
    """
    url_list = []

    for i in range (pages_per_location):
        offset = listings_per_page * i
        url_pagination = url + "&items_offset=20"
        url_list.append(url_pagination)

    return url_list

### FOR AIRBNB ###
# From  ->      https://www.airbnb.ie/s/Cork--Ireland/homes
# To    ->      https://www.airbnb.ie/s/Cork--Ireland/homes?tab_id=home_tab&items_offset=20

### FOR BOOKING ###
# From  ->      https://_________
# To    ->      https://_________





# ______________________________________________________________________________________________________________________________________________________________________________________
#

def extract_soup_js(listing_url, waiting_time = [5, 1]):
    """
    Extracts HTML from JS pages: open, wait, click, wait, extract.
    """

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options = options) # Should probably be firefox?

    driver.get(listing_url)
    time.sleep(waiting_time[0])

    try:
        driver.find_element_by_class_name("____________"),click()
    except:
        pass # amenities button not found
    try:
        driver.find_element_by_class_name("____________").click()
    except:
        pass # prices button not found

    time.sleep(waiting_time[1])
    detail_page = driver.page_source

    driver.quit()

    return BeautifulSoup(detail_page, features = "html.parser")





def extract_element_data(soup, params):
    """
    Extracts data from a specified HTML element
    """

    # 1. Find the right tag
    if "class" in params:
        elements_found = soup.find_all(params["tag"], params["class"])
    else:
        elements_found = soup.find_all(params["tag"])
    
    # 2. Extract text from these tags
    if "get" in params:
        element_texts = [el.get(params["get"]) for el in elements_found]
    else:
        element_texts = [el.get_text() for el in elements_found]

    # 3. Select a particular text or concatenate all of them
    tag_order = params.get("order", 0)
    if tag_order == -1:
        output = "**_**".join(element_texts)
    else:
        output = element_texts[tag_order]
    
    return output