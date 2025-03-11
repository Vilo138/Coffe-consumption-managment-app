from ._anvil_designer import DB_usersTemplate
from anvil import *
import anvil.server
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class DB_users(DB_usersTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.load_data()

  def load_data(self):
    """Načíta všetky riadky do Repeating Panel"""
    #self.repeating_panel_1.items = app_tables.users.search(tables.order_by("id", ascending=True))
    self.repeating_panel_1.items = app_tables.users.client_writable().search(tables.order_by("id", ascending=True))


  def button_1_click(self, **event_args):
    """Pridanie nového riadku do databázy a obnovenie UI"""
    #app_tables.users.add_row()
    #row = app_tables.users.get(id=item['id'])
    get_max_id = list(app_tables.users.search(tables.order_by('id', ascending=False)))[:1]
    #print(get_max_id)
    max_id = get_max_id[0]['id']
    if max_id is None:
      new_max_id = 1
    else:
      new_max_id = max_id + 1
    app_tables.users.add_row(id=new_max_id)
    self.load_data()

  
