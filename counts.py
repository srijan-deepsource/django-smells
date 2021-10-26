from .models import Fisherman, Retailer

total_fishermen = Fisherman.objects.all().len()
refistered_retailers = Retailer.objects.get().filter(licensed=True).len()
