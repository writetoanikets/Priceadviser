from .models import Link
from .utils import get_data


def main():
    qs = Link.objects.all()
    for singlelink in qs:
        url = singlelink.url
        name, price = get_data(url)
        old_price = singlelink.current_price
        if singlelink.current_price:
            if price != old_price:
                diff = price - old_price
                singlelink.price_difference = round(diff, 2)
                singlelink.old_price = old_price
        else:
            singlelink.old_price = 0
            singlelink.price_difference = 0
        singlelink.name = name
        singlelink.current_price = price
        singlelink.save()


if __name__ == '__main__':
    main()
