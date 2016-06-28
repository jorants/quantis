#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import os
import imp
import re
import mimetypes
from urlparse import urlparse,parse_qs
import traceback
ROOT_PATH = "document_root/"
SPECIAL_PATH = "special/"
PORT_NUMBER = 8080

index = [
        "index.py",
        "index.html"
]


def parse_python_file(filename):
        data = open(filename).read()
        if data[:7]=="#HIDDEN":
                return None
        reg = re.compile("<\?python((.|\n)+?)nohtyp\?>",re.MULTILINE)
        result = reg.split(data)
        parts =  filter(lambda x: len(x.strip())>0,result)
        if data.strip()[:8] == "<?python":
                parts = [""]+parts
        txt_frm = "echo(\"\"\"%s\"\"\")\n"
        python_code = ""
        for i,txt in enumerate(parts):
                if i%2 == 0:
                        python_code+= txt_frm % txt
                else:
                        python_code += txt + "\n"
        return  python_code


#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
                self.HTTPtype = "GET"
                self.do_request()
            
        def do_POST(self):
                content_len = int(self.headers.getheader('content-length', 0))
                post_body = self.rfile.read(content_len)
                self.POST = parse_qs(post_body)                 
                self.HTTPtype = "POST"                            
                self.do_request()

        def do_request(self):
                res =  urlparse(self.path)
                path = res.path
                self.GET = parse_qs(res.query)
                
                realpath = os.path.join(ROOT_PATH,os.path.normpath(path)[1:])
                
                
                if os.path.isdir(realpath):
                        for i in index:
                                if os.path.isfile(os.path.join(realpath,i)):
                                        realpath = os.path.join(realpath,i)
                                        break
                                
                if not os.path.isfile(realpath):
                        self.error404()
                        return

                if realpath[-4:] == ".pyc":
                        self.eror404()
                        return
                
                if realpath[-3:] == ".py":

                        code = parse_python_file(realpath)
                        if code==None:
                                self.error404()
                                return
                        self.txt = ""
                        self.header_closed = False
                        env = {
                               'headers':{'Content-type':"text/html"},
                               'status':200,
                               
                        }
                        
                        def echo(s):
                                s = s
                                if self.header_closed:
                                        self.wfile.write(s)
                                else:
                                        self.txt += s
                                        
                        def println(*args):
                                echo(str(args[0]))
                                for a in args[1:]:
                                        echo(" "+str(a))
                                echo("\r\n")

                        def close_header():
                                if not self.header_closed:
	                                self.send_response(env['status'])
                                        for key in env['headers']:
                                                self.send_header(key,env['headers'][key])
	                                self.end_headers()
                                        self.header_closed = True
                                        self.wfile.write(self.txt)

                        def load(path):
                                d = os.path.dirname(realpath)
                                p = os.path.join(d,path)
                                mod = imp.load_source(os.path.basename(p).split(".")[0],p)
                                return mod

                        def include(path):
                                d = os.path.dirname(realpath)
                                p = os.path.join(d,path)
                                mod = imp.load_source(os.path.basename(p).split(".")[0],p)
                                env[os.path.basename(p).split(".")[0]] = mod
                                return mod

                        
                        env['echo'] = echo
                        env['println'] = println
                        env['close_header'] = close_header
                        env['REQUEST_URL'] = self.path
                        env['GET'] = self.GET
                        env['TYPE'] = self.HTTPtype
                        env['load'] = load
                        env['include'] = include


                        if env['TYPE'] == "POST":
                                env['POST'] = self.POST
                        else:
                                env['POST'] = []
                        
                        try:

                                exec code in env
                                close_header()
                        except SystemExit:
                                close_header()
                        except Exception as e:
                                self.send_response(200)
	                        self.send_header('Content-type',"text/plain")
                                self.end_headers()
                                self.wfile.write("An error has occured: "+ str(e)+"\n")
                                self.wfile.write(traceback.format_exc())
                                
                else:
                        mime = mimetypes.guess_type(realpath)                        
                        self.send_response(200)
                        if mime[0] != None:
	                        self.send_header('Content-type',mime[0])
	                self.end_headers()                
                        
                        self.wfile.write(open(realpath).read())
                        return 

                
        def error404(self):
	        self.send_response(404)
	        self.send_header('Content-type','text/html')
	        self.end_headers()
                if os.path.isfile(os.path.join(SPECIAL_PATH,"404.html")):
                        self.wfile.write(open(os.path.join(SPECIAL_PATH,"404.html")).read())
                else:
                        error = "<html><body><h1>404 - File not found</h1>Sorry, you are in the wrong place.</body></html>"
                        self.wfile.write(error)            
try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER	
	#Wait forever for incoming htto requests
	server.serve_forever()
except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()



        
