from django.urls import path
from . import views

urlpatterns = [
    path('',views.loginpage,name='Home'),
	path('signup1/',views.signuppage,name='sign up'),
	path('signup1/signupfn/',views.signupfn,name='sign up fn'),
	path('loginfn/',views.loginfn,name='login fn'),
	path('add questions/',views.addqstnpage,name='add qustions'),
	path('add questions/addfn/',views.addqstnfn,name='add qstn fn'),
	path('add questions/edit questions/',views.editpage,name='edit questions'),
	path('add questions/edit questions/search/',views.editsearch,name='search questions'),
	path('add questions/edit questions/editfn/',views.editfn,name='search questions'),
	path('add questions/view total/',views.viewtotal,name='view question set'),
	
	path('add questions/view total/view/',views.viewtotalfn,name='view question set'),
		
	path('view questionset/',views.viewqstnpage,name='view question set'),
	path('view questionset/view questions/',views.viewqstnpage1,name='view questions'),
	path('view questionset/view questions/check/',views.checkradio,name='check questions fn'),
	path('view questionset/view questions/viewfn/',views.viewfn,name='view questions fn'),
	path('view questionset/view questions/result/',views.resultpage,name='view questions fn'),
	path('view questionset/view questions/result/result/',views.checkresult,name='view questions fn'),
	path('view questionset/view questions/result/viewfn/',views.viewfn,name='view questions fn'),
	
	
	
	
]
