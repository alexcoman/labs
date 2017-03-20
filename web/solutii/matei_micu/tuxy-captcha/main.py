"""
Tuxy captcha.
"""
# pylint: disable=import-error, no-member, invalid-name
import cherrypy


def get_data(filename):
    """Get data from a file."""
    with open(filename, 'r') as data:
        return data.read()


class TuxyCaptcha(object):
    """TuxyCaptcha."""
    exposed = True

    @staticmethod
    def GET():
        """GET method."""
        return get_data("index.html").format("")

    @staticmethod
    def POST(first, second, rez):
        """POST method."""
        try:
            # x + y = z
            # (z - y)/x
            val_x = float(first)
            val_y = float(second)
            val_z = float(rez)
            response = get_data("index.html").format((val_z-val_y)/val_x)
        except ValueError:
            return get_data("index.html").format("Parametri prosti")
        except ZeroDivisionError:
            return get_data("index.html").format(
                "Coeficientul lui x este 0 => x nu are o valoare exacta.")
        else:
            return response


def main():
    """Main."""
    conf = {
        "/": {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher()
        }
    }
    cherrypy.quickstart(TuxyCaptcha(), "/", conf)


if __name__ == "__main__":
    main()
