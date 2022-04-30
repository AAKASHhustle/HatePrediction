import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def server_fn(text,result):
  app_tables.table1.add_row(Tweet=text,Gender_Bias=result[0],Communal_Bias=result[1],Aggression=result[2],Hate_Speech=result[3],Profanity=result[4],Author=anvil.users.get_user())
