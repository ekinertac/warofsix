from django.dispatch import Signal
from datetime import timedelta
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import UserTroops, Race, Troops, Buildings, UserBuildings, Resources, Location, UserTracker, Settlement, Statistic, UserTroopTraining, TroopUpgrades, Profile
from encampment.models import DepartingCampaigns, DepartingTroops, ArrivingCampaigns, ArrivingTroops, DefencePosition
from battle.models import Battles, AttackerDeads, DefenderDeads
from .views import positive_or_zero
from django.utils import timezone
# import csv
import random, math
from math import floor
from django.db.models import F, Q
from django.contrib.auth.models import User




profile_description_samples = {
    "Men": [
    "ALL WE HAVE TO DECIDE IS WHAT TO DO WITH THE TIME THAT IS GIVEN TO US.",
    "You shall not pass!",
    "Fly, you fools!",
    "Forth.. And fear no darkness!",




    ],

    "Elves":[
    "You have been called here to answer the threat of Mordor. Middle-earth stands upon the brink of destruction; none can escape it. You will unite or you will fall.",
    
    ],

    "Dwarves":[
    "You'll find more cheer in a graveyard.",
    "Loyalty, Honor, A Willing Heart; I Can Ask No More Than That",
    "I have a wee proposition, if you don't mind giving me a few moments of your time. Would you consider... JUST SODDING OFF!",
    "I will not stand down before any elf! Not least this faithless Woodland sprite!",
    "We're on! Let's give these b*st*rds a good hammering!"


    
    ],

    "Isengard":[
    "We are the servants of Saruman the Wise, the White Hand: the Hand that gives us man's-flesh to eat.",
    "The age of Men is over. The time of the Orc has come.",
    "The old world will burn in the fires of industry. The forests will fall. A new order will rise.",
    "the wolf that one hears is worse than the orc that one fears.",



    ],

    "Mordor": [
    "You cannot hide. I see you. There is no life in the void. Only death.",
    "Ash nazg durbatulûk, ash nazg gimbatul, ash nazg thrakatulûk agh burzum-ishi krimpatul.",
    "The age of men is over. The time of the orc has come.",
    "Slay them all",
    "Fear.. The city is rank with it! Let us ease their suffering.",
    "Grond... Grond... Grond...",
    ""

    
    ],

    "Goblins":[
    "Oh, but I'm forgetting, you don't have a mountain, and you're not a king, which makes you nobody, really.",
    "Bones will be shattered, necks will be wrung!",
    "Abominations, disfigurations, mutilations, and repulsions... That's all you're going to find down here.",
    
    ]
}


@receiver(post_save, sender=Race)
def create_instances(sender, instance, created, **kwargs):
    if created:
        if instance.name == "Wild" or instance.name == "Wild2":
            pass
        else:     
            race = instance.name
            troops = Troops.objects.filter(race=race)
            user = instance.user

            #Asing a location with random
            locs = Location.objects.filter(user=None, type="settlement")
            loc = random.choice(locs)
            loc.user = user
            loc.save()

            for troop in troops:
                UserTroops.objects.create(user=user, troop = troop)
            new = UserTroops.objects.filter(user=user)
            new = new.get(troop__name = 'Builder')
            new.count = 5
            new.save()

            race = Race.objects.get(user=user)
            race.is_selected = True
            race.save()


@receiver(post_save, sender=DepartingCampaigns)
def create_battle_task(sender, instance, created, **kwargs):
    if created:
        print(instance)
        print("signal emcampment")
        # print(instance.speed)



@receiver(post_save, sender=Race)
def create_buildings(sender, instance, created, **kwargs):
    if created:
        if instance.name == "Wild" or instance.name == "Wild2":
            pass
        else:
            race = instance.name
            user = instance.user

            #Create Fortress by default with level 1
            fortress_first = Buildings.objects.get(race=race, name="Fortress")
            user_fortress = UserBuildings.objects.create(user=user, building=fortress_first, level=1)
            user_fortress.save()

            troop_builder = Troops.objects.get(name="Builder", building= user_fortress.building)
            UserTroopTraining.objects.create(user=instance.user, user_building= user_fortress, troop=troop_builder)

            #Create Resources for user on DB
            Resources.objects.create(user=user)


            # Create Statistic for user
            user_statistic = Statistic.objects.create(user=user)


            #Create the settlement with all 20 spots and assign Fortress to number 10
            for number in range(1,21):
                Settlement.objects.create(user=user, settlement_id = number)
                
            fortress = Settlement.objects.get(user=user, settlement_id=10)
            fortress.building = UserBuildings.objects.get(user=user, building__name = "Fortress")
            fortress.save()

            # create a profile
            Profile.objects.create(
                user=user,
                race = instance,
                location = Location.objects.get(user=user),
                statistic = user_statistic,
                description = random.choice(profile_description_samples[instance.name])
            )
                
            # Troop Upgrades
            TroopUpgrades.objects.create(user=user)

            # Create a tracker
            UserTracker.objects.create(user=user)

            # Create a Defensive Position
            positions_list = [11, 12, 13, 14, 21, 22, 23, 24, 31, 32, 33, 34]
            default_builder = UserTroops.objects.get(user=user, troop__name="Builder")
            for pos in positions_list:
                if pos == 11:
                    DefencePosition.objects.create(user=user, position=pos, user_troop=default_builder, percent=100)
                else:
                    DefencePosition.objects.create(user=user, position=pos, user_troop=default_builder)



# İLERİDE SERVER'DA BU SİGNAL'İN BELİRLİ ARALIKLARLA ÇALIŞMASI GEREKİYOR

@receiver(post_save, sender=UserTracker)
def catch_request(sender, instance, **kwargs):
    user = instance.user
    training_check(user)

    buildings = UserBuildings.objects.filter(user=user)
    building_update_check(buildings)
    resource_production(user)
    current_resources(user)
    armory_update_check(user)
    # create_wild_good_easy()







campaign_created_signal = Signal()


def campaign_created(sender, instance, **kwargs):
    print("Departing Campaign signals")
    print(instance)
    print(f"Hız: {instance.speed}")
    print(f"Varış Zamanı: {instance.arriving_time}")


campaign_created_signal.connect(campaign_created)


# Hızları ayarlamak için lazım olduğunda kullandım.
def speed_dec():
    troops = Troops.objects.all()
    for troop in troops:
        troop.speed = round(troop.speed / 3)
        print(f"{troop} yeni hızı {troop.speed} oldu.")
        troop.save()

# tracker'da sorun yaşıyor
def create_wild_good_easy():
    number = random.choice(range(99999))
    user = User.objects.create(username=f"wild1{number}", password="Galadriel123", is_staff=False, is_active=True, is_superuser=False)
    race = Race.objects.create(user=user, name="Wild", is_selected=True)

    loc = random.choice(Location.objects.filter(type="wild"))
    loc.user = user
    loc.location_name = "Wildling Camp"
    loc.save()

    buildings = Buildings.objects.filter(race="Wild")
    for building in buildings:
        UserBuildings.objects.create(user=user, building=building, level=5, resource_worker=5)
    troops = Troops.objects.filter(race="Wild")
    troops = random.choices(troops, k=2)
    for troop in troops:
        UserTroops.objects.create(user=user, troop=troop, count=random.randint(13,30))
    
    resource = Resources.objects.create(user=user, wood=random.randint(12000,19000), stone=random.randint(12000,19000), iron=random.randint(12000,19000), grain=random.randint(12000,22000))

    stat = Statistic.objects.create(user=user)

    profile = Profile.objects.create(user=user, race=race, location=loc, statistic=stat)
    tracker = UserTracker.objects.create(user=user)


def resource_production(user):
    base = 50
    try:
        wood_production = 50
        woods = UserBuildings.objects.filter(user=user, building__type = "wood")
        for wood in woods:
            wood_production += wood.level * 1.25 * wood.resource_worker * base if wood.resource_worker != 0 else wood.level * 1.25 * base
    except:
        wood = base

    try:
        stone_production = 50
        stones = UserBuildings.objects.filter(user=user, building__type = "stone")
        for stone in stones:
            stone_production += stone.level * 1.25 * stone.resource_worker * base if stone.resource_worker != 0 else stone.level * 1.25 * base
    except:
        stone = base
    
    try:
        iron_production = 50
        irons = UserBuildings.objects.filter(user=user, building__type = "iron")
        for iron in irons:
            iron_production += iron.level * 1.25 * iron.resource_worker * base if iron.resource_worker != 0 else iron.level * 1.25 * base
    except:
        iron = base
    
    try:
        grain_production = 50    
        grains = UserBuildings.objects.filter(user=user, building__type = "grain")
        for grain in grains:
            grain_production += grain.level * 1.25 * grain.resource_worker * base if grain.resource_worker != 0 else grain.level * 1.25 * base
    except:
        grain= base
        
    # Troops' grain consuption calcutaions
    user_troops = UserTroops.objects.filter(user=user)
    consuption = 0
    for user_troop in user_troops:
        consuption += user_troop.troop.consuption * user_troop.count
    
    grain_production -= consuption

    production = {
        "wood": round(wood_production),
        "stone": round(stone_production),
        "iron": round(iron_production),
        "grain": round(grain_production)
    }
    return production

def current_resources(user):
    resource_prod = resource_production(user)
    resources = Resources.objects.get(user=user)
    #time difference between two visit by minute
    time_difference = floor((timezone.now() - resources.last_checkout).total_seconds() / 60)
    if time_difference < 1:
        resources = resources
    else:
        resources.wood += round(resource_prod["wood"] / 60 * time_difference)
        resources.stone += round(resource_prod["stone"] / 60 * time_difference)
        resources.iron += round(resource_prod["iron"] / 60 * time_difference)
        resources.grain += round(resource_prod["grain"] / 60 * time_difference)

        if resources.grain < 0:
            resources.grain = 0
        
        resources.last_checkout = resources.last_checkout + timedelta(minutes=time_difference)
        resources.save()

    return resources

def troop_training_check(troops, user):
    for troop in troops:
        if troop.training == 0:
            pass
        else:
            building = UserBuildings.objects.get(user=user, building = troop.troop.building)
            time_diff = (timezone.now() - troop.last_checkout).total_seconds()
            training_time = round(troop.troop.training_time / building.level)
            troop.time_passed += round(time_diff)
            trained = math.floor(troop.time_passed / training_time)
            if trained > troop.training:
                trained = troop.training
                troop.time_passed = 0
            
            troop.training -= trained
            troop.count += trained
            troop.time_passed -= trained * training_time
            if troop.time_passed < 0:
                troop.time_passed = 0
            troop.last_checkout = timezone.now()

            troop.time_left_total = timezone.now() + timezone.timedelta(seconds = troop.training * training_time - troop.time_passed)
            troop.time_left_per_troop = training_time - troop.time_passed
 

            troop.save()
    return troops


def training_check(user):
    trainings = UserTroopTraining.objects.filter(user=user)
    for troop in trainings:
        if troop.training == 0:
            troop.time_passed = 0
            troop.save()
        else:
            time_diff = (timezone.now() - troop.last_checkout).total_seconds()
            training_time = round(troop.troop.training_time / troop.user_building.level)
            troop.time_passed += round(time_diff)
            trained = math.floor(troop.time_passed / training_time)
            if trained >= troop.training:
                trained = troop.training
                troop.time_passed = 0
            else:
                troop.time_passed -= trained * training_time
            
            troop.training -= trained
            user_troop = UserTroops.objects.get(user=user, troop=troop.troop)
            user_troop.count += trained
            user_troop.save()

            troop.last_checkout = timezone.now()
            troop.time_left_total = timezone.now() + timezone.timedelta(seconds= troop.training * training_time - troop.time_passed)
            troop.time_left_per_troop = training_time - troop.time_passed

            troop.save()
    return trainings


def building_update_check(buildings):
    for building in buildings:
        if building.time_left != 0:
            building.time_left = positive_or_zero(building.time_left - round((timezone.now() - building.last_checkout).total_seconds()))
            building.last_checkout = timezone.now()
            if building.time_left == 0:
                building.level +=1
                if building.level == 1:
                    building_troops = Troops.objects.filter(building = building.building)
                    for troop in building_troops:
                        UserTroopTraining.objects.create(user=building.user, user_building=building, troop=troop)
                if building.building.type == "armory":
                    user_troops = UserTroops.objects.filter(user=building.user)
                    user_troops.update(defence_level=F('defence_level')+0.01)
                    user_troops.update(attack_level=F('attack_level')+0.01)
                builder = UserTroops.objects.get(user=building.user, troop__name="Builder")
                builder.count += building.worker
                building.worker = 0
                builder.save()

            building.save()


def armory_update_check(user):
    upgrades = TroopUpgrades.objects.get(user=user)
    if upgrades.time_left == 0:
        pass
    else:
        time_diff = (timezone.now()- upgrades.last_checkout).total_seconds()
        new_time_left = upgrades.time_left - time_diff
        
        if positive_or_zero(new_time_left) == 0:
            field = upgrades.upgrading_field
            print("***************************")
            print(field)
            current_value = getattr(upgrades, field)
            current_value += 1
            setattr(upgrades, field, current_value)
 
            upgrades.last_checkout = timezone.now()
            upgrades.time_left = 0
            upgrades.save()

            # UPGRADE the USER TROOPS'
            if field == "heavy_armor":
                user_troops = UserTroops.objects.filter(user=user).exclude(Q(troop__type = "siege"))
                user_troops.update(defence_level=F('defence_level') + 0.01)
            elif field == "forge_blade":
                user_troops = UserTroops.objects.filter(user=user, troop__type = "infantry")
                user_troops.update(attack_level=F('attack_level') + 0.01)
            elif field == "arrow":
                user_troops = UserTroops.objects.filter(user=user, troop__type= "archer")
                user_troops.update(attack_level=F('attack_level') + 0.01)
            else:
                pass

        else:
            upgrades.time_left = new_time_left
            upgrades.last_checkout = timezone.now()
            upgrades.save()
    return True







# THESE LINES ARE USED TO ENTER LOCATIONS TO DB
# NOT USE IT AGAIN IF Locations Table not deleted.

        # with open("bfme2.csv", "r", encoding="UTF-8") as file:
        #     file = csv.reader(file, delimiter="\t")
        #     y = 30
        #     for row in file:
        #         for x in range(30):
        #             if row[x] == "n":
        #                 Location.objects.create(locx=x+1, locy = y, type="nature")
        #             elif row[x] == "w":
        #                 Location.objects.create(locx=x+1, locy = y, type="wild")
        #             else:
        #                 Location.objects.create(locx=x+1, locy = y, type="settlement")
        #         y -= 1
        #         if y < 1:
        #             break

        

