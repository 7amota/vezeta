from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify

# Create your models here.
class Profile(models.Model):
    #contexts
    gender = [
        ('M' , 'male'),
        ('f' , 'female')
    ]
    doctor_Specialization = [
        ('جلدية' , 'جلدية'),
        ('أسنان' , 'أسنان'),
        ('نساء وتوليد' , 'نساء وتوليد'),
        ('نفسي' , 'نفسي'),
        ('اطفال حديثي الولادة' , 'اطفال حديثي الولادة'),
        ('مخ واعصاب' , 'مخ واعصاب'),
        ('عظام' , 'عظام'),
        ('انف واذن وحنجرة' , 'انف واذن وحنجرة'),
        ('قلب واوعية دموية' , 'قلب واوعية دموية'),
        ('اورام' , 'اورام'),
        ('باطنة' , 'باطنة'),
        ('تخسيس وتغذية' , 'تخسيس وتغذية'),
        ('جراحة اطفال' , 'جراحة اطفال'),
        ('جراحة اوعية دموية' , 'جراحة اوعية دموية'),
        ('جراحة اورام' , 'جراحة اورام'),
        ('جراحة تجميل' , 'جراحة تجميل'),
        ('جراحة سمنة ومناظير' , 'جراحة سمنة ومناظير'),
    ]


    ##vars
    user = models.OneToOneField(User , verbose_name=('user') , on_delete=models.PROTECT)
    name = models.CharField(("الاسم :"), max_length=80)
    gender = models.CharField(('النوع'), max_length=50 , choices=gender , blank = True , null = True)
    join_us = models.DateTimeField( auto_now_add=True)
    Specialization = models.CharField(('التخصص'),max_length=50 , choices=doctor_Specialization , blank = True , null = True)
    subtitle = models.CharField(("نبذة عنك :"), max_length=80 , blank = True , null = True) 
    address   = models.CharField((" المحافظة :"), max_length=80, blank = True , null = True)
    gmail   = models.CharField( max_length=300, blank = True , null = True)
    twitter   = models.CharField( max_length=300, blank = True , null = True)
    google = models.CharField( max_length=300, blank = True , null = True)
    facebook   = models.CharField( max_length=300, blank = True , null = True)
    who_i = models.TextField((" من انا :"))
    price = models.IntegerField(("سعر الكشف :") , blank = True , null = True)
    waiting_time  = models.IntegerField(("مدة الانتظار :") , blank = True , null = True)
    working_hours = models.IntegerField(("ساعات العمل:") , blank = True , null = True)
    number_phone = models.IntegerField(("رقم الهاتف:") , blank = True , null = True)
    image =  models.ImageField(("صورة"), upload_to='photos/%y/%m/%d' , blank = True , null = True )
    # like : www.facebook/7amota.9/profile
    slug = models.SlugField(blank= True , null = True)




    ###defs
    def save(self, *args, **kwargs):
       if not self.slug:
           self.slug = slugify(self.user)
       super(Profile, self).save(*args, **kwargs) # Call the real save() method


    def __str__(self):
        return '%s' %(self.user)    
        

        
    def create_profile(sender , **kwargs):
        if kwargs['created']:
            Profile.objects.create(user = kwargs['instance'])
    post_save.connect(create_profile , sender = User)

class NewPost(models.Model):
    title_plugin = models.CharField(("عنوان المقال"), max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(("صورة للمقال"), upload_to='cats/%y/%m/%d' , blank = True , null = True )
    plugin = models.TextField((""))