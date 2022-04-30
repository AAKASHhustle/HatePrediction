from ._anvil_designer import Form1Template
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run when the form opens.
    anvil.users.login_with_form()
  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    mytext = self.text_box_1.text
    result = anvil.server.call("my_server_gender",mytext)
    self.label_gender.text = result
    
    result2 = anvil.server.call("my_server_communal",mytext)
    self.label_communal.text = result2
    
    result3 = anvil.server.call("my_server_agg",mytext)
    self.label_aggression.text = result3
    
    result4 = anvil.server.call("my_server_hate",mytext)
    self.label_hate.text = result4
    
    result5 = anvil.server.call("my_server_profane",mytext)
    self.label_profane.text = result5
    
    output = [result,result2,result3,result3,result5]
    anvil.server.call('server_fn',mytext,output)
