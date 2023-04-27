from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
import os
import re
# Create your views here.
from .forms import Userform
from .models import Users

def index(request):
    return redirect('/admin/login')

def admin_index(request):
    adminuser=request.session.get('admin')
    if adminuser is None:

        return redirect('/admin/login')
        
 
    return render(request,'index.html')
    
def admin_login(request):
    
    
    if request.method=='POST':
        data=Users.objects.filter(username=request.POST['username'],password=request.POST['password']).first()
        if data is None:
            return redirect('/admin/login')
        else:
            if data.is_admin==True:
                request.session['admin']={
                    "id":data.id,
                    "username":data.username,
                    "password":data.password,
                    "img":str(data.img)
                }
                return redirect('/admin')
    
    return render(request,'login.html')

def admin_logout(request):
    adminuser=request.session.get('admin')
    if adminuser is None:

        return redirect('/admin/login')
        
    del request.session['admin']
    
    return redirect('/admin')

def admin_add_user(request):

    adminuser=request.session.get('admin')
    if adminuser is None:

        return redirect('/admin/login')
        

    user=Users.objects.all()
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
    
def admin_delete_user(request,id):

    adminuser=request.session.get('admin')
    if adminuser is None:

        return redirect('/admin/login')
        
    user=Users.objects.filter(id=id).first()
    import os
    path='admin_page/'+os.path.join('static','assets',str(user.img))
    if os.path.exists(path):
        os.remove(path)
    user.delete()
    return redirect('/admin/users')

def admin_update_user(request,id):

    adminuser=request.session.get('admin')
    if adminuser is None:

        return redirect('/admin/login')
        

    user=Users.objects.filter(id=id).first()
    url='admin/update/user/'+id
    regex = r'^\+994(50|51|70|77|55)\d{7}$'
    if request.method=='POST':
        form=Userform(request.POST,request.FILES,instance=user)
        
        s=os.path.join('admin_page/static/assets/',str(user.img))
        if form.is_valid():
               
                number=str(form.cleaned_data.get('number'))
                if re.match(regex,number):

                    if os.path.exists(s):
                        os.remove(s)
                    form.save()
                    return redirect('/admin/users')
                else:

                    error='Nömrə yanlışdır '
                    
                    
                
        else:
                error='Formda duzgun doldurun'
    return render(request,'updateuser.html',{"form":Userform(instance=user),'url':url})

def admin_profile(request):

    data=Users.objects.filter(id=request.session.get('admin')['id']).first()
    
    return render(request,'profile.html',{"data":data})

def admin_change_password(request,id):
    user=Users.objects.filter(id=id).first()
   
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