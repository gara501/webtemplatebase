import os

'''
  Templates Definition
  type (string): Template type to return
'''
def _code_base(type):
  if type == "html":
    return '''<!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Demo</title>
      <link rel="stylesheet" type="text/css" href="css/styles.css">
    </head>
    <body>
    </body>
    <script src="js/app.js"></script>
  </html>'''
  elif type == "css":
    return ''':root {
      box-sizing: border-box;
    }

    *,
    *::before,
    *::after {
      box-sizing: inherit;
      margin: 0;
      padding: 0;
    }'''
  elif type == "js":
    return '''/* Js File */'''
  
'''
  Create local file
  path (string): file path
  template (string): template code from _code_base
'''
def _create_local_file(path, template):
  try:
    f = open(path, "w")
    f.write(template)
    f.close()
    print("File created in: ", path)
  except:
    print("Error creating file")  
  
'''
  Create file
  filetype (string): File type to create
''' 
def create_file(filetype):
  path = os.getcwd()
  filepath = path + "/template/"
  
  template = _code_base(filetype)
  
  if filetype == "html":
    _create_local_file(filepath + "index.html", template)
  elif filetype == "css":
    _create_local_file(filepath + "css/styles.css", template)
  elif filetype == "js":
    _create_local_file(filepath + "js/app.js", template)

'''
  Create folders
  folders (Array): Array with the folders
''' 
def create_folders(folders):
  # create directory to save the template
  path = os.getcwd()
  
  for folder in folders:
    template_path = path + "/" + folder
    isDir = os.path.isdir(template_path)

    if not isDir:
      try:
        access_rights = 0o755
        os.mkdir(template_path, access_rights)
      except OSError:
        print("error creating directory")
      else:
        print("Directory created succesfully", template_path)
'''
  Init
  Initialize the script
''' 
def init():
  print("Script initialization: ------------")
  folders = ["template", "template/css", "template/js", "template/assets", "template/assets/images"]
  templates = ["html", "css", "js"]
  
  create_folders(folders)
  
  for item in templates:
    create_file(item)
  
  print("Process Finished: ------------")

init()