# Certificate Maker
```
This folder contains a python3 script to make a certificate, given the names of people in excel format. It creates both pdf and png version of certificates.
```

# Requirements
1. OpenCV
        
```
pip install opencv-python
```

2. openpyxl

```
pip install openpyxl
```

3. pillow

```
pip install pillow
```

# How this script works
* Fork this repository and clone it in your local directory. Specify the template path, participants file path and output directory path in the appropriate places.

* Execute the certificate_maker.py file.
Make sure you have saved your certificate template as certificate_template.png and participants list as participants.xlsx in the same folder.
```
python certificate_maker.py
```

* New files with appropriate names will be created in the output directory specified.