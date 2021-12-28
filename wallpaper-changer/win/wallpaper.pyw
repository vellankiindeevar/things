import ctypes
import click
import json

@click.command()
@click.argument('x')
def image(x):
    WALLPAPER_PATH="C:\\Users\\Admin\\Pictures\\anime\\{}".format(x)  
    ctypes.windll.user32.SystemParametersInfoW(20, 0, WALLPAPER_PATH, 3)

    # just opens the settings.json file 
    def write_json(data,filename="C:\\Users\\Admin\\AppData\\Local\\Packages\\Microsoft.WindowsTerminal_8wekyb3d8bbwe\\LocalState\\settings.json"):
        with open (filename, "w") as f:
            json.dump(data,f,indent=4)

    with open ("C:\\Users\\Admin\\AppData\\Local\\Packages\\Microsoft.WindowsTerminal_8wekyb3d8bbwe\\LocalState\\settings.json") as json_file:
        data = json.load(json_file)

    # saves the settings.json file
    write_json(data)
   

if __name__ == '__main__':
    image()
