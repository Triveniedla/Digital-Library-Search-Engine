# users/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm, HomeForm
from django.shortcuts import render

from django.contrib import messages
from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user_model
from .token_generator import account_activation_token
from .models import SearchHistoryModel


from .elasticsearchETD import elasticsearchfun

def SignUpView(request):
    form_class = CustomUserCreationForm

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            email_subject = 'Activate Your Account'

            message = render_to_string('activateaccount.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()
            return redirect('accountconfirmation')
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})

#-------------------------------------
def activateaccount(request, uidb64, token):

    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):

        user.is_active = True
        user.save()
        login(request, user)
        form = HomeForm()

        context = {'uidb64':uidb64, 'token':token,'form':form,'text':"Your account is activated!"}
        return render(request, 'home.html', context)
    else:

        print("not entered")
        form = HomeForm()
        context = {'form':form}
        return render(request, 'home.html',context)
#----------------------------------------
#function for accountconfirmation
def accountconfirmation(request):
    template_name = 'accountconfirmation.html'
    return  render(request,template_name)
#-------------------------------------
#class for HomePageView and elastic search
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get(self,request):
        form=HomeForm()

        args={'form':form}
        return render(request,self.template_name,args)

    #taking the input from the search page
    def post(self,request):
        form=HomeForm(request.POST)
        if form.is_valid():
            searchtext= form.cleaned_data['searchtext']
            whattosearch={'searchtext':searchtext}
            if request.user.is_authenticated:
                searchhistorystore=form.save(commit=False)
                searchhistorystore.user=request.user
                searchhistorystore.searchtext=searchtext
                searchhistorystore.save()
            request.session["whattosearch"]=whattosearch

            return redirect('serp')



        else:
            msg=0
            searchtext = ""
            output=["Not valid input"]


        args={'form':form,'msg':msg,'output':output,'text':searchtext}
        return render(request,self.template_name,args)
#-------------------------------------
def SERPView(request):
    template_name = 'serp.html'

    print(request.session["whattosearch"])

    if request.method=='GET':
        whattosearch=request.session["whattosearch"]
        searchtext=whattosearch["searchtext"]
        output,msg = elasticsearchfun(request.session["whattosearch"])
        form=HomeForm()
        args={'form':form,'msg':msg,'output':output,'text':searchtext}
        return render(request,template_name,args)

    if request.method=='POST':

        form=HomeForm(request.POST)
        if form.is_valid():
            searchtext= form.cleaned_data['searchtext']
            whattosearch={'searchtext':searchtext}
            if request.user.is_authenticated:
                searchhistorystore=form.save(commit=False)
                searchhistorystore.user=request.user
                searchhistorystore.searchtext=searchtext
                searchhistorystore.save()
            request.session["whattosearch"]=whattosearch
            return redirect('serp')

        else:
            msg=0
            searchtext = ""
            output=["Not valid input"]


        form=HomeForm()
        args={'form':form,'msg':msg,'output':output,'text':searchtext}
        return render(request,template_name,args)

    args={'form':form,'msg':0,'output':["Some issue with SERPView"],'text':''}
    return render(request,template_name,args)


#-------------------------------------
#class for HomePageView and elastic search
def SearchHistoryView(request):
    template_name = 'searchhistory.html'

    if request.method == 'GET':
        searchhistoryquery=SearchHistoryModel.objects.filter(user_id=request.user.id)
        args={"searchhistoryquery":searchhistoryquery}

        return render(request,template_name,args)

    if request.method == 'POST':
        return render(request,template_name)
