import http.server
import socketserver
from jinja2 import Environment, FileSystemLoader, select_autoescape
from ania.ui import printb, clear, bye
from termcolor import colored

port = 5666
handler = http.server.SimpleHTTPRequestHandler

env = Environment(
    loader=FileSystemLoader('ania/web_player/templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

def web_player(animei, servers):
  class Router(handler):
    def do_GET(self):
      if self.path == '/':
        template = env.get_template("index.html")
        content = template.render({'title': animei.title, 'servers': servers, 'episode': animei.episode})
        self.send_response(200)
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))
      
      elif self.path != '/':
        self.send_response(302)
        self.send_header('Location', '/')
        self.end_headers()    
 
  with socketserver.TCPServer(("", port), Router) as httpd:
    episode = colored(str(animei.episode), 'cyan', attrs=['bold'])
    title = colored(str(animei.title), 'yellow', attrs=['bold'])
    
    # UI
    clear()
    print(f'¡Ahora puedes ver el episodio {episode} de {title}!')
    printb('\nAbre este enlace en tu navegador:')
    print(f'http://localhost:{port} \n')
    
    try:
      httpd.serve_forever()
    except KeyboardInterrupt:
      httpd.server_close()
      httpd.socket.close()
    finally:
      bye()
