'''
C R E A T E   P L A Y A B L E   C S O U N D   M A N U A L

Copyright (c) 2017 by Michael Gogins.
Licensed under the terms of the GNU Lesser Public License version 2

This Python script creates a modified version of the Csound Reference Manual
in which the example CSDs will play online in standard Web browsersome using 
the WebAssembly build of Csound. The target is the docs directory of the 
csound-extended repository.

Customize the source and target directories, run this Python script, and then
add the target directory to the csound-extended Git repository and push your
changes.
'''

print(__doc__)

from io import StringIO
import glob
import os
import os.path
import shutil
import traceback

'''
The user must customize these variables. No additional configuration should be
required. The manual must already have been built in the usual way.
'''
source_home = r'''~/csound-extended-manual/manual'''
target_home = r'''~/csound-extended-manual/docs'''

source_html_directory = os.path.join(source_home, 'html')
source_examples_directory = os.path.join(source_html_directory, 'examples')

target_html_directory = target_home ### os.path.join(target_home, 'html')
target_examples_directory = os.path.join(target_html_directory, 'examples')

print('source_home:', source_home)
print('source_html_directory:', source_html_directory)
print('source_examples_directory:', source_examples_directory)
print('target_home:', target_home)
print('target_html_directory:', target_html_directory)
print('target_examples_directory:', target_examples_directory)

play_button_template = '''<a class="ulink" href="examples/%s.csd.html" target="_top"><button>Play</button></a>'''

def format_playable_example(filename, text):
    try:
        html_filename = filename
        print("Writing playable example: {}".format(html_filename))
        fout = StringIO()
        chunk = '''<html>
<head>
    <title>Minimal Example using Csound for WebAssembly</title>
 </head>
<body style="background-color:LightGrey;">
    <script src="CsoundAudioNode.js"></script>
    <script src="csound_loader.js"></script>
    <script>
    var csound_message_callback = function(message) {
        var messages_textarea = document.getElementById("console");
        var existing = messages_textarea.value;
        messages_textarea.value = existing + message;
        messages_textarea.scrollTop = messages_textarea.scrollHeight;
    }
    var onPlayClick = async function() {
        let messages_textarea = document.getElementById("console");
        messages_textarea.value = "";
        let csound_ = await get_csound(csound_message_callback);
        if (csound_ == null) {
            return;
        }
        let csd = document.getElementById('csd').value;
        await csound_.Stop();
        await csound_.Cleanup();
        await csound_.Reset();
        await csound_.CompileCsdText(csd);
        await csound_.Start();
        await csound_.Perform();
        
    }
    var onPlayStop = async function() {
        let csound_ = await get_csound(csound_message_callback);
        await csound_.Stop();
        await csound_.Cleanup();
        await csound_.Reset();
    }
  </script>
<h1 style="font-family:sans-serif;">'''
        fout.write(chunk)
        fout.write(html_filename)
        chunk = '''</h1>
<p>
This should play if your Web browser has WebAssembly enabled (most do). Most examples will play unless they need to load files. The first time you click <i>Play</i>, Csound will spend a few seconds loading, then play. You can edit this code and replay it. 
</p>
<p>
<input type="button" value="Play" onclick="onPlayClick()"/>
<input type="button" value="Stop" onclick="onPlayStop()"/>
<input type="button" value="Back" onclick="window.history.back()"/>
<p>
<textarea id="csd" style="width:98vw;height:45vh;font-family:monospace;background-color:#050570;color:#F0F090;">'''
        fout.write(chunk)
        # All examples MUST have sr = 48000; ksmps = 128; nchnls = 2; nchnls_i=1.
        # First we comment out ANY original settings.
        text = text.replace('sr ',       '; sr ', 1)
        text = text.replace('kr ',       '; kr ', 1)
        text = text.replace('ksmps ',    '; ksmps ', 1)
        text = text.replace('nchnls ',   '; nchnls ', 1)
        text = text.replace('nchnls_i ', '; nchnls_i ', 1)
        text = text.replace('sr=',       '; sr=     ', 1)
        text = text.replace('kr=',       '; kr=', 1)
        text = text.replace('ksmps=',    '; ksmps=', 1)
        text = text.replace('nchnls=',   '; nchnls=', 1)
        text = text.replace('nchnls_i=', '; nchnls_i=', 1)
        # Then we insert ALL correct settings.
        text = text.replace('<CsInstruments>\n', '<CsInstruments>\n\n; Required settings for WebAudio:\n\nsr = 48000\nksmps = 128\nnchnls = 2\nnchnls_i = 1\n')
        fout.write(text)
        chunk = '''</textarea>
<textarea id="console" readonly style="width:98vw;height:40vh;font-family:monospace;background-color:DarkSlateGrey;color:LawnGreen;">
</textarea>
</body>
</html>'''
        fout.write(chunk)
        return fout.getvalue()
    except:
        print('Exception on chunk: {}'.format(chunk))
        traceback.print_exc()

print()
print('Rewriting Csound Reference Manual pages to target...')
print()
source_pages = os.listdir(source_html_directory)
for filename in source_pages:
    source_pathname = os.path.join(source_html_directory, filename)
    source_basename = os.path.basename(source_pathname)
    source_filename, source_extension = os.path.splitext(source_basename)
    target_pathname = os.path.join(target_html_directory, filename)
    if (os.path.isfile(source_pathname)):
        if source_extension == '.html':
            print('Rewriting:', source_pathname, 'to:', target_pathname)
            with open(source_pathname, 'r') as source_file:
                source_page = source_file.read()
                source_page = source_page.replace("It uses the file ", "")
                # Imitate a button.
                # Original is like this:
                # <a class="ulink" href="examples/abs.csd" target="_top"><em class="citetitle">abs.csd</em></a>.
                source_page = source_page.replace('.csd" target="_top">', '.csd.html" target="_top" style="background-color:LightGray;border-color:LightGray;border-style:outset;border-radius:7px;color:Black;padding:.4em;text-decoration:none;font-family:sans-serif;"> Play ')
                source_page = source_page.replace('</em></a>.', '</em></a>')
                with open(target_pathname, 'w') as target_file:
                    target_file.write(source_page)
        else:
            print('Copying:', source_pathname, 'to:', target_pathname)
            shutil.copy(source_pathname, target_pathname)
print()
print('Rewriting Csound Reference Manual examples to target...')
print()
source_pages = os.listdir(source_examples_directory)
for filename in source_pages:
    source_pathname = os.path.join(source_examples_directory, filename)
    source_basename = os.path.basename(source_pathname)
    source_filename, source_extension = os.path.splitext(source_basename)
    target_pathname = os.path.join(target_examples_directory, filename) + '.html'
    if (os.path.isfile(source_pathname) and source_extension == '.csd'):
        print('Rewriting:', source_pathname, 'to:', target_pathname)
        with open(source_pathname, 'r') as source_file:
            with open(target_pathname, 'w') as target_file:
                source_page = source_file.read()
                target_page = format_playable_example(source_filename, source_page)
                target_file.write(target_page)
                
shutil.copy("index-frames.html", os.path.join(target_html_directory, "indexframes.html"))