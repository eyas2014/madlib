import httpx
from fastapi import FastAPI, Response
import requests


app = FastAPI()

@app.get('/madlib')
def madlib():
	url='https://reminiscent-steady-albertosaurus.glitch.me/'

	words=[]
	for verb in ['adjective','verb','noun']:
		response=requests.get(url+verb).text
		words.append(response.strip('"'))

	response='It was a {adjective} day. '\
		'I went downstairs to see if I could {verb} dinner. '\
		'I asked, "Does the stew need fresh {noun}?"'\
		.format(adjective=words[0],
				verb=words[1],
				noun=words[2])

	return Response(response)