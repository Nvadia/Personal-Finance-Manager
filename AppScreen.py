import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def  __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1 #first grid

        self.inside = GridLayout() #defining second grid
        self.inside.cols = 2 #second grid
    
         #all .inside are inside the second grid
        self.inside.add_widget(Label(text="First Name: "))
        self.name = TextInput(multiline = False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Last Name: "))
        self.lastname = TextInput(multiline = False)
        self.inside.add_widget(self.lastname)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline = False)
        self.inside.add_widget(self.email)

        #these are the only two rows in the main grid
        self.add_widget(self.inside)

        self.submit = Button(text = "Submit", font_size = 20)
        self.submit.bind(on_press = self.pressed)
        self.add_widget(self.submit) 
        
    def pressed(self,  instance):
        print("Pressed")

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()
