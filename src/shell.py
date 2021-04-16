import rustedscript

while True:
	text = input('Rusted_Script > ')
	result, error = rustedscript.run('<stdin>', text)

	if error: print(error.as_string())
	elif result: print(result)