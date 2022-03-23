actorRoles = [
  ["Nathan Fillion", "Captain Malcolm Reynolds"],
  ["Gina Torres", "Zoe Washburn"],
  ["Alan Tudyk", "Hoban Washburn"],
  ["Morena Baccarin", "Inara Serra"],
  ["Adam Baldwin", "Jayne Cobb"],
  ["Jewel Staite", "Kaylee Frye"],
  ["Sean Maher", "Dr. Simon Tam"],
  ["Summer Glau", "River Tam"],
  ["Ron Glass", "Derrial Book"],
]



print(
  """Featuring:
  _=_=_=_=_=_=_=_=_=_"""
  )


for actorRole in actorRoles:
  actor = actorRole[0]
  role = actorRole[1]
  print(actor + " as " + role)