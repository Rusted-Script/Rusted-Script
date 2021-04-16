# Copyright (c) Rusted Studio
# Licensed under APGL-3.0 license. Read LiCENSE.txt for more info
#Developers:
# CertifiedRice - Lead Developer
# Rusted Studio - Development Studio

import rustedscript

while True:
	text = input('Rusted_Script > ')
	result, error = rustedscript.run('<stdin>', text)

	if error: print(error.as_string())
	elif result: print(result)
