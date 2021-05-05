# Program to Show how to attach a callback to switch

# import kivy module
import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require('1.9.0')

# The Switch widget is active or inactive
# The state transition of a switch is from
# either on to off or off to on.
from kivy.uix.switch import Switch

# The GridLayout arranges children in a matrix.
# It takes the available space and
# divides it into columns and rows,
# then adds widgets to the resulting “cells”.
from kivy.uix.gridlayout import GridLayout

# The Label widget is for rendering text.
from kivy.uix.label import Label

# A Gridlayout with a label a switch
# A class which contains all stuff about the switch

from multivicks.base import HomeAutomation
link = 'https://home-automation-336c0-default-rtdb.firebaseio.com/'
obj = HomeAutomation(link)

class SimpleSwitch(GridLayout):

    # Defining __init__ constructor
    def __init__(self, **kwargs):

        # super function can be used to gain access
        # to inherited methods from a parent or sibling class
        # that has been overwritten in a class object.
        super(SimpleSwitch, self).__init__(**kwargs)

        # no of coloumns
        self.cols = 2

        # Adding label to the Switch
        self.add_widget(Label(text ="Switch"))

        # Initially switch is Off i.e active = False
        self.settings_sample = Switch(active = False)

        # Add widget
        self.add_widget(self.settings_sample)

        # Arranging a callback to the switch
        # using bing function
        self.settings_sample.bind(active = switch_callback)

# Callback for the switch state transition
# Defining a Callback function
# Contains Two parameter switchObject, switchValue
def switch_callback(switchObject, switchValue):

    # Switch value are True and False
    if(switchValue):
        obj.push(1)
    else:
        obj.push(0)

# Defining the App Class
class SwitchApp(App):
    # define build function
    def build(self):
        # retuen the switch class
        return SimpleSwitch()


# Run the kivy app
if __name__ == '__main__':
    SwitchApp().run()
