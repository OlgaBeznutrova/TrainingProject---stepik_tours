from random import sample

from django.http import Http404, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render

from tours import data


def main_view(request):
    random_tours = sample(data.tours.items(), 6)
    return render(request, "tours/index.html",
                  context={"subtitle": data.subtitle, "description": data.description,
                           "random_tours": random_tours})


def departure_view(request, departure):
    try:
        departure_rus = data.departures[departure]
    except KeyError:
        raise Http404
    tours = [{tour_id: tour} for tour_id, tour in data.tours.items() if tour["departure"] == departure]
    prices = [value["price"] for tour in tours for value in tour.values()]
    nights = [value["nights"] for tour in tours for value in tour.values()]
    return render(request, "tours/departure.html",
                  context={"tours": tours, "departure_rus": departure_rus, "amount_tours": len(tours),
                           "min_price": min(prices), "max_price": max(prices), "min_nights": min(nights),
                           "max_nights": max(nights)
                           }
                  )


def tour_view(request, tour_id):
    try:
        tour = data.tours[tour_id]
    except KeyError:
        raise Http404
    departure_rus = data.departures[tour["departure"]]
    return render(request, "tours/tour.html",
                  context={"tour": tour, "departure_rus": departure_rus})


def custom_handler404(request, exception):
    return HttpResponseNotFound("Ресурс не найден!")


def custom_handler500(request):
    return HttpResponseServerError("Ошибка сервера!")
