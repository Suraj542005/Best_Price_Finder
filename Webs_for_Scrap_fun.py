import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from colorama import Fore

"""Flipkart Website"""


def flipkart_scrap(search_query, product_dict):
    print(Fore.YELLOW + "Data Scraping from Flipkart Website ....." + Fore.RESET)

    url = "https://www.flipkart.com/search?q=" + search_query
    print("The Web Site Link is ----->", url)
    while True:
        try:
            ua = UserAgent()
            headers = {'User-Agent': ua.random}  # Correct initialization of headers dictionary
            print("Header ----->", headers)
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                print("Successfully Fetched 1st Time Data from Flipkart Website.....")
                soup = BeautifulSoup(response.text, "lxml")
                names = soup.find_all("div", class_="_4rR01T")
                prices = soup.find_all("div", class_="_30jeq3 _1_WHN1")
                offers = soup.find_all("div", class_="_3Ay6Sb")
                ratings = soup.find_all("div", class_="_3LWZlK")
                images = soup.find_all("img", class_="_396cs4")
                web_link = soup.find_all("a", class_="_1fQZEK")

                min_length = len(names)
                if len(prices) < min_length:
                    min_length = len(prices)
                elif len(offers) < min_length:
                    min_length = len(offers)
                elif len(ratings) < min_length:
                    min_length = len(ratings)
                elif len(images) < min_length:
                    min_length = len(images)
                elif len(web_link) < min_length:
                    min_length = len(web_link)

                for count in range(min_length):

                    if names[count].text != "" and prices[count].text != "" and \
                            offers[count].text != "" and ratings[count].text != "" and \
                            images[count].get("src") != "" and web_link[count].get("href") != "":
                        product_dict[names[count].text] = [prices[count].text,
                                                           offers[count].text,
                                                           ratings[count].text + " Rating",
                                                           images[count].get("src"),
                                                           "https://flipkart.com" + web_link[count].get("href")]

                # for i in product_dict:
                #     print(str(i) + "----->" + str(product_dict[i]))
                # print("The Total Products are", len(product_dict))
                # print("The Links for Products.....")

                if len(product_dict) == 0:
                    print("Successfully Fetched 2nd Time Data from Flipkart Website.....")
                    soup = BeautifulSoup(response.text, "lxml")
                    names = soup.find_all("a", class_="s1Q9rs")
                    prices = soup.find_all("div", class_="_30jeq3")
                    offers = soup.find_all("div", class_="_3Ay6Sb")
                    ratings = soup.find_all("div", class_="_3LWZlK")
                    images = soup.find_all("img", class_="_396cs4")
                    web_link = soup.find_all("a", class_="s1Q9rs")

                    min_length = len(names)
                    if len(prices) < min_length:
                        min_length = len(prices)
                    elif len(offers) < min_length:
                        min_length = len(offers)
                    elif len(ratings) < min_length:
                        min_length = len(ratings)
                    elif len(images) < min_length:
                        min_length = len(images)
                    elif len(web_link) < min_length:
                        min_length = len(web_link)

                    for count in range(min_length):
                        if names[count].text != "" and prices[count].text != "" and \
                                offers[count].text != "" and ratings[count].text != "" and \
                                images[count].get("src") != "" and web_link[count].get("href") != "":
                            product_dict[names[count].text] = [prices[count].text,
                                                               offers[count].text,
                                                               ratings[count].text + " Rating",
                                                               images[count].get("src"),
                                                               "https://flipkart.com" + web_link[count].get("href")]

                    # for i in product_dict:
                    #     print(str(i) + "----->" + str(product_dict[i]))
                    # print("The Total Products are", len(product_dict))

                    if len(product_dict) == 0:
                        print("Successfully Fetched 3nd Time Data from Flipkart Website.....")
                        soup = BeautifulSoup(response.text, "lxml")
                        names = soup.find_all("a", class_="IRpwTa")
                        prices = soup.find_all("div", class_="_30jeq3")
                        offers = soup.find_all("div", class_="_3Ay6Sb")
                        ratings = soup.find_all("div", class_="_3LWZlK")
                        images = soup.find_all("img", class_="_2r_T1I")
                        web_link = soup.find_all("a", class_="_2UzuFa")

                        min_length = len(names)
                        if len(prices) < min_length:
                            min_length = len(prices)
                        elif len(offers) < min_length:
                            min_length = len(offers)
                        elif len(ratings) < min_length:
                            min_length = len(ratings)
                        elif len(images) < min_length:
                            min_length = len(images)
                        elif len(web_link) < min_length:
                            min_length = len(web_link)

                        for count in range(min_length):
                            if names[count].text != "" and prices[count].text != "" and \
                                    offers[count].text != "" and ratings[count].text != "" and \
                                    images[count].get("src") != "" and web_link[count].get("href") != "":
                                product_dict[names[count].text] = [prices[count].text,
                                                                   offers[count].text,
                                                                   ratings[count].text + " Rating",
                                                                   images[count].get("src"),
                                                                   "https://flipkart.com" + web_link[count].get("href")]

                        # for i in product_dict:
                        #     print(str(i) + "----->" + str(product_dict[i]))
                        # print("The Total Products are", len(product_dict))

                        break
                    else:
                        break
                else:
                    break
            else:
                print("Response Status is :", response.status_code)

        except Exception as e:
            print("Error:", e)
            continue
    print(Fore.GREEN + "Scraped Successfully....." + Fore.RESET)
    return product_dict


"""Amazon Website"""


def amazon_scrap(search_query, product_dict):
    print(Fore.YELLOW + "Data Scraping from Amazon Website ....." + Fore.RESET)

    url = "https://www.amazon.in/s?k=" + search_query
    print("The Web Site Link is ----->", url)

    while True:
        # try:
        ua = UserAgent()
        headers = {'User-Agent': ua.random}
        r = requests.get(url, headers=headers)

        if r.status_code == 200:
            print(Fore.GREEN + "Successfully Fetched Data from Amazon Website....." + Fore.RESET)
            print(Fore.BLUE + "Fetching 1st Time Data ....." + Fore.RESET)

            soup = BeautifulSoup(r.text, "html5lib")
            # soup = BeautifulSoup(r.text, "lxml")

            # print(Fore.RED + "Printing the Div Data....." + Fore.RESET)
            div_data = soup.find_all("div", "puisg-row")

            for i in div_data:
                try:
                    sponsor = i.find("span", class_="a-color-secondary")
                    if sponsor.text == "Sponsored":
                        print("Sponsored is Present.....")
                        continue
                    else:
                        product_name = i.find("span", class_="a-size-medium a-color-base a-text-normal")
                except:
                    product_name = i.find("span", class_="a-size-medium a-color-base a-text-normal")

                if product_name is not None:
                    product_price = i.find("span", class_="a-price-whole")
                    product_rating = i.find("div", class_="a-row").find("span")
                    product_offer = i.find("div", class_="a-row a-size-base a-color-base").find_all("span")
                    product_image = i.find("img", class_="s-image")
                    product_link = i.find("a",
                                          class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
                    if product_price is not None and product_offer is not None and product_rating is not None \
                            and product_image is not None and product_link is not None:
                        product_dict[product_name.text] = ["₹" + str(product_price.text),
                                                           product_offer[-1].text[1:len(product_offer[-1].text) - 1:],
                                                           product_rating.text.split()[0],
                                                           product_image.get("src"),
                                                           "https://www.amazon.in" + product_link.get("href")]
            if len(product_dict) == 0:
                print(Fore.BLUE + "Fetching 2nd Time Data ....." + Fore.RESET)
                print(Fore.RED + "Printing the Div Data....." + Fore.RESET)
                div_data = soup.find_all("div",
                                         "sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20")

                for j in div_data:
                    try:
                        sponsor = j.find("span", class_="a-color-secondary")
                        if sponsor.text == "Sponsored":
                            print("Sponsored is Present.....")
                            continue
                        else:
                            product_name_h2 = j.find("span", class_="a-size-base-plus a-color-base")
                            product_name = j.find("span", class_="a-size-base-plus a-color-base a-text-normal")
                    except:
                        product_name_h2 = j.find("span", class_="a-size-base-plus a-color-base")
                        product_name = j.find("span", class_="a-size-base-plus a-color-base a-text-normal")

                    if product_name_h2 is not None and product_name is not None:
                        print(product_name_h2.text + product_name.text)
                        product_price = j.find("span", class_="a-price-whole")
                        product_rating = j.find("span", class_="a-icon-alt")
                        product_offer = j.find("div", class_="a-row a-size-base a-color-base").find_all("span")
                        product_image = j.find("img", class_="s-image")
                        product_link = j.find("a",
                                              class_="a-link-normal s-no-hover s-underline-text s-underline-link-text s-link-style a-text-normal")

                        if product_price is not None and product_offer is not None and product_rating is not None \
                                and product_image is not None and product_link is not None:
                            product_dict[product_name.text] = ["₹" + str(product_price.text),
                                                               product_offer[-1].text[
                                                               1:len(product_offer[-1].text) - 1:],
                                                               product_rating.text.split()[0],
                                                               product_image.get("src"),
                                                               "https://www.amazon.in" + product_link.get("href")]
                # break

                if len(product_dict) == 0:
                    print(Fore.BLUE + "Fetching 3nd Time Data ....." + Fore.RESET)
                    print(Fore.RED + "Printing the Div Data....." + Fore.RESET)
                    div_data = soup.find_all("div",
                                             "sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20")

                    for j in div_data:
                        sponsor = j.find("span", class_="a-color-secondary")
                        try:
                            if sponsor.text == "Sponsored":
                                print("Sponsored is Present.....")
                                continue
                            else:
                                product_name = j.find("span", class_="a-size-base-plus a-color-base a-text-normal")
                        except:
                            product_name = j.find("span", class_="a-size-base-plus a-color-base a-text-normal")
                        if product_name is not None:
                            print(product_name.text)
                            product_price = j.find("span", class_="a-price-whole")
                            product_rating = j.find("span", class_="a-icon-alt")
                            product_offer = j.find("div", class_="a-row a-size-base a-color-base").find_all("span")
                            product_image = j.find("img", class_="s-image")
                            product_link = j.find("a",
                                                  class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")

                            if product_price is not None and product_offer is not None and product_rating is not \
                                    None and product_image is not None and product_link is not None:
                                product_dict[product_name.text] = ["₹" + str(product_price.text),
                                                                   product_offer[-1].text[
                                                                   1:len(product_offer[-1].text) - 1:],
                                                                   product_rating.text.split()[0],
                                                                   product_image.get("src"),
                                                                   "https://www.amazon.in" + product_link.get(
                                                                       "href")]
                    break

                else:
                    break
            else:
                break
        else:
            print("Failed to Fetch with Status Code ----->", r.status_code)
    # except Exception as e:
    #     print("An exception occurred:", e)
    #     continue

    print(Fore.GREEN + "Scraped Successfully....." + Fore.RESET)
    return product_dict


"""For Checking Code Before Connecting to Server"""

# product_dict = {}
# search_input = input("Enter the Product Name :")
# print("Searching for", search_input + ".....")
# search_input_list = search_input.lower().split()
# search_input = ""
# for word in search_input_list:
#     search_input += word + "%20"
#
# Updated_amazon(search_input, product_dict)
#
# for i in product_dict:
#     print(str(i) + "----->" + str(product_dict[i]))
