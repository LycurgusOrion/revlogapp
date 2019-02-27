from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


Builder.load_string("""
<whoscreen>:
    canvas:
        Rectangle:
            source: 'abc.jpg'
            pos: self.pos
            size: self.size
	Label:
		pos_hint:{"x":0,"y":0.4}
		text:"Choose User Type"
		font_size:30

	Button:
	    on_press: root.manager.current = 'retailerscreen'
	    pos_hint:{"x":0.35,"y":0.6}
	    text:"Retailer"

	Button:
	    pos_hint:{"x":0.35,"y":0.4}
	    text:"Executive"
	    on_press: root.manager.current = 'executivescreen'

	Button:
	    pos_hint:{"x":0.35,"y":0.2}
	    text:"Manufacturer"
	    on_press: root.manager.current = 'manufacturerscreen'

<retailerscreen>:
    canvas:
        Rectangle:
            source: 'abc.jpg'
            pos: self.pos
            size: self.size       
    Button:
	    on_press: root.manager.current = 'whoscreen'
	    on_press:nameinput.text=""
	    on_press:passinput.text=""
	    size_hint:0.2,0.08
	    pos_hint:{"x":0,"top":1}
	    text:"Back"
		
	Button:
		pos_hint:{"x":0.2,"y":0.1}
		text:"   Forgot\\nPassword"

	Button:
		pos_hint:{"x":0.5,"y":0.1}
		text:"Login"
		on_press: root.manager.current ='newscreen'
	 
		

	Label:
		pos_hint:{"x":-0.2,"y":0.2}
		text:"Username"

	Label:
		pos_hint:{"x":-0.2,"y":0}
		text:"Password"
	TextInput:
		id: nameinput
		size_hint: (.2, None)
		height: 30
		pos_hint:{"x":0.5,"y":0.67}
		multiline:False

	TextInput:
		id: passinput
		size_hint: (.2, None)
		height: 30
		pos_hint:{"x":0.5,"y":0.47}
		multiline:False
		password:True

<executivescreen>:
    canvas:
        Rectangle:
            source: 'abc.jpg'
            pos: self.pos
            size: self.size       
    Button:
	    on_press: root.manager.current = 'whoscreen'
	    on_press:nameinput.text=""
	    on_press:passinput.text=""
		pos_hint:{"x":0,"top":1}
		text:"Back"
		
	Button:
		pos_hint:{"x":0.2,"y":0.1}
		text:"   Forgot\\nPassword"

	Button:
		pos_hint:{"x":0.5,"y":0.1}
		text:"Login"
	 
		

	Label:
		pos_hint:{"x":-0.2,"y":0.2}
		text:"Username"

	Label:
		pos_hint:{"x":-0.2,"y":0}
		text:"Password"
	TextInput:
		id: nameinput
		size_hint: (.2, None)
		height: 30
		pos_hint:{"x":0.5,"y":0.67}
		multiline:False

	TextInput:
		id: passinput
		size_hint: (.2, None)
		height: 30
		pos_hint:{"x":0.5,"y":0.47}
		multiline:False
		password:True

<manufacturerscreen>:
    canvas:
        Rectangle:
            source: 'abc.jpg'
            pos: self.pos
            size: self.size       
    Button:
	    on_press: root.manager.current = 'whoscreen'
	    on_press:nameinput.text=""
	    on_press:passinput.text=""
		pos_hint:{"x":0,"top":1}
		text:"Back"
		
	Button:
		pos_hint:{"x":0.2,"y":0.1}
		text:"   Forgot\\nPassword"

	Button:
		pos_hint:{"x":0.5,"y":0.1}
		text:"Login"
	 
		

	Label:
		pos_hint:{"x":-0.2,"y":0.2}
		text:"Username"

	Label:
		pos_hint:{"x":-0.2,"y":0}
		text:"Password"
	TextInput:
		id: nameinput
		size_hint: (.2, None)
		height: 30
		pos_hint:{"x":0.5,"y":0.67}
		multiline:False

	TextInput:
		id: passinput
		size_hint: (.2, None)
		height: 30
		pos_hint:{"x":0.5,"y":0.47}
		multiline:False
		password:True

		
<newscreen>:
    canvas:
        Rectangle:
            source: 'abc.jpg'
            pos: self.pos  
            size: self.size
    Button:
	    on_press: root.manager.current = 'retailerscreen'	    
		pos_hint:{"x":0,"top":1}
		text:"Back"
		size_hint:0.2,0.08
    Button:
	    on_press: root.manager.current = 'mainscreen'
	    pos_hint:{"x":0.35,"y":0.6}
	    text:"Generate New"

	Button:
	    pos_hint:{"x":0.35,"y":0.4}
	    text:"Show Pending"
	    on_press: root.manager.current = 'datascreen'
    
<datascreen>:
    canvas:
        Rectangle:
            source: 'abc.jpg'
            pos: self.pos  
            size: self.size
    Button:
	    on_press: root.manager.current = 'newscreen'	    
		pos_hint:{"x":0,"top":1}
		text:"Back"
		size_hint:0.2,0.08


<mainscreen>:    
    canvas:
        Rectangle:
            source: 'abc.jpg'
            pos: self.pos  
            size: self.size

    Button:
	    on_press: root.manager.current = 'retailerscreen'
	    on_press:btn.text="Select brand:"
	    on_press:btn2.text="Select product:"
        on_press:quantityinput.text=""	    
		pos_hint:{"x":0,"top":1}
		text:"Back"
		size_hint:0.2,0.08

        
	Label:
		pos_hint:{"x":0,"y":0.4}
		text:"Choose Item and Quantity"
		font_size:30
		
	Label:
		pos_hint:{"x":-0.15,"y":-0.1}
		text:"   Enter\\n Quantity"
		font_size:20
		
	TextInput:
		id: quantityinput
		size_hint: (.2, None)
		height: 30
		pos_hint:{"x":0.5,"y":0.38}
		multiline:False
		
	Button:
	    text: 'Submit'
	    on_press: root.manager.current = 'newscreen'
        pos_hint:{"x":0.7,"y":0.15}
        size_hint_y: None
        height: '48dp'

		
	Button:
        id: btn
        text: 'Select brand'
        on_release: dropdownbrand.open(self)
        size_hint_y: None
        height: '48dp'
        pos_hint:{"x":0.2,"y":0.7}
        
    DropDown:
        id: dropdownbrand
        on_select: btn.text = 'Selected brand:\\n     {}'.format(args[1])

        Button:
            text: 'Item A'
            size_hint_y: None
            height: '48dp'
            on_release: dropdownbrand.select('Brand A')

        Button:
            text: 'Item B'
            size_hint_y: None
            height: '48dp'
            on_release: dropdownbrand.select('Brand B')

        Button:
            text: 'Item C'
            size_hint_y: None
            height: '48dp'
            on_release: dropdownbrand.select('Brand C')
            
     
    Button:
        id: btn2
        text: 'Select product'
        on_release: dropdownproduct.open(self)
        size_hint_y: None
        height: '48dp'
        pos_hint:{"x":0.5,"y":0.7} 
            
    DropDown:
        id: dropdownproduct
        on_select: btn2.text = 'Selected product:\\n     {}'.format(args[1])

        Button:
            text: 'Item A'
            size_hint_y: None
            height: '48dp'
            on_release: dropdownproduct.select('Product A')

        Button:
            text: 'Item B'
            size_hint_y: None
            height: '48dp'
            on_release: dropdownproduct.select('Product B')

        Button:
            text: 'Item C'
            size_hint_y: None
            height: '48dp'
            on_release: dropdownproduct.select('Product C')
    
		
<Button>:
	color:1,1,1,1
	font_size:16
	size_hint:0.3,0.1
""")


class whoscreen(Screen):
    pass

class retailerscreen(Screen):
    pass
class executivescreen(Screen):
    pass
class manufacturerscreen(Screen):
    pass

class mainscreen(Screen):
    pass

class newscreen(Screen):
    pass

class datascreen(Screen):
     pass


sm = ScreenManager()
sm.add_widget(whoscreen(name='whoscreen'))
sm.add_widget(retailerscreen(name='retailerscreen'))
sm.add_widget(executivescreen(name='executivescreen'))
sm.add_widget(manufacturerscreen(name='manufacturerscreen'))
sm.add_widget(mainscreen(name='mainscreen'))
sm.add_widget(newscreen(name='newscreen'))
sm.add_widget(datascreen(name='datascreen'))


class TestApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()
