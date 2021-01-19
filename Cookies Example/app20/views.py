from django.shortcuts import render

def showIndex(request):
    return render(request,"index.html")

def cookies_data(request):
    name = request.GET.get('name')
    price = request.GET.get('price')
    data = {"total_cookies":len(request.COOKIES)}
    response = render(request,"index.html",data)
    response.set_cookie(key=name,value=price)
    return response

def show_cookies(request):
    data = {'total_cookies':len(request.COOKIES),"cookies":request.COOKIES}
    return render(request,"cookies.html",data)

def delete_cookies(request):
    delete_key = request.GET.get('cn')
    request.COOKIES.pop(delete_key)
    return show_cookies(request)
