from .models import Country


def get_countries_all():
    return Country.objects.all()


def add_country(name):
    country = Country(name=name)
    country.save()
