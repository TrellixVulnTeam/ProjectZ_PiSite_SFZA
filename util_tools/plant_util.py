from Home import models


def get_profile():
    try:
        model = models.PlantProfile.objects.get()
        return model
    except Exception as err:
        print(err)

    return None


def change_profile(request):
    try:
        model = models.PlantProfile.objects.get()

    except Exception as err:
        print(err)
        model = models.PlantProfile.objects.create()

    model.plant_name = request.POST["plant_name"]
    model.avg_heat = request.POST["avg_heat"]
    model.avg_light = request.POST["avg_light"]
    model.moist = request.POST["moist"]
    model.location = request.POST["location"]
    model.time_to_water = request.POST["time_to_water"]
    model.priority = request.POST["priority"]

    model.save()
