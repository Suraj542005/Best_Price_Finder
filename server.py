from flask import Flask, render_template, request
from colorama import Fore
from Webs_for_Scrap_fun import amazon_scrap, flipkart_scrap

app = Flask(__name__)


"""To Find the Best Match"""


def best_match(product_search_list, product_dictionary):
    """To Find the Best Match"""

    print(Fore.WHITE + "ok" + Fore.RESET)
    # search_list = search_query.lower().split()
    # for product in product_dict:
    product_name_list = []
    product_keys = []
    short_listed_dict = {}
    for product in product_dictionary:
        product_keys.append(product)
        product_name_list.append(product.lower().split())

    for element in product_search_list:
        key_count = 0

        for product_element_list in product_name_list:
            if element in product_element_list:

                if product_keys[key_count] in short_listed_dict:
                    short_listed_dict[product_keys[key_count]] += 1
                elif product_keys[key_count] not in short_listed_dict:
                    short_listed_dict[product_keys[key_count]] = 1

            # print(product_keys)
            key_count += 1

    # print("The Length of the Product Keys are :", len(product_keys))
    print("The Short Listed Dictionary is .....")
    # print(short_listed_dict)
    for i in short_listed_dict:
        print(str(i) + "----->" + str(short_listed_dict[i]))

    # max_match = 0
    final_short_list = {}
    for i in range(10):
        max_match = 0
        for key in short_listed_dict:
            if short_listed_dict[key] >= max_match:
                max_match = short_listed_dict[key]
        print("The Most number of Times Matched Product is :", max_match)
        for match in short_listed_dict:
            if short_listed_dict[match] == max_match:
                final_short_list[match] = short_listed_dict[match]
                short_listed_dict.pop(match)
                print(f"We Just Popped the {match}")
                break  # iske bajase se no. ek hi baar aaraha hai

    print(Fore.BLUE + "Showing the Final Short Listed Data....." + Fore.RESET)

    for i in final_short_list:
        print(str(i) + "----->" + str(final_short_list[i]))

    final_product_dict = {}

    for i in final_short_list:
        final_product_dict[i] = product_dictionary[i]

    return final_product_dict


"""To Display Lago of the Website from that the Product is coming"""


def logo_adder(product_dict):
    """To Display Lago of the Website from that the Product is coming"""
    for i in product_dict:
        if "flipkart.com/" in product_dict[i][4]:
            product_dict[i].append("static/flipkart.png")
        elif "amazon.in/" in product_dict[i][4]:
            product_dict[i].append("static/amazon.png")
        else:
            pass


"""To Compair the prices"""


def price_comparison(product_dict):
    """To Compair the Prices"""
    price_list = []
    temp_dict = {}
    for product in product_dict:
        price = ""
        for i in product_dict[product][0]:
            if i.isdigit():
                price += i
        temp_dict[product] = [int(price), product_dict[product][1],
                              product_dict[product][2], product_dict[product][3],
                              product_dict[product][4]]
        price_list.append(int(price))
    price_list.sort()
    # print(price_list)
    shorted_dict = {}
    # for product in temp_dict:
    for i in price_list:
        for key in temp_dict:
            if temp_dict[key][0] == i:
                for link in product_dict:
                    if temp_dict[key][4] == product_dict[link][4]:
                        shorted_dict[key] = [product_dict[link][0],     # Change it with ',' System.
                                             temp_dict[key][1],
                                             temp_dict[key][2],
                                             temp_dict[key][3],
                                             temp_dict[key][4]]

    return shorted_dict


"""To Compair the Offers"""


def offer_comparison(product_dict):
    """To Compair the Offers"""

    offer_list = []
    temp_dict = {}
    for product in product_dict:
        off = ""
        # print(product_dict[product][1])
        for i in product_dict[product][1]:
            if i.isdigit():
                off += i
        if off == "":
            continue
        temp_dict[product] = [product_dict[product][0], int(off),
                              product_dict[product][2], product_dict[product][3],
                              product_dict[product][4]]
        offer_list.append(int(off))
    offer_list.sort()

    # print(Fore.GREEN + "-"*200 + Fore.RESET)
    # print("Printing The Shorted Offer List.....")
    # print(offer_list)
    # print(Fore.GREEN + "-"*200 + Fore.RESET)

    shorted_dict = {}
    for i in offer_list:
        for key in temp_dict:
            if str(temp_dict[key][1]) == str(i):
                shorted_dict[key] = [temp_dict[key][0],
                                     product_dict[key][1],
                                     temp_dict[key][2],
                                     temp_dict[key][3],
                                     temp_dict[key][4]]

    # print(Fore.BLUE + "The Shorted Dict is ....." + Fore.RESET)
    # for i in shorted_dict:
    #     print(str(i) + "----->" + str(shorted_dict[i]))

    reversed_dict = {k: v for k, v in reversed(list(shorted_dict.items()))}

    # print(Fore.GREEN + "-" * 200 + Fore.RESET)
    # print("Printing The Reversed Shorted Offer List.....")
    # print(reversed_dict)
    # print(Fore.GREEN + "-" * 200 + Fore.RESET)

    product_dict = reversed_dict
    return product_dict


"""Main Code for starting the Server"""


@app.route('/', methods=['GET', 'POST'])
def webapp():
    if request.method == 'POST':
        html_search_input = request.form.get("html_input")
        search_input = html_search_input
        print("Searching for", search_input + ".....")
        search_input_list = search_input.lower().split()
        search_input = ""
        for word in search_input_list:
            search_input += word + "%20"

        product_dict = {}
        amazon_dict = {}
        flipkart_dict = {}
        final_dict = {}

        print(Fore.BLUE + "Fetching Data From Flipkart Website On Server File" + Fore.RESET)
        flipkart_dict = flipkart_scrap(search_input, flipkart_dict)
        print("Length of the Flipkart Dict is :", len(flipkart_dict))

        print(Fore.BLUE + "Fetching Data From Amazon Website On Server File" + Fore.RESET)
        amazon_dict = amazon_scrap(search_input, amazon_dict)
        print("Length of the Amazon Dict is :", len(amazon_dict))

        print(Fore.MAGENTA + "Printing Final Dict after Flipkart" + Fore.RESET)
        for i in flipkart_dict:
            print(i, flipkart_dict[i])

        print(Fore.MAGENTA + "Printing Final Dict after Amazon" + Fore.RESET)
        for i in amazon_dict:
            print(i, amazon_dict[i])

        final_dict.update(flipkart_dict)
        final_dict.update(amazon_dict)
        # best_match(search_input_list, final_dict)

        # product_dict = final_dict
        print(Fore.YELLOW + "*"*200 + Fore.RESET)
        print("Length of the Final Dict is :", len(final_dict))
        print(Fore.BLUE + "Printing the Product Dict From Server ....." + Fore.RESET)
        for i in final_dict:
            print(i, final_dict[i])

        # amazon_product_dict.update(flipkart_dict)
        # amazon_product_dict = offer_comparison(product_dict)
        # amazon_product_dict = price_comparison(product_dict)
        # logo_adder(amazon_product_dict)
        # print(Fore.LIGHTRED_EX + "*"*200 + Fore.RESET)
        # print(Fore.BLUE + "Printing the Product Dict before Offer Comparison ....." + Fore.RESET)
        # count = 1
        # for i in final_dict:
        #     if count == 6:
        #         break
        #     else:
        #         print(i, final_dict[i])
        #         count += 1

        final_dict = offer_comparison(final_dict)

        # print(Fore.LIGHTRED_EX + "*" * 200 + Fore.RESET)
        # print(Fore.BLUE + "Printing the Product Dict After Offer Comparison ....." + Fore.RESET)
        # count = 1
        # for i in final_dict:
        #     if count == 6:
        #         break
        #     else:
        #         print(i, final_dict[i])
        #         count += 1
        # print(Fore.LIGHTRED_EX + "*" * 200 + Fore.RESET)

        final_dict = price_comparison(final_dict)
        logo_adder(final_dict)
        final_dict = best_match(search_input_list, final_dict)
        # print("Printing after logo.....")
        # print(amazon_product_dict)
        return render_template("main.html", product_dict=final_dict)
        # return render_template("main.html", product_dict=amazon_product_dict)
        # return render_template("main.html", product_dict=product_dict)

    return render_template("main.html")


app.run()
