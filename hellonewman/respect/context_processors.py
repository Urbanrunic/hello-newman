from models import People


def respect(request):
    """ retrieves the list of items for the cities jump menus """

    people = People.objects.filter(published=True)

    return {'people': people}
    
