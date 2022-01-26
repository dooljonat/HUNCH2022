echo FERMENTATIONLAB 
start /min cmd /c python modularize\fermentationlab\fermentationlab\manage.py runserver 8000
start /min cmd /c python modularize\crystallab\crystallab\manage.py runserver 8010