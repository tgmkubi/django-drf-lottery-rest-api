from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from random import randint
import boto3

def sendSMS(phone_number, message):
    client = boto3.client('sns')
    response = client.publish(
    PhoneNumber=phone_number,
    Message=message,
    )
    print(response)

# Create your models here.
class Lottery(models.Model):
    lottery_name = models.CharField(max_length=30, blank=False, null=False)
    select_winner = models.BooleanField(default=False)
    winner = models.CharField(max_length=50, blank=True, null=True)
    #winner = models.OneToOneField(Competitor, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.lottery_name

@receiver(pre_save, sender=Lottery)
def pre_save_handler(sender, instance, **kwargs):
    if(instance.select_winner):
        lottery_id = instance.id
        lottery = Lottery.objects.get(pk=lottery_id)
        competitors = lottery.competitors_of_lotteries.filter(is_active=True) # Competitors modelindeki lottery field için related_name => competitors_of_lotteries
        numberOfCompetitors = competitors.count()
        random_winner = randint(0, numberOfCompetitors - 1)
        winner = competitors[random_winner].email
        instance.winner = str(winner)

        print(instance.winner)
        #print(str(competitors[random_winner].phone_number))
        #print(instance.lottery_name)

        
        #sendSMS(str(competitors[random_winner].phone_number), f"Tebrikler {str(instance.lottery_name)} çekilişini kazandınız!")
    else:
        print("Kazananı seçmek istemediniz.")

