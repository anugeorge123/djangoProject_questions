from django.db import models

class Questions(models.Model):
	sid=models.IntegerField(default=0)
	question=models.CharField(max_length=1000,default="0")
	option1=models.CharField(max_length=1000,default="0")
	option2=models.CharField(max_length=1000,default="0")
	option3=models.CharField(max_length=1000,default="0")
	option4=models.CharField(max_length=1000,default="0")
	answer=models.CharField(max_length=1000,default="0")
				
	class Meta:
		db_table="questions"

class Sets(models.Model):
	sname=models.CharField(max_length=100,default="0")
	class Meta:
		db_table="sets"

