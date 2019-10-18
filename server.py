from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib
from battleship import Battleship
import sys


host = "localhost"
port = int(sys.argv[1])
board_path =  sys.argv[2]

game = Battleship(board_path = board_path)
print(game.format_board(game.opp_board))

class Handler(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        if self.path == ("/own_board.html"):
            #print("Serving own board")
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            board = game.generate_board_html(game.own_board)
            #print(game.format_board(game.own_board))
            self.wfile.write(bytes(board,'utf-8'))

        if self.path == ("/opponent_board.html"):
            #print("Serving opponent board")
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            board = game.generate_board_html(game.opp_board)
            #print(game.format_board(game.opp_board))
            self.wfile.write(bytes(board,'utf-8'))


    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        content = self.rfile.read(content_length).decode("utf-8") 
        #print(content)
        content_parsed = urllib.parse.parse_qs(content)
        #print(content_parsed["x"])


        try:
            x = int(content_parsed["x"][0])
            y = int(content_parsed["y"][0])

            if game.validate_coordinates(x, y) == 0:
                response = 404 #not found
                result_encoded = ''
            else:
                result = game.receive_fire(x, y)
                #print(result)
                if result['hit'] == -1:
                    response = 410 #gone
                    result_encoded = ''

                elif result['hit'] >= 0:
                    response = 200 #ok
                    result_encoded = urllib.parse.urlencode(result)
        except:
            response = 400
            result_encoded = ''

        #print(result_encoded)
        self.send_response(response)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(result_encoded.encode("utf-8"))


server = HTTPServer((host, port), Handler)

server.serve_forever()
