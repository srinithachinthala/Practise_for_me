from django.shortcuts import render
from .forms import example_form
from .models import model_for_form
# Create your views here.
def fun1(request):
    exf=example_form(request.POST,request.FILES)
    if request.method=="POST":
        print("outer")
        if exf.is_valid():
            print("inner")
            Name=exf.cleaned_data["Name"]
            DOB=exf.cleaned_data["DOB"]
            Email_Id=exf.cleaned_data["Email_Id"]
            phone_Number=exf.cleaned_data["phone_Number"]
            Flat_no=exf.cleaned_data["Flat_no"]
            street=exf.cleaned_data["street"]
            country=exf.cleaned_data["country"]
            upload_photo=request.FILES["upload_photo"]
            print(upload_photo)
            print(country)
            model_res=model_for_form(Name=Name,DOB=DOB,Email_Id=Email_Id,phone_Number=phone_Number, street=street,Flat_no=Flat_no,country=country,upload_photo=upload_photo)
            model_res.save()
            exf=example_form()
            # res.delete()
            return render(request,"second.html",{"ex_f":exf})

    exf=example_form()
    res=model_for_form.objects.all()
    return render(request,"second.html",{"ex_f":exf,"f_res":res})
    
   
    
    
    