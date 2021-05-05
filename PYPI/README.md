# Firebase-CRUD
  Home Automation using my firebase package and kivy Android App, finally display output on my website >> https://imvickykumar999.herokuapp.com/

## Create new file in cmd
  echo print('hello') > main.py


![image](https://user-images.githubusercontent.com/50515418/116424009-cd519480-a85e-11eb-943f-e566d49bad09.png)

## CMD...

    - C:\Users\Vicky\Desktop\home-automation>python
    - Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 16:30:00) [MSC v.1900 64 bit (AMD64)] on win32
    - Type "help", "copyright", "credits" or "license" for more information.

    >>> from multivicks.crud import HomeAutomation as h
    >>> link = 'https://led-blink-wifi-default-rtdb.firebaseio.com/'
    >>> o = h(link)

    >>> p = o.pull()
    >>> p
    1

    >>> u = o.push()
    >>> u
    "{'A': {'B': {'C': {'Name': 'LED', 'Switch': 1}}}, 'led1': 0, 'led2': 0}, ...is present"

    >>> o.remove('led2')
    "{'A': {'B': {'C': {'Name': 'LED', 'Switch': 1}}}, 'led1': 0}, ...is present"

    >>> o.push(0)
    "{'A': {'B': {'C': {'Name': 'LED', 'Switch': 0}}}, 'led1': 0}, ...is present"

    >>> o.push()
    "{'A': {'B': {'C': {'Name': 'LED', 'Switch': 1}}}, 'led1': 0}, ...is present"
    >>> o.pull()
    1

    >>> o.pull('A/B')
    {'C': {'Name': 'LED', 'Switch': 1}}

    >>> o.pull('A/B/C')
    {'Name': 'LED', 'Switch': 1}

    >>> o.pull('A/B/C/Switch')
    1

    >>> o.push(1, 'led2')
    "{'A': {'B': {'C': {'Name': 'LED', 'Switch': 1}}}, 'led1': 0, 'led2': 1}, ...is present"
    >>>
