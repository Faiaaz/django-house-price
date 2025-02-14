import pickle
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

# Load the trained model
with open("house_price_model.pkl", "rb") as file:
    model = pickle.load(file)


# Display the form for input
def index(request):
    return render(request, "predict_form.html")


# Handle form submission and predict the price
@csrf_exempt
@api_view(["POST"])
def predict_price(request):
    if request.method == "POST":
        # Get input values from the form
        area = float(request.POST.get("area"))
        bedrooms = int(request.POST.get("bedrooms"))

        # Predict the price
        prediction = model.predict([[area, bedrooms]])[0]

        return render(request, "predict_form.html", {"predicted_price": prediction, "area": area, "bedrooms": bedrooms})

    return HttpResponse("Invalid request", status=400)
