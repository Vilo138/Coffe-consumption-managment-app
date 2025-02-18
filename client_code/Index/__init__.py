from ._anvil_designer import IndexTemplate
from anvil import *
import anvil.server
import anvil.users
from datetime import datetime
from anvil.tables import app_tables
import sys
from ..DatePickerDialog import DatePickerDialog
from anvil import alert
from ..Test import Test
from ..Home import Home



import anvil.tables as tables
import anvil.tables.query as q
#from anvil.tables import app_tables
from anvil import open_form
from .. import login_flow

class Index(IndexTemplate):
    def __init__(self, **properties):
        # Toto nastaví komponenty na formulári
        self.init_components(**properties)

        # Zmena textu na prihlasovacom tlačidle
        self.update_sign_in_text()
        #print(sys.path)
        self.content_panel.add_component(Home())
        

    def update_sign_in_text(self):
        """Aktualizuje text prihlasovacieho tlačidla"""
        user = anvil.users.get_user()
        if user:
            email = user["email"]
            self.sign_in.text = email
        else:
            self.sign_in.text = "Sign In"

    def sign_in_button(self, **event_args):
        """Pri kliknutí na tlačidlo sa používateľ prihlási"""  
        login_flow.do_email_confirm_or_reset()
        self.content_panel.clear()
        self.content_panel.add_component(Test())
        #open_form('Test')

    
    
    


#

    def generate_pdf_button_click(self, **event_args):
        # Zobrazenie modálneho dialógu na výber dátumov
        #dates = DatePickerDialog().show()
        dialog = DatePickerDialog()
        result = alert(content=dialog, large=True, buttons=[])
        if result is None:
          print("Používateľ zrušil dialóg.")
        else:
          print("Výsledok:", result)
          start_date, end_date = result
          data = anvil.server.call('get_filtered_data', start_date, end_date)
          pdf = anvil.server.call('generate_pdf', data)
          anvil.media.download(pdf)  # Stiahnutie PDF
        #dates = dialog.show()

    def title_click(self, **event_args):
      """This method is called when the link is clicked."""
      if not isinstance(self.content_panel.get_components()[-1], Home):
        # Clear existing components and add Home
        self.content_panel.clear()
        self.content_panel.add_component(Home())
      

        
      

        
        
        

    


