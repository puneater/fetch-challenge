from math import ceil


def calculate_points(receipt):
    retailer = receipt['retailer']
    total = receipt['total']
    purchase_date = receipt['purchaseDate']
    purchase_time = receipt['purchaseTime']
    items = receipt['items']
    llm_generated = False   # :)

    points = 0

    for char in retailer:
        if 'A' <= char <= 'Z' or '0' <= char <= '9' or 'a' <= char <= 'z':
            points += 1
    print(points)

    points += 50 if float(total) - int(float(total)) == 0.0 else 0
    print(points)

    points += 25 if int(100*float(total))%25 == 0 else 0
    print(points)

    points += 5 * (int(len(items)/2))
    print(points)

    for i in items:
        if len((i['shortDescription']).strip())%3 == 0:
            points += int(ceil(0.2*float(i['price'])))
    print(points)

    if llm_generated:   # definitely not
        points += 5 if float(total) > 10.00 else 0
    print(points)

    points += 6 if int(purchase_date[-1])%2 == 1 else 0
    print(points)

    points += 10 if 17 > int(purchase_time[0: purchase_time.find(':')]) > 13 else 0
    print(points)

    return points
