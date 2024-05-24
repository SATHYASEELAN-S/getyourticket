from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse

from ticket.models import BusInfo,Stop,Travelinfo
from ticket.form import BusInfoForm,StopForm
from django.contrib.auth.decorators import login_required





# def ticket(request):

#     return HttpResponse("hello")



# # @login_required
def home(request):
    busform=BusInfoForm()
    stopform=StopForm()

    if request.method=="POST":
        busform=BusInfoForm(request.POST)
        # stopform=StopForm(request.POST)
        if busform.is_valid():
            bus=busform.save(commit=False)
            bus.user=request.user
            bus.save()
            # stop=stopform.save(commit=False)
            # stop.bus_no=bus
            # stop.save()
            return HttpResponse("success")
    return render(request,'booking.html',{'bus':busform})


# def bus(request):
#     bus_no="TN22BN002"
#     bus_info = get_object_or_404(BusInfo, bus_no=bus_no)
#     bus = BusInfo.objects.filter(bus_no=bus_no)

#     # Use first() to get the first result from the queryset
#     travel = Travelinfo.objects.filter(bus_no=bus_info).first()
#     stops = Stop.objects.filter(bus_no=travel)

#     context={
#         'travel':travel,
#         'stops':stops,
#         'bus':bus,
#     }
#     print(context['stops'])
#     return render(request,"booking.html",context)

def bus(request):
    # bus_no = "TN22BN002"
    bus_no=request.GET.get("busno")
    print(bus_no)
    bus_info = get_object_or_404(BusInfo, bus_no=bus_no)
    bus = BusInfo.objects.filter(bus_no=bus_no)
    travel = Travelinfo.objects.filter(bus_no=bus_info).first()
    stops = Stop.objects.filter(bus_no=travel)

    context = {
        'travel': travel,
        'stops': stops,
        'bus': bus,
    }
    if request.method == 'POST' :
        print(request.POST['seats'])
        seats = int(request.POST['seats'])
        print("seats",seats)
        print("before tokm")
        # tokm=int(request.POST["tokm"])
        tokm=0
        print("after tokm")
        print("tokm ",tokm)
        price=((tokm*1.2)//2)
        if price < travel.min_price:
            price=travel.min_price 
        price*=seats
        print("price",price)
        return JsonResponse({'price': price})
    return render(request, "booking.html", context)