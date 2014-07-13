import webapp2


from app import Main


app = webapp2.WSGIApplication([
    webapp2.Route('/', handler=Main.MainHandler)
], debug=True)
