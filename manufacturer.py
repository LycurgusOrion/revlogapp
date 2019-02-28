from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton

class StudentListButton(ListItemButton):
    pass

class StudentDB(BoxLayout):
    f=ObjectProperty()
    l=ObjectProperty()
    s=ObjectProperty()

    def a(self):
        st=self.f.text+" "+self.l.text
        self.s.adapter.data.extend([st])
        self.s._trigger_reset_populate()

class StudentDBApp(App):
    def build(self):
        return StudentDB()

dbApp=StudentDBApp()
dbApp.run()