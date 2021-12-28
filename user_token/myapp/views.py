from django.shortcuts import render, HttpResponse
from django.template.loader import get_template
from rest_framework.authtoken.models import Token
import random
import string
from django.contrib.auth.models import User
from .models import UserProfile
from django.core.paginator import Paginator
import csv
import pdfkit as pdf
from xhtml2pdf import pisa
from .utils import render_to_pdf


# Create your views here.
def home():
    # For random username generation :-------------
    username = ''.join(random.choices(
        string.ascii_letters + string.digits, k=10))
    print(username)

    # For Auto Password Generation :----------
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    all = lower + upper + num + symbols
    temp = random.sample(all, 12)
    password = "".join(temp)
    print(password)
    print('--------------')

    # User.objects.create_user(username,password) This creates new user
    user = User.objects.create_user(username, password)
    user.save()

    # Save the values in UserProfile model:-----------------
    range_start = 10**(10-1)
    range_end = (10**10)-1
    mobile = random.randint(range_start, range_end)
    choices = ['Admin', 'Uploader', 'Editor']
    permission = random.choice(choices)
    userprofile = UserProfile()
    userprofile.user = user
    userprofile.mobile = mobile
    userprofile.permission = permission  # This select only Uploader permission
    userprofile.save()

    # Here, Token Generations :-------------------------
    token_create = Token.objects.get_or_create(user=user)


def detail_dropdown(request):
    profile = UserProfile.objects.all()

    token = Token.objects.all().values_list('key')
    z1 = []
    z2 = []
    z3 = []
    z4 = []
    for i in profile:
        z1.append(i.user)
        z2.append(i.mobile)
        z3.append(i.permission)
        token = Token.objects.get(user=i.user)
        z4.append(token.key)
    data = zip(z1, z2, z3, z4)
    a = []
    for i in data:
        a.append(i)

    recs = request.GET.get('rec')
    print(recs)
    if recs != None and recs != "" :
        paginator = Paginator(a, int(recs))
    else:
        paginator = Paginator(a, 10) # By default,10 recorda per page
        recs = 10
    print(paginator.num_pages,'------number of pages----------')
    print(paginator.page_range,'------page range---------')
    page1 =paginator.page(1)
    print(page1,'--------page1---------')
    print(page1.object_list,'--------page1 object_list--------')
    page2 = paginator.page(2)
    print(page2.object_list,'---------page2 object_list--------')
    print(page2.has_next(),'----------page2 has_next----------')
    print(page2.has_previous(),'-----------page2 has_previous-------')
    print(page1.start_index,'----------page1 start index------')
    print(page1.end_index,'-------page1 end index------')


    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    
    return render(request, 'list.html', {'page_obj': page_obj, 'total': paginator.count,'pages':page_number,'recs':recs})


def export(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        if file_format == 'CSV':
            profile = UserProfile.objects.all()

            token = Token.objects.all().values_list('key')
            z1 = []
            z2 = []
            z3 = []
            z4 = []
            for i in profile:
                z1.append(i.user)
                z2.append(i.mobile)
                z3.append(i.permission)
                token = Token.objects.get(user=i.user)
                z4.append(token.key)
            data = zip(z1, z2, z3, z4)

            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'
            writer = csv.writer(response)
            writer.writerow(['Username', 'Mobile', 'Permission', 'Token'])

            for i in data:
                writer.writerow(i)

            return response
        else:
            template = get_template('list1.html')
            profile = UserProfile.objects.all()
         
            token = Token.objects.all().values_list('key')
            z1 = []
            z2 = []
            z3 = []
            z4 = []
            for i in profile:
                z1.append(i.user)
                z2.append(i.mobile)
                z3.append(i.permission)
                token = Token.objects.get(user=i.user)
                z4.append(token.key)
            data = zip(z1, z2, z3, z4)
            a = []
            for i in data:
                a.append(i)
            paginator = Paginator(a, 20)
            page_obj = paginator.get_page(2)
       
            context = {'page_obj': page_obj, 'total': len(a)}
            pdf = render_to_pdf('list1.html', context)
            return HttpResponse(pdf, content_type='application/pdf')
