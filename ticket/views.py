from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from ticket.models import BusInfo,Stop,Travelinfo
from ticket.form import BusInfoForm,StopForm
from django.contrib.auth.decorators import login_required


def ticket(request):
    bus_no="TN22BN002"
    bus_info = get_object_or_404(BusInfo, bus_no=bus_no)
    bus = BusInfo.objects.filter(bus_no=bus_no)
    travel = Travelinfo.objects.filter(bus_no=bus_info).first()
    stops = Stop.objects.filter(bus_no=travel)

    context={
        'travel':travel,
        'stops':stops,
        'bus':bus,
    }
    print(context['stops'])
    return render(request,"bus.html",context)



# # @login_required
# def home(request):
#     busform=BusInfoForm()
#     stopform=StopForm()

#     if request.method=="POST":
#         busform=BusInfoForm(request.POST)
#         # stopform=StopForm(request.POST)
#         if busform.is_valid():
#             bus=busform.save(commit=False)
#             bus.user=request.user
#             bus.save()
#             # stop=stopform.save(commit=False)
#             # stop.bus_no=bus
#             # stop.save()
#             return HttpResponse("success")
#     return render(request,'bus.html',{'bus':busform})