# Study Spark – AI Text Summarizer for students
Study Spark is an AI-powered desktop application 
that uses Microsoft’s Phi 3 mini 4k instruct q4 
model to summarize text in a variety of note-taking 
methods. One of the challenges I faced when creating 
this model were finding a model that could run on CPU-only
devices that would also generate a satisfactory output. 
The graphical user interface would also freeze when the 
model would run. To overcome these challenges, I tested a 
variety of models and came to the conclusion that Phi 3 
not only provided satisfactory responses for users, but did 
so at only 2GB of ram and high CPU usage. To overcome the 
GUI freeze, I ran the GUI on the main thread while the 
model ran in a different worker thread. Prompts given to the model are synthetic.
## How to use this project
To modify and install this project manually you need the following installed:
-	Visual Studio (Desktop Development with C++ workload)
-	Python 3.12
-	Graphiz

In the root directory open the terminal and type: `mkdir models`. Then download the file at this link https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4.gguf and add it to the 
models subfolder.

If you have the above installed type this command in your terminal ‘pip install -r requirements.txt’
When you are finish modifying the project, type the following command in the root directory of your project:

    nuitka "Study Spark.py" ^
      --standalone ^
      --enable-plugin=pyside6 ^
      --include-data-dir=models=models ^
      --output-dir="Study Spark" ^
      --output-filename="Study Spark.exe" ^
      --windows-console-mode=disable

Open the created subfolder and run the 'Study Spark.exe' file to use the program.

### License
This Project is under the MIT License
