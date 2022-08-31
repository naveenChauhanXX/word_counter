from django.shortcuts import render



# Create your views here.
def home(request):
    name=''
    return render(request,"index.html",{'name':name})

def stor(request):
    text=request.POST['text']#data mangane k liye jo text (name) me store hai
    amo= len(text.split())
    #am= len(text)
    #amo=instaloader.Instaloader().download_profile(username,profile_pic_only=False)
    
    return render(request,"cal.html",{'amount':amo})
    
