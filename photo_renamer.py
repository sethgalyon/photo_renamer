import os
import exifread


def photo_renamer(photos_dir):
    try:
        entities = os.listdir(photos_dir)
    except FileNotFoundError:
        print('\nError: Directory not found')
        return

    dir_list = []
    for i, entity in enumerate(entities):
        if os.path.isdir(os.path.join(photos_dir, entity)):
            dir_list.append(entity)
            photo_renamer(os.path.join(photos_dir, entity))
        else:
            entities[i] = os.path.join(photos_dir, entity)
            
    for dir in dir_list:
        entities.remove(dir)

    files = []
    for file in entities:
        with open(file, 'rb') as image:
            exif = exifread.process_file(image, details=False, stop_tag='DateTimeOriginal')
        
        try:
            date = str(exif['EXIF DateTimeOriginal'])
        except KeyError:
            date = file.split('\\')
            if len(date[-2]) <= 2:
                date = f'{date[-3]}:{date[-2]}:00 00:00:00'
            else:
                date = f'{date[-2]}:00:00 00:00:00'
        
        date = ''.join(date.split(' ', 1)[0].split(':', 2) + date.split(' ', 1)[1].split(':', 2))

        files.append((date, file))
    
    files.sort()
    
    num_photos_per_day = {}
    for file in files:
        year = file[0][:4]
        month = file[0][4:6]
        day = file[0][6:8]
        date = year + month + day
        
        newName = photos_dir + '\\' + date + '_' + str(num_photos_per_day.get(date, 1)) + '.' + file[1].split('\\')[-1].split('.')[-1]
        oldName = photos_dir + '\\' + file[1].split('\\')[-1]

        os.rename(oldName, newName)
        
        num_photos_per_day[date] = num_photos_per_day.get(date, 1) + 1
        
    print(f'Folder, {photos_dir}, done!')


if __name__ == '__main__':
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    photos_dir = str(input('\nPlease enter the directory of your photos: '))
    photos_dir = os.path.join(script_dir, photos_dir)
    
    photo_renamer(photos_dir)
