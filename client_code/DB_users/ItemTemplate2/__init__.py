from ._anvil_designer import ItemTemplate2Template
from anvil import *
import anvil.server
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ItemTemplate2(ItemTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.text_box_1.text = self.item['id']
    self.text_box_2.text = self.item['name']
    self.text_box_3.text = self.item['email']
    #self.text_box_2.enabled = False


    # Any code you write here will run before the form opens.

  def button_del_click(self, **event_args):
    #self.repeating_panel_1.items = app_tables.users.client_writable().search(tables.order_by("id", ascending=True))
    if confirm('Are you sure you want to PERMANENTLY delete this row?'):
      self.item.delete()
      self.remove_from_parent()
  


  #def text_box_2_lost_focus(self, **event_args): 
  #    self.item['name'] = self.text_box_2.text  # Aktualizácia 
  #    anvil.server.call('update_row_name', self.item)    


  #def button_edt_click(self, **event_args):
  #    self.text_box_2.enabled = True
  #    self.item['name'] = self.text_box_2.text  # Aktualizácia hodnoty
  #    anvil.server.call('update_row', self.item)
      #self.text_box_2_lost_focus()

  
  
  def text_box_3_lost_focus(self, **event_args):
      self.item['email'] = self.text_box_3.text  # Aktualizácia 
      anvil.server.call('update_row_email', self.item)

  def text_box_2_change(self, **event_args):
    if not hasattr(self, "timer_running"):
        self.timer_running = False

    if not self.timer_running:
        self.timer_running = True
        self.timer = Timer(interval=0.5, function=self.update_name)
  def update_name(self):
    self.timer_running = False
    self.item['name'] = self.text_box_2.text
    anvil.server.call('update_row_name', dict(self.item))

  

  

    
      
