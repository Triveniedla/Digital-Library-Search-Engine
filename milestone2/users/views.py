from django.shortcuts import render

# users/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView

from .forms import CustomUserCreationForm,HomeForm,UploadForm
from .token_generator import account_activation_token
from .models import SearchHistoryModel,HandleModel
from .elasticsearchETD import elasticsearchfun

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
from elasticsearch import Elasticsearch
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings


#-------------------------------------
#function for signup
def SignUpView(request):
    form = CustomUserCreationForm

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

#----------------------------------------------------
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
        return render(request, 'accountactivated.html', context)
    else:
        form = HomeForm()
        context = {'form':form}
        return render(request, 'accountactivated.html',context)
#----------------------------------------
#function for accountconfirmation
def accountconfirmation(request):
    template_name = 'accountconfirmation.html'
    return  render(request,template_name)
#----------------------------------------
#function for accountconfirmation
def accountactivated(request):
    template_name = 'accountactivated.html'
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
            whattosearch=filtersearchtext(form)
            #saving user history if the user is loggedin
            historysave(request,form,whattosearch)
            request.session["whattosearch"]=whattosearch
            return redirect('serp')

        else:
            msg=0
            searchtext=""
            output=["Not valid input"]

        args={'form':form,'msg':msg,'output':output,'text':searchtext}
        return render(request,self.template_name,args)
#----------------------------------------
def historysave(request,form,whattosearch):
    if request.user.is_authenticated:
        searchhistorystore=form.save(commit=False)
        searchhistorystore.user=request.user
        searchhistorystore.searchtext=whattosearch['title']
        searchhistorystore.save()
#-----------------------------------------
def filtersearchtext(form):

    searchtext= form.cleaned_data['searchtext']
    whattosearch={'title':searchtext}

    contributor_department= form.cleaned_data['contributor_department']
    if contributor_department !='':
        whattosearch['contributor_department']=contributor_department

    contributor_author= form.cleaned_data['contributor_author']
    if contributor_author !='':
        whattosearch['contributor_author']=contributor_author

    contributor_committeechair= form.cleaned_data['contributor_committeechair']
    if contributor_committeechair !='':
        whattosearch['contributor_committeechair']=contributor_committeechair

    description_degree= form.cleaned_data['description_degree']
    if description_degree !='':
        whattosearch['description_degree']=description_degree

    whattosearch['date1']=str(form.cleaned_data['date1'])
    whattosearch['date2']=str(form.cleaned_data['date2'])

    return whattosearch

#-------------------------------------
def SERPView(request):
    template_name='serp.html'

    if request.method=='GET':
        form=HomeForm()
        whattosearch=request.session["whattosearch"]
        output,msg=elasticsearchfun(whattosearch)

        searchtext=''

        for key in whattosearch.keys():
            if key not in ['date1','date2']:
                searchtext=searchtext+whattosearch[key]+", "
        searchtext=searchtext+"between "+whattosearch['date1']+" and "+whattosearch['date2']

        args={'form':form,'msg':msg,'output':output,'text':searchtext}
        return render(request,template_name,args)

    if request.method=='POST':
        form=HomeForm(request.POST)
        if form.is_valid():
            whattosearch=filtersearchtext(form)
            #saving user history if the user is loggedin
            historysave(request,form,whattosearch)
            request.session["whattosearch"]=whattosearch
            return redirect('serp')
        else:
            msg=0
            searchtext=""
            output=["Not valid input"]

        form=HomeForm()
        args={'form':form,'msg':msg,'output':output,'text':searchtext}
        return render(request,template_name,args)

    args={'form':form,'msg':0,'output':["Some issue with SERPview"],'text':''}
    return render(request,template_name,args)
#----------------------------------------
#function for accountconfirmation
def SERPdetailsView(request):
    template_name = 'serpdetails.html'

    if request.method == 'GET':
        return  render(request,template_name)

    if request.method == 'POST':
        handle=request.POST.get('handle',None)
        whattosearch={"handle":handle}
        output,msg=elasticsearchfun(whattosearch,type="handlequery")

        try:
            pdfnames=output[0]["relation_haspart"]
            if str(type(pdfnames))=="<class 'str'>":
                pdfnames=[pdfnames]

            fnames=[]
            for fname in pdfnames:
                dumdict={}
                dumdict['url']="http://127.0.0.1:8000/media/dissertation/"+handle+"/"+fname

                dumdict['name']=fname
                fnames.append(dumdict)
        except:
            msg=0
            fnames=[]
            output=["PDF files not found"]

        args={'output':output,'msg':msg,'fnames':fnames}
        return render(request,template_name,args)

    return  render(request,template_name)

# -------------------------------------
def UploadView(request):

    msg=0
    if request.method=='GET':
        form=UploadForm()

    if request.method =='POST':
        form=UploadForm(request.POST,request.FILES)
        if form.is_valid():

            whattoindex={}
            #indexing strings
            whattoindex['title']=form.cleaned_data["title"]
            whattoindex['contributor_author']=form.cleaned_data["contributor_author"]
            whattoindex['description_abstract']=form.cleaned_data["description_abstract"]
            whattoindex['contributor_committeechair']=form.cleaned_data["contributor_committeechair"]
            whattoindex['contributor_department']=form.cleaned_data["contributor_department"]
            whattoindex['date_issued']=str(form.cleaned_data["date_issued"])
            whattoindex['identifier_sourceurl']=form.cleaned_data["identifier_sourceurl"]

            #Uploading comitte membsers into list
            comitmembs=form.cleaned_data["contributor_committeemember"]
            try:
                comitmembs=comitmembs.split('"')[1::2]
                if len(comitmembs)==0:
                    comitmembs=form.cleaned_data["contributor_committeemember"]
                    comitmembs=comitmembs.split()[1::2]
                if len(comitmembs)==0:
                    comitmembs=[form.cleaned_data["contributor_committeemember"]]
            except:
                comitmembs=[form.cleaned_data["contributor_committeemember"]]
            whattoindex['contributor_committeemember']=comitmembs

            #Uploading subject into list
            keywords=form.cleaned_data["contributor_committeemember"]
            try:
                keywords=keywords.split('"')[1::2]
                if len(keywords)==0:
                    keywords=form.cleaned_data["subject"]
                    keywords=keywords.split()[1::2]
                if len(keywords)==0:
                    keywords=[form.cleaned_data["subject"]]
            except:
                keywords=[form.cleaned_data["subject"]]
            whattoindex['subject']=keywords

            #uplodaing thehandle number by querying the model database
            handleobjects=HandleModel.objects.all()
            if len(handleobjects)==0:
                handlenum=29581
            else:
                handlenum=int(handleobjects[len(handleobjects)-1].handle)+1
            #increasing the current handle number by 1 in the database
            if request.user.is_authenticated:
                handlestore=form.save(commit=False)
                handlestore.user=request.user
                handlestore.handle=str(handlenum)
                handlestore.save()
            whattoindex['handle']=handlenum

            #Uploading the relation_haspart into list
            uploaded_file=request.FILES['file']
            fs=FileSystemStorage("media/dissertation/"+str(handlenum)+"/")
            fs.save(uploaded_file.name,uploaded_file)
            whattoindex['relation_haspart']=[uploaded_file.name]
            output,msg=elasticsearchfun(whattoindex,type="index")

        else:
            form=UploadForm()

    args={"form":form}

    return render(request,'upload.html',args)
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
