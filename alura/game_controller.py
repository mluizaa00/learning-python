import json;

difficulties = list();

def load_settings():
    with open("/resources/settings.json") as file:
        settings_file = file;
        settings_data = json.loads(settings_file.read());
        
        for key, value in settings_data["difficulties"]:
            difficulties.append(value);
            

def finish_game(current_points):
    print("The game was finished!");
    print("Final points: {}".format(current_points))
