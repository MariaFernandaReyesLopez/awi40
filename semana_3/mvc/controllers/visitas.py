import web
import datetime

class Visitas:
  def GET(self, nombre):
    try:
      cookie = web.cookies()
      visitas = "0"
      dt = datetime.datetime.now()
      fecha = dt.strftime("%c")
      print(cookie)
      if nombre:
        web.setcookie("nombre",nombre,expires="", domain=None)
      else:
        nombre = "NA"
        web.setcookie("nombre",nombre,expires="", domain=None)

      if cookie.get("visitas"):
        visitas = int(cookie.get("visitas"))
        visitas += 1
        web.setcookie("visitas", str(visitas), expires="", domain=None)
      else:
        web.setcookie("visitas", str(1), expires="", domain=None)
        visitas = "1" 

      return "Visitas " + str(visitas) + "   Nombre " + nombre + "   Fecha y hora: " + str(fecha)
    except Exception as e:
      return "Error " + str(e.args)
