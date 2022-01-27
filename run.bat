echo HUB
start /min cmd /c python modularize\hub\hub\manage.py runserver 8000
echo HUB
start /min cmd /c python modularize\crystallab\crystallab\manage.py runserver 8010
echo FUNGUSLAB
start /min cmd /c python modularize\funguslab\funguslab\manage.py runserver 8020
echo FERMENTATIONLAB 
start /min cmd /c python modularize\fermentationlab\fermentationlab\manage.py runserver 8030