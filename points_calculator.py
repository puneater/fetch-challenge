from math import ceil


def calculate_points(receipt):

    points = 0

    if "retailer" in receipt:
        retailer = receipt['retailer']
        for char in retailer:
            if 'A' <= char <= 'Z' or '0' <= char <= '9' or 'a' <= char <= 'z':
                points += 1

    if "total" in receipt:
        total = receipt['total']
        points += 50 if float(total) - int(float(total)) == 0.0 else 0

        points += 25 if int(100*float(total))%25 == 0 else 0

    if "items" in receipt:
        items = receipt['items']
        for i in items:
            if len((i['shortDescription']).strip())%3 == 0:
                points += int(ceil(0.2*float(i['price'])))

        points += 5 * (int(len(items) / 2))

    llm_generated = False   # :)
    if llm_generated:   # definitely not
        points += 5 if float(total) > 10.00 else 0

    if "purchaseDate" in receipt:
        purchase_date = receipt['purchaseDate']
        points += 6 if int(purchase_date[-1])%2 == 1 else 0

    if "purchaseTime" in receipt:
        purchase_time = receipt['purchaseTime']
        points += 10 if 16 > int(purchase_time[0: purchase_time.find(':')]) >= 14 and purchase_time != "14:00" else 0

    return points
