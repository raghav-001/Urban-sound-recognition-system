from my_app.models import AudioFile
from django.shortcuts import render, redirect
from .forms import AudioForm
from .predictModel import figure_model, load_model, predict_model


def home(request):

    if request.method == "POST":
        # we use request.files only here since we passing a file
        form = AudioForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            global name
            # we are saving the name in a global var name to use it later, then saving it in db
            name = form.cleaned_data.get("name")
            print(name)
            form.save()
            return redirect("my_app:predict")
    else:
        form = AudioForm()
    context = {"form1": form}  # we pass this form1 to html file
    return render(request, 'my_app/home.html', context)


def predict(request):
    audio_db = AudioFile.objects.get(name=name).audio
    load_model()
    audio_path = audio_db.url  # gets the path from db
    audio_path = audio_path[1:]  # for removing the first / in the path
    audio_path_fig=audio_path[14:]
    label_name = predict_model(audio_path)
    figure_model(audio_path)
    context = {"label_name": label_name,
               "audio_path_fig": audio_path_fig}    # we add context to pass it to the predict.html
    return render(request, 'my_app/predict.html', context)

