"""
Tuxy bot.
"""

# pylint: disable=import-error, no-member
import cherrypy


class TuxyBot(object):
    """Tuxy Bot."""

    @cherrypy.expose
    @staticmethod
    def index():
        """Dummy Index Page."""
        return "OK"

    @cherrypy.expose
    @staticmethod
    def retine(key, value):
        """Register a key value pair."""
        cherrypy.session[key] = value
        # NOTE(mmicu): This is just an example, we should not expose this data
        # TODO(mmicu): It might be a good idea to have a new dict inside
        #              the session that stors only KVP's for this app
        return repr(cherrypy.session.items())

    @cherrypy.expose
    @staticmethod
    def palindrom(value=None):
        """Check if a string is palindrome."""
        if not value:
            return "The value can't be None."
        for key, value in cherrypy.session.items():
            value.replace(key, value)
        return str(value == value[::-1])

    @cherrypy.expose
    @staticmethod
    def calculeaza(val1, operator, val2):
        """Solve an equation Grade 1."""
        for key, value in cherrypy.session.items():
            val1 = val1.replace(key, value)
            operator = operator.replace(key, value)
            val2 = val2.replace(key, value)

        try:
            if operator == "+":
                return str(int(val1) + int(val2))
            elif operator == "-":
                return str(int(val1) - int(val2))
            elif operator == "*":
                return str(int(val1) * int(val2))
            elif operator == "/":
                return str(int(val1) / int(val2))
        except ValueError:
            return "Respecta constrangerile pentru: {} {} {}".format(
                val1, operator, val2)
        except ZeroDivisionError:
            return "Div by zero"

    @cherrypy.expose
    @staticmethod
    def curata():
        """Clean the sessin."""
        cherrypy.session.clear()


def main():
    """Main."""
    conf = {
        "/": {
            'tools.sessions.on': True,
        }
    }
    cherrypy.quickstart(TuxyBot(), "/", conf)


if __name__ == "__main__":
    main()
