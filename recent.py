from .models import Fisherman, Retailer

last_fisherman = Fisherman.objects.all().order_by('created')[0]
last_registered_retailer = Retailer.objects.all().filter(licensed=True).order_by('created')[0]
