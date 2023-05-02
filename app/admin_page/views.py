from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

import os
import re
# Create your views here.
from .forms import Userform
from .models import Myuser,Categories,Products
from django.core.mail import send_mail

def index(request):

    return redirect('/admin/login')

@login_required
def admin_index(request):


    return render(request,'index.html')
    
def admin_login(request):
    
    
    if request.method=='POST':
       user=request.POST['username']
       passw=request.POST['password']
       data=authenticate(request,username=user,password=passw)
       if data is not None:
            login(request,data)
            return redirect('/admin')
       
    #    else:
    #         return HttpResponse(passw)
           
    
    return render(request,'login.html')

@login_required
def admin_logout(request):

    
        
    logout(request)
    
    return redirect('/admin')

@login_required
def admin_add_user(request):

    user=Myuser.objects.all()
    error=''
    regex = r'^\+994(50|51|70|77|55)\d{7}$'
    if request.method=='POST':
        
        form=Userform(request.POST,request.FILES)
        
        if form.is_valid():
            number=str(form.cleaned_data.get('number'))
            if re.match(regex,number):
                
                
                form.save()
                return redirect('/admin/users')
            else:

               error='Nömrə yanlışdır '
                 
                
            
        else:
            error='Formda duzgun doldurun'
        
    return render(request,'users.html',{"form":Userform,'users':user,'error':error})

@login_required
def admin_delete_user(request,id):


        
    user=Myuser.objects.filter(id=id).first()
    import os
    path=os.path.join('admin_page/static/assets/',str(user.img))
    if os.path.exists(path):
        if path=='admin_page/static/assets/':
                            pass
        else:
                        os.remove(path)
    user.delete()
    return redirect('/admin/users')

@login_required
def admin_update_user(request,id):



    user=Myuser.objects.filter(id=id).first()
    # return HttpResponse(str(user.img))
    url='admin/update/user/'+id
    regex = r'^\+994(50|51|70|77|55)\d{7}$'
    if request.method=='POST':
        form=Userform(request.POST,request.FILES,instance=user)
        
        s=os.path.join('admin_page/static/assets/',str(user.img))
        if form.is_valid():
               
                number=str(form.cleaned_data.get('number'))
                if re.match(regex,number):

                    if os.path.exists(s) :
                        # return HttpResponse(s)
                        if s=='admin_page/static/assets/':
                            pass
                        else:
                            os.remove(s)
                    pas=form.cleaned_data['password']
                    
                    form.save()
                    
                    return redirect('/admin/users')
                else:

                    error='Nömrə yanlışdır '
                    
                    
                
        else:
                error='Formda duzgun doldurun'
    return render(request,'updateuser.html',{"form":Userform(instance=user),'url':url})

@login_required
def admin_profile(request):

    data=Myuser.objects.filter(username=request.user).first()
    
   
    return render(request,'profile.html',{"data":data})

@login_required
def admin_change_password(request,id):
    user=Myuser.objects.filter(id=id).first()
   
    if request.method=='POST':

        oldpassword=request.POST['oldpass']
        new_password=request.POST['newpass']
        new_password_again=request.POST['newpass2']


        if oldpassword==user.password and new_password==new_password_again:
            user.password=new_password
            user.save()
            return redirect('/admin/profile')
        else:
            return redirect('/admin/profile/'+id+"/change/password")
    return render(request,'change.html',{'id':id})

# category routes ---------------------------------------------------

@login_required
def admin_categories(request):

    category=Categories.objects.all()
    
    if request.method=='POST':
        cate=request.POST['category']
        data=Categories(name=cate)
        data.save()
        return redirect('/admin/categories') 
    

        
    return render(request,'category/categories.html',{'category':category,'error':''})

@login_required
def admin_category_delete(request,id):

    category=Categories.objects.filter(id=id).first()
    
    category.delete()
    return redirect('/admin/categories')

@login_required
def admin_category_update(request,id):

    category=Categories.objects.filter(id=id).first()
    if request.method=='POST':
         
        category.name=request.POST['category']
        category.save()
        return redirect('/admin/categories')
    return render(request,'category/updatecategory.html',{"data":category})


# product routes-----------------------------
           
@login_required
def admin_products(request):
    products=Products.objects.all()
    category=Categories.objects.all()

    if request.method=='POST':
        title=request.POST['title']
        text=request.POST['text']
        cate=request.POST['category']

        data=Products(title=title,text=text,category=Categories.objects.filter(id=cate).first())
        data.save()
        return redirect('/admin/products')


    return render(request,'product/products.html',{"products":products,"category":category})
        
@login_required
def admin_product_delete(request,id):

    product=Products.objects.filter(id=id).first()
    
    product.delete()
    return redirect('/admin/products')

@login_required
def admin_product_update(request,id):
    category=Categories.objects.all()
    product=Products.objects.filter(id=id).first()
    if request.method=='POST':
         newcat=Categories.objects.filter(id=request.POST['category']).first()
         product.title=request.POST['title']
         product.text=request.POST['text']
         product.category=newcat
         product.save()
         return redirect('/admin/products')
    return render(request,'product/productupdate.html',{'data':product,"category":category})



        
    

def chat(request):
    import nltk
    from nltk.chat.util import Chat, reflections

    pairs = [
        
    [ 
        r"Salam|salam ",
        ["Salam Men söhbət botuyam sizə necə komək edə bilərəm"]
    ],
    [ 
        r"netersiz|necesen|netersen ",
        ["men bir botam menim hislerim yoxdu amma yenede sagoun sizə necə komək edə bilərəm"]
    ]
        
    ]
    chatbot=Chat(pairs,reflections)
    data=''
    if request.method=='POST':
         data=chatbot.respond(request.POST['chat'])
    return render(request,'chat.html',{"data":data})

