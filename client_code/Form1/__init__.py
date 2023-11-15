from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.media 


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.label_1.text=str(file.name )
    pass
  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.x=anvil.server.call("hi",self.label_1.text,self.query_holen())
    self.text_area_1.text=str(self.x["answer"])
    #summarization.generate_summary_kivy(str(file.name),self.query_holen())

  def query_holen(self):
    if self.radio_button_1.selected==True:
      return str(self.radio_button_1.text)
    elif self.radio_button_2.selected==True:
      return str(self.radio_button_2.text)
    elif self.radio_button_3.selected==True:
      return str(self.text_area_1.text)
    else:
      return print("No Query selected")

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    anvil.media.download(my_media_object)
    pass
    