from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils import timezone

from lottery.models import Lottery
import boto3

def createNumber(phone_number):
    client = boto3.client('sns')
    response = client.create_sms_sandbox_phone_number(
        PhoneNumber=phone_number,
        LanguageCode='en-GB'
    )
    # 3rd party kullanırken response kontrol etmeliyiz
    print(response)

def verifyNumber(phone_number, onePassword):
    client = boto3.client('sns')
    response = client.verify_sms_sandbox_phone_number(
        PhoneNumber=phone_number,
        OneTimePassword=onePassword
    )
    print(response)


def send_verify_sms(phone_number):
    print(f"Competitor oluşturuldu ve {phone_number} numarasına sms iletildi.")

# Create your models here.
class Competitor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # LotterySerializer'da artık bu "competitors_of_lotteries" anahtar kelimesi ile Competitor Modeli bilgilerine erişebileceğiz.
    lottery = models.ForeignKey(Lottery, on_delete=models.CASCADE, related_name="competitors_of_lotteries")
    email = models.EmailField(unique=True, blank=False, null=False)
    phone_number = PhoneNumberField(unique=True, blank=False, null=False)
    created = models.DateTimeField(editable=False)
    is_active = models.BooleanField(default=False)

    def clean(self):
        super().clean()
        try:
            validate_email(self.email)
        except ValidationError:
            raise ValidationError({'email': 'Geçerli bir e-posta adresi girin.'})

    def __str__(self):
        return self.email

    """
    def save(self, *args, **kwargs):
        # id yoksa, bu model yeni oluşturuluyo demektir.
        if not self.id:
            self.created = timezone.now()
        # do something else
        # send_verify_sms(self.phone_number)
        return super(Competitor, self).save(*args, **kwargs)
    """


@receiver(pre_save, sender=Competitor)
def pre_save_handler(sender, instance, **kwargs):
    instance.created = timezone.now()

    if instance.is_active and instance.onePassword:
        verifyNumber(str(instance.phone_number), instance.onePassword)

    """
    if instance.is_active:
        createNumber(str(instance.phone_number))
    """


@receiver(post_save, sender=Competitor)
def post_save_handler(sender, instance, created, **kwargs):
    if created:
        print(f"{instance.first_name} Competitor Modeli oluşturuldu... Hoşgeldiniz...")

        print("Doğrulama SMS gönderiliyor")
        createNumber(str(instance.phone_number))


    else:
        print("Güncelleme işlemi başarılı....")
        # sms kodu doğruysa is_active = True işlemi yap. Güncellemede çalışsın
