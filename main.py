import kivy
from kivy.app import App
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.button import Button


# Replace this with your
# current version
kivy.require('1.11.1')

# Defining a class
class MyFirstKivyApp(App):
	
	# Function that returns
	# the root widget
	def build(self):
		
		# Label with text Hello World is
		# returned as root widget
		return Button(text ="Hello World !")		


# Here our class is initialized
# and its run() method is called.
# This initializes and starts
# our Kivy application.
MyFirstKivyApp().run()			
