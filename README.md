# Gemini 101 Workshop

This is a workshop dedicated to introducing Google's Gemini API with Python and Streamlit. You'll learn how to generate an API key, authenticate with the API, make requests to the Gemini API, and output the response to the web with streamlit.


## Getting Started

We'll first start with creating a new API key.

### Step 1: Open Google AI Studio and Login / Create an Account

Here's the link: https://aistudio.google.com/app/apikey

<img width="1469" alt="1" src="https://github.com/realTristan/geminiworkshop/assets/75189508/362d8f6d-c6ec-4293-a154-52bb1e782c8c">

### Step 2: Click on "Create API key"

This opens the modal to select which GC project to create an API in.

<img width="1355" alt="2" src="https://github.com/realTristan/geminiworkshop/assets/75189508/55ceb68f-4ff9-4b26-9d1f-54f435648997">

### Step 3: Click "Create API key in new project"

If you don't have an existing project, you can create a new one. Otherwise, select the project you'd like to create the API key for.

<img width="1354" alt="3" src="https://github.com/realTristan/geminiworkshop/assets/75189508/66a209f0-5650-4eb0-bd6f-8e1e81711234">

### Step 4: Copy the API key

Copy the API key and save it for later. We'll need it soon.

## Folder Structure

Now that we've created our API key, we need to create a new folder where our Python files will be stored.

### Step 1: Create a new folder

Create the folder that you want to store your Python code and files in.

### Steps 2: Creating required files

#### Source Folder

This is where we'll store our source code.

1. Create a new folder called: `src`
2. Inside the `src` folder, create a new file called: `main.py`
3. Inside the `src` folder, create a new folder called: `utils`.
4. Inside the `src/utils` folder, create a new file called: `to_markdown.py`

Done!

#### Creating the config file

This is where we'll store our API key and project configurations.

1. Create a new file called: `config.json`
2. Add the following content to the file:

```json
{
  "gemini": {
    "api_key": "YOUR GEMINI API KEY"
  }
}
```

Note: If you cloned the repository, rename `config.template.json` to `config.json`.

Done!

## Coding

Now we'll actually get into the coding!

### Requirements

First we need to install some libraries.

```bash
pip install -q -U google-generativeai streamlit IPython
```

### File: to_markdown.py

We'll start with coding the `to_markdown` function. This function will convert a text to markdown format.

```python
import textwrap
from IPython.display import Markdown


##
## Convert a text to markdown format
##
def to_markdown(text: str):
    text = text.replace("•", "  *")

    return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))
```

### File: app.py

This is our main file. See `src/app.py` for the code.

## Running the program

An example of running the program is shown below:

```bash
streamlit run /Users/skewalramani/Desktop/geminiworkshop/src/app.py
```

Basically, you'll need the path to your `app.py` file. You can get this however you like, but if you run the python file normally, streamlit will output the proper command to run.
