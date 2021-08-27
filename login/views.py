from django.shortcuts import render,HttpResponse,redirect
from login.models import Contact
from login.models import Profile
from login.models import Phishing,Date_user
from .forms import MyFileUploadForm
# from login.models import Template_Category
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_exempt
from django.core.files.storage import FileSystemStorage
from django.core import mail
# from django.http import HttpResponse
# from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.template.loader import get_template
# from anymail.signals import tracking
# from django.dispatch import receiver
from django.http import FileResponse




# Create your views here.
def log_in(request):
    
    
    return render (request,'login/login.html')

@login_required
def home(request):

   
    
    return render (request,'login/home.html')



def about(request):
    return render (request,'login/about.html')

def contact(request):
    if request.method=="POST":
        print("this is post")
        name=request.POST['name']
        email= request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']

        print(name,email,phone,message)
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
        print(contact)
        
        # send_mail(
        # 'NEW CONTACT',
        # message,
        # 'pleasedonotreply07@gmail.com',
        # ['ewareportal@gmail.com'],
        # fail_silently=False,
        # )

    return render (request,'login/contact.html')

def form(request):
    
    # print(Select_Template)
    if request.method=="POST" :

        print("this is post")
        # c_form=MyFileUploadForm(request.POST, request.FILES)
        # if c_form.is_valid():
        #     my_file=c_form.cleaned_data['files']
        #     Form(myfile=my_file).save()
            
        name=request.POST['name']
        Select_Template_Category=request.POST.get('Select_Template_Category')
        select_country=request.POST.get('select_country')
        mail= request.POST['mail']
        sname=request.POST['sname']
        subject=request.POST['subject']
        # date=request.POST['date']
        myfile=request.FILES.get('myfile')
        count=request.POST['count']
        interval=request.POST['interval']
        ttype=request.POST['ttype']
        
        print(name,mail,sname,subject,count,interval,ttype)
        
        form1 = Phishing(name=name,Select_Template_Category=Select_Template_Category,select_country=select_country,mail=mail, sname=sname, subject=subject,myfile=myfile,count=count,interval=interval,ttype=ttype)
        # form=Form.objects.create(myfile=myfile)
        form1.save()
        print(form1)
        # Select_Template=Select_Template_Category.replace("%5C","\\")
        # Select_Template1=Select_Template[1:]

        # Select_Template_Category= Form.objects.select_related("select_Template_Category")
        login11='login\\'
        html11=".html"
        Select_Template1=login11+Select_Template_Category[1:]+html11

        # f = Phishing.objects.all().get(id=0).myfile
        # myfile.open()
        


        
        # lines = myfile.readlines()
    
        # content =lines
        # # content.split(',')

        # # mail_list=content.split(',')
        # print(content)


        # recipient_list = content
        # chaiye="media\emails.txt"
        # myfile="email.txt"  #myfile
        # x="media\\"
        # z=x+myfile
        # print(z)
        try:
            recipients_list= []
            for line in myfile.open('rb').readlines():
                recipients_list.append(line.strip())
            print(recipients_list)

            recipients = b','.join(recipients_list)


            subject = subject
            html_message = render_to_string(Select_Template1,{'context': 'values'})
            plain_message = strip_tags(html_message)
            from_email = 'pleasedonotreply07@gmail.com'
            # to = recipients
            print(html_message)

            send_mail(subject, plain_message, 'Do not Reply', recipients_list, html_message=html_message)
            messages.success(request, " Mail has been sent successfully")
        except:
            subject = subject
            html_message = render_to_string(Select_Template1,{'context': 'values'})
            plain_message = strip_tags(html_message)
            # from_email = 'ewareportal@gmail.com'
            to = mail
            print(html_message)

            send_mail(subject, plain_message, 'Do not Reply', [to], html_message=html_message)
            messages.success(request, " Mail has been sent successfully")

    # if event.event_type == 'clicked':
        # print("Recipient %s clicked url %s" % (
        #       event.recipient, event.click_url))

        # return render(request, 'subscribe/success.html', {'recepient': recepient})
    context={'form':MyFileUploadForm()}
    return render (request,'login/form.html',context)
    





def profile(request,*args, **kwargs):
    # data=Profile.objects.all()
    ids = request.user.id
    profile = User.objects.get(pk=ids)

    if request.method=="POST":
        # data=Profile.objects.filter(user__id=request.user.id)
        # data=Profile.objects.all()
        print("this is post")
        fullName=request.POST['fullName']
        eMail= request.POST['eMail']
        phone=request.POST['phone']
        Street=request.POST['Street']
        gender=request.POST['gender']
        ciTy=request.POST['ciTy']
        sTate=request.POST['sTate']

        
        zIp=request.POST['zIp']
        site=request.POST['site']
        FaceBook=request.POST['FaceBook']
        Organization_Name=request.POST['Organization_Name']
        Job_Title=request.POST['Job_Title']
        # added_on=request.POST['added_on']
        

        print(fullName,eMail,phone,Street,ciTy,sTate,zIp,site,FaceBook,Organization_Name,Job_Title)
        profile = Profile(fullName=fullName, eMail=eMail, phone=phone, Street=Street,gender=gender,ciTy=ciTy,sTate=sTate,zIp=zIp,site=site,FaceBook=FaceBook,Organization_Name=Organization_Name,Job_Title=Job_Title)
        profile.save()
        print(profile)
    



    return render (request,'login/profile.html',{'profile':profile})

def aboutHome(request):
    return render (request,'login/home.html')


def reports(request):
    # data=Phishing.objects.get(pk = request.user.pk)
    # status_filter = data.filter(user=request.user)
    context={}
    # ch=Phishing.objects.filter(user__id=request.user.id)
    # if len(ch)>0:
    #     data=Phishing.objects.get(user__id=request.user.id)
    #     context["data"]=data
    all=Phishing.objects.all()
    
    # ids = request.user.id
    # all = User.objects.get(pk=ids)

    
    context["campaigns"]=all
    return render (request,'login/reports.html',context)



def handleSignUp(request):
    if request.method=="POST":

        # Get the post parameters
        username=request.POST['name']
        datemax= request.POST['datemax']
        email= request.POST['email']
        psw1=request.POST['psw1']
        psw2=request.POST['psw2']

        # check for errorneous input
        # if psw1!=psw2:
        #     messages.error(request, "passwords must be same")
        #     return redirect('/')
        if User.objects.filter(username=username).exists():
            messages.warning(request,"username already exist")
            return redirect("/")
            
        
        # Create the user
        else:
        
            myuser = User.objects.create_superuser(username, email, psw1)
            # myuser.first_name= name
            myuser.date=datemax
            myuser.set_password(psw2)
            # myuser.last_name= lname
            myuser.save()
            date_of_birth=Date_user(user=myuser,dob=datemax)
            date_of_birth.save()
            print(date_of_birth)
            messages.success(request, " Your EWARE account has been created successfully")
            
            return redirect('/')

    else:
        return HttpResponse("404 - Not found")


#login

def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username= username,password=password)
        if user is not None:
            auth.login(request, user)
            # messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.warning(request, "Invalid credentials! Please try again")
            return redirect("/")

    return HttpResponse("404- Not found")

#logout
def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")

    return redirect("/")
    # messages.success(request, "Successfully Logged Out")





# @xframe_options_exempt
# def amazon(request):
#     # if request.method=='POST':

#     return render(request,"login/amazon.html")

@xframe_options_exempt
def gmail(request):
    
    #     recipients_list= []
    #     for line in myfile.open('rb').readlines():
    #         recipients_list.append(line.strip())
    #     print(recipients_list)

    #     recipients = b','.join(recipients_list)
    #     subject = subject
    #     html_message = render_to_string('login\gmail.html',{'context': 'values'})
    #     plain_message = strip_tags(html_message)
    #     from_email = 'pleasedonotreply07@gmail.com'
    #     # to = recipients
    #     print(html_message)

    #     send_mail(subject, plain_message, 'Do not Reply', recipients_list, html_message=html_message)
    #     messages.success(request, " Mail has been sent successfully")
    # send_mail(
    #     'Subject',
    #     'Email message',
    #     'pleasedonotreply07@gmail.com',
    #     ['deepshikha2700@gmail.com'],
    #     fail_silently=False,
    # )

    # #return HttpResponse('Mail successfully sent')
        # if request.method=='GET':
    #     send_mail(
    #         'Subject',
    #         'Email message',
    #         'pleasedonotreply07@gmail.com',
    #         ['deepshikha2700@gmail.com'],
    #         fail_silently=False,
    #     )

    #     return HttpResponse('Mail successfully sent')
    # login11='mail_template.html'
    
    # # Select_Template1=login11+Select_Template_Category[1:]+html11

    # return redirect(request,login11)

    return render(request,"login/gmail.html")

@xframe_options_exempt
def amazon(request):
    # if request.method=='POST':

    return render(request,"login/amazon.html")

@xframe_options_exempt
def socialpassword(request):
    # if request.method=='POST':

    return render(request,"login/socialpassword.html")

@xframe_options_exempt
def health(request):
    # if request.method=='POST':

    return render(request,"login/health.html")

@xframe_options_exempt
def office_mailer(request):
    # if request.method=='POST':

    return render(request,"login/office_mailer.html")

@xframe_options_exempt
def D_D(request):
    # if request.method=='POST':

    return render(request,"login/D_D.html")

@xframe_options_exempt
def account_recovery(request):
    # if request.method=='POST':

    return render(request,"login/account_recovery.html")

@xframe_options_exempt
def company_ann(request):
    # if request.method=='POST':

    return render(request,"login/company_ann.html")

@xframe_options_exempt
def covid(request):
    # if request.method=='POST':

    return render(request,"login\covid.html")

@xframe_options_exempt
def consumer_shopping(request):
    # if request.method=='POST':

    return render(request,"login/consumer_shopping.html")


def mail_template(request):
    
    send_mail(
        'Subject',
        'Email message',
        'pleasedonotreply07@gmail.com',
        ['deepshikha2700@gmail.com'],
        fail_silently=False,
    )
    # img = open('https://www.corsicatech.com/wp-content/uploads/2019/11/phishing_endpage_fail.png', 'rb')

    # response = FileResponse(img)

    # return response

    # #return HttpResponse(mimetype="https://www.corsicatech.com/wp-content/uploads/2019/11/phishing_endpage_fail.png")
    return redirect("https://www.corsicatech.com/wp-content/uploads/2019/11/phishing_endpage_fail.png")

def analyze(request):
    # if request.method=='POST':

    return render(request,"login/analyze.html")

def index(request):
    # if request.method=='POST':

    return render(request,"login/index.html")

def send_email(request):
    send_mail(
        'Subject',
        'Email message',
        'pleasedonotreply07@gmail.com',
        ['deepshikha2700@gmail.com'],
        fail_silently=False,
    )

    return HttpResponse('Mail successfully sent')


#email


# '''
# subject = 'welcome to GFG world'
# message = 'Hi, thank you for registering in geeksforgeeks.'
# email_from = settings.EMAIL_HOST_USER
# recipient_list = ['gulati.khushi.1999@gmail.com' ]
# send_mail( subject, message, email_from, recipient_list )
# '''
# # template=get_template('mail_template.html')
# subject = 'That’s your subject'
# html_message = render_to_string('login\gmail.html',{'context': 'values'})
# plain_message = strip_tags(html_message)
# from_email = 'ewareportal@gmail.com'
# to = 'dddhiman2000@gmail.com'

# mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)


# def analyze(request):
#     client_address = request.META['HTTP_X_FORWARDED_FOR']
#     djtext = request.GET.get('client_address', 'default')


# recipients_list= []
# for line in open('emails.txt','r').readlines():
#     recipients_list.append(line.strip())
# print(recipients_list)

# recipients =  ', '.join(recipients_list)
# fromaddr = 'khushigulati71@gmail.com'
# toaddrs  = recipients


# username = 'covidcase'
# password = 'JATINSETIA25'
# server = smtplib.SMTP('smtp.gmail.com:587')
# server.starttls()
# server.login(username,password)
# server.sendmail(fromaddr,recipients_list , msg.as_string())
# print("message has been sent")
# server.quit()