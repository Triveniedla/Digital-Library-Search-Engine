from django.shortcuts import render

# users/views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView

from .forms import CustomUserCreationForm,HomeForm,UploadForm,SaveItemForm, LikeItemForm
from .token_generator import account_activation_token
from .models import SearchHistoryModel,HandleModel,SaveItemModel, LikeItemModel
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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import bleach
from datetime import date
import requests
from django.contrib.auth.forms import AuthenticationForm

def LoginView(request):
    form = AuthenticationForm()
    msg =""
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        # Begin reCAPTCHA validation 
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response}
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        # End reCAPTCHA validation

        if result['success']:
            if form.is_valid():                
                email = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(email = email, password=password)
                if user is not None:
                    login(request,user)
                    return redirect('home')
                else:
                    msg = "Invalid username or password"
            else:
                msg = "Invalid username or password"
        else:
            msg = "Validate the recaptche"
    
    return render(request,"registration/login.html",{"form":form,"msg":msg})

#-------------------------------------
#function for signup
def SignUpView(request):
    form = CustomUserCreationForm
    msg =""

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        # Begin reCAPTCHA validation 
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response}
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        # End reCAPTCHA validation

        if result['success']:
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
            msg = "Validate the Recaptche"
    else:
        form = CustomUserCreationForm()
        msg =""

    return render(request, 'signup.html', {'form': form,'msg':msg})
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

        try:
            searchhistorystore.contributor_department=whattosearch['contributor_department']
        except:
            pass
        try:
            searchhistorystore.contributor_author=whattosearch['contributor_author']
        except:
            pass
        try:
            searchhistorystore.contributor_committeechair=whattosearch['contributor_committeechair']
        except:
            pass

        try:
            searchhistorystore.description_degree=whattosearch['description_degree']
        except:
            pass

        searchhistorystore.date1=str(whattosearch['date1'])
        searchhistorystore.date2=str(whattosearch['date2'])
        searchhistorystore.save()
#-----------------------------------------
def bleachcleanfun(form,arg):
    return bleach.clean(form.cleaned_data[arg], strip=True, tags=[''])

def filtersearchtext(form):
    
    searchtext = bleachcleanfun(form,'searchtext')
    whattosearch={'title':searchtext}

    contributor_department= bleachcleanfun(form,'contributor_department')
    if contributor_department !='':
        whattosearch['contributor_department']=contributor_department

    contributor_author= bleachcleanfun(form,'contributor_author')
    if contributor_author !='':
        whattosearch['contributor_author']=contributor_author

    contributor_committeechair= bleachcleanfun(form,'contributor_committeechair')
    if contributor_committeechair !='':
        whattosearch['contributor_committeechair']=contributor_committeechair

    description_degree= bleachcleanfun(form,'description_degree')
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

        if msg:
            likeditems=LikeItemModel.objects
            for i in range(0,len(output)):
                output[i]["totlikes"]=len(likeditems.filter(handle=output[i]["handle"]))
                output[i]["liked"]=len(likeditems.filter(handle=output[i]["handle"], user_id=request.user.id))
        
                pdfmsg,pdfnames=pdflinks(output,i,output[i]["handle"])
                output[i]["pdfmsg"]=pdfmsg
                output[i]["pdfnames"]=pdfnames

                for npdf in range(0,len(output[i]["pdfnames"])):
                    name=output[i]["pdfnames"][npdf]["name"]
                    name=name[:3]+"..."+name[-5:]
                    output[i]["pdfnames"][npdf]["name"]=name

        numresults=len(output)
        output=paginationfun(output,request,10)
        
        totsearchtext=''
        for key in whattosearch.keys():
            if key not in ['date1','date2']:
                totsearchtext=totsearchtext+whattosearch[key]+", "
        totsearchtext=totsearchtext+"between "+whattosearch['date1']+" and "+whattosearch['date2']
        searchtext = whattosearch["title"]

        args={'form':form,'msg':msg,'output':output,'totsearchtext':totsearchtext,
        'searchtext':searchtext,'numresults':numresults}
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
        args={'form':form,'msg':msg,'output':output,'totsearchtext':searchtext,
        'searchtext':searchtext,'numresults':0}
        return render(request,template_name,args)

    args={'form':form,'msg':msg,'output':["Some issue with SERPview"],'totsearchtext':'',
    'searchtext':'','numresults':0}
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

        pdfmsg,pdfnames=pdflinks(output,0,handle)

        args={'output':output,'pdfmsg':pdfmsg,'pdfnames':pdfnames}
        return render(request,template_name,args)

    return  render(request,template_name)

def pdflinks(output,hnum,handle):

    try:
        pdfmsg=1
        rawpdfnames=output[hnum]["relation_haspart"]
        if str(type(rawpdfnames))=="<class 'str'>":
            rawpdfnames=[rawpdfnames]

        pdfnames=[]
        for fname in rawpdfnames:
            dumdict={}
            dumdict['url']="http://127.0.0.1:8000/media/dissertation/"+handle+"/"+fname

            dumdict['name']=fname
            pdfnames.append(dumdict)
    except:
        pdfmsg=0
        pdfnames=[]

    return pdfmsg,pdfnames
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
        if request.user.is_authenticated:
            searchhistoryquery=SearchHistoryModel.objects.filter(user_id=request.user.id).order_by('date').reverse()

            output=paginationfun(searchhistoryquery,request,15)

            args={"output":output}
            return render(request,template_name,args)
        return redirect('home')

    if request.method == 'POST':
        searchid=request.POST.get('searchid',None)
        searchhistoryquery=SearchHistoryModel.objects.filter(id=searchid)
        
        whattosearch={}            
        for arg in searchhistoryquery:
            whattosearch["title"]=arg.searchtext
            whattosearch['date1']=arg.date1
            whattosearch['date2']=arg.date2

            if len(arg.contributor_author)!=0:
                whattosearch['contributor_author']=arg.contributor_author

            if len(arg.contributor_committeechair)!=0:
                whattosearch['contributor_committeechair']=arg.contributor_committeechair

            if len(arg.contributor_department)!=0:
                whattosearch['contributor_department']=arg.contributor_department

            if len(arg.description_degree)!=0:
                whattosearch['contributor_degree']=arg.description_degree

            form=HomeForm()
            historysave(request,form,whattosearch)
            request.session["whattosearch"]=whattosearch
            return redirect('serp')

#-------------------------------------
#class for HomePageView and elastic search
def ClearHistoryView(request):
    
    if request.method == 'GET':
        return redirect('searchhistory')

    if request.method == 'POST':
        searchid=request.POST.get('searchid',None)        
        if int(searchid)==-1:
            SearchHistoryModel.objects.filter(user_id=request.user.id).delete()
        else:
            SearchHistoryModel.objects.filter(id=searchid).delete()
        return redirect('searchhistory')

#-------------------------------------
def getuseritems(request):
    usersitems=SaveItemModel.objects.filter(user_id=request.user.id)
    output=[]
    for arg in usersitems:
        whattosearch={"handle":arg.handle}
        dumoutput,msg=elasticsearchfun(whattosearch,type="handlequery")
        dumoutput[0]["id"]=arg.id
        output.append(dumoutput[0])
    return output

def SaveItemView(request):

    template_name = 'saveitem.html'    
    if request.method == 'GET':
        if request.user.is_authenticated:
            form=SaveItemForm()
            output=getuseritems(request)
            numresults=len(output)
            output=paginationfun(output,request,5)

            args={'form':form,'msgtext':"",'output':output,'numresults':numresults} 
            return render(request,template_name,args)
        else:
            return redirect('home')

    if request.method == 'POST':
        handle=request.POST.get('handle',None)

        try:
            form=SaveItemForm()
            saveitems=form.save(commit=False)
            saveitems.user=request.user
            saveitems.handle=handle
            saveitems.save()
            return redirect('saveitem')
        except:
            form=SaveItemForm()
            output=getuseritems(request)
            numresults=len(output)
            output=paginationfun(output,request,5)

            args={'form':form,'msgtext':"Already saved",'output':output,'numresults':numresults} 
            return render(request,template_name,args)

#-------------------------------------
#class for HomePageView and elastic search
def DeleteItemView(request):    
    if request.method == 'GET':
        return redirect('saveitem')
    if request.method == 'POST':
        deleteitemid=request.POST.get('deleteitemid',None)        
        if int(deleteitemid)==-1:
            SaveItemModel.objects.filter(user_id=request.user.id).delete()
        else:
            SaveItemModel.objects.filter(id=deleteitemid).delete()
        return redirect('saveitem')

def paginationfun(output,request,numpages):

    page = request.GET.get('page', 1)
    paginator = Paginator(output, numpages)
    try:
        output = paginator.page(page)
    except PageNotAnInteger:
        output = paginator.page(1)
    except EmptyPage:
        output = paginator.page(paginator.num_pages)
    
    return output

#-------------------------------------------------------------------
from django.http import JsonResponse
def LikeItemView(request):

    if request.method == 'GET':
        handle = int(request.GET.get('handle'))
        likeditems=LikeItemModel.objects

        if len(likeditems.filter(user_id=request.user.id,handle=handle)):
            likeditems.filter(user_id=request.user.id,handle=handle).delete()
        else:
            form=LikeItemForm()
            likeitems=form.save(commit=False)
            likeitems.user=request.user
            likeitems.handle=handle
            likeitems.save()
        result={}
        result["liked"]=len(likeditems.filter(user_id=request.user.id,handle=handle))
        result["handle"]=handle
        result["likecount"]=len(likeditems.filter(handle=handle))

        return JsonResponse(result)


    if request.method == 'POST':
       
        handle=request.POST.get('handle',None)
        form=LikeItemForm()
        likeitems=form.save(commit=False)
        likeitems.user=request.user
        likeitems.handle=handle
        likeitems.save()    

    args={'form':HomeForm()}
    return render(request,"home.html",args)
       