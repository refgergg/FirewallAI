# How to use:

clone the git repository and set up a virtual environment:

```bash
$ git clone https://github.com/refgergg/FirewallAI.git
$ cd FirewallAI
$ python3 -m venv .venv
```

Install the python requirements:

```python
pip install -r requirements.txt
```

Add a .env file with your OpenAI API key like so:
```
OPENAI_KEY="{key}"
```
Replace `{key}` with your API key.


Finally, run `python server.py` first, then `python ai.py` in a seperate shell.
The server will be available at `http://localhost:5051`.
