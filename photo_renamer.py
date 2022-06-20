import os
import time


def photo_renamer(photos_dir):
    entities = os.listdir(photos_dir)
    dir_list = []
    for i, entity in enumerate(entities):
        if os.path.isdir(os.path.join(photos_dir, entity)):
            dir_list.append(entity)
            photo_renamer(os.path.join(photos_dir, entity))
        else:
            entities[i] = os.path.join(photos_dir, entity)
            
    for dir in dir_list:
        entities.remove(dir)

    entities.sort(key=os.path.getctime)
    
    num_photos_per_day = {}
    for file in entities:
        t = time.gmtime(os.path.getctime(file))
        
        year = str(t.tm_year)
        
        month = str(t.tm_mon)
        if len(month) < 2:
            month = '0' + month
            
        day = str(t.tm_mday)
        if len(day) < 2:
            day = '0' + day
        
        date = year + month + day
        
        newName = photos_dir + "\\" + date + "_" + str(num_photos_per_day.get(date, 1)) + ".jpg"
        oldName = photos_dir + "\\" + file.split("\\")[-1]

        os.rename(oldName, newName)
        num_photos_per_day[date] = num_photos_per_day.get(date, 1) + 1
        
    print(f"Folder, {photos_dir}, done!")


if __name__ == '__main__':
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    photos_dir = str(input("Please enter the directory of your photos: "))
    photos_dir = os.path.join(script_dir, photos_dir)
    
    photo_renamer(photos_dir)