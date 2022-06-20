# photo_renamer
Windows command line tool to rename all photos in a directory and its sub-directories written in Python.

Renames all photos in directory and sub-directories to "YYYYMMDD_#" where # is the number of the picture in that day, sorted by time taken.

# dependancies
1: exifread module
This tool uses the exifread python module in order to read image exif data. Use pip to install,
```
pip install exifread
```
2: Folder structure
The folder structure must comprise of years, months, and then photos. There must be no other text in the year and month naming schemes. For example, the folder structure can be "C:\photos\2005\10\photo.jpg" but not "C:\photos\2005\10 Vacation\photo.jpg".

# to do
1: Update to handle text within the folder structure. For example, "C:\photos\2005\10 Vacation\photo.jpg".

2: Update to be able to choose directories outside of the script's working directory.
