# microservice implementation for atlas workout app

Hello, and thank you for working with me. The microservice that I have developed for your app, as we've discussed, receives information
about a user and their workout, calculates their average pace and calories burned, and returns the results of those calculations.

I have provided code that you can use to call the microservice:

# example user data
This is what you will change; instead of hard-coded values, assign the user's actual input and information to these variables.
Leave the variable names as-is so the subprocess call can reference them.

`workout_distance = 5        # must be passed as a number. miles for running/biking, meters for swimming`<p>
`workout_minutes = 120`<p>
`workout_type = "run"        # microservice will recognize strings "run", "bike", or "swim"`<p>
`athlete_weight = 89         # athlete's weight in kg required for calculating calories burned`

# code for calling microservice
`# ----- DO NOT CHANGE ANYTHING IN THIS BLOCK -----`

`# this takes those variables, plugs them into stdin, and calls the microservice!`

`input_data = {"distance": workout_distance, "duration": workout_minutes, "type": workout_type, "weight": athlete_weight}`

`input_string = str(input_data)`

`microservice = subprocess.Popen(["python", "workout_data_calculator.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)`

`microservice.stdin.write(input_string.encode())`

`microservice.stdin.close()`
`# --------------------------------------------------`

# handling output
Finally, this line of code will receive the data and put it into a variable (called my_output but you can name it whatever)
`my_output = microservice.stdout.read()`

The output data will be a string, so you can change it into a usable dictionary with this line (you'll need to import ast):
`my_usable_output = ast.literal_eval(my_output)`

And now you can pull values out of the dictionary by key:
`my_usable_output.get("pace")` 
`my_usable_output.get("calories")`

These get calls will return strings in the format "x number calories burned" and "y minutes per mile" etc. The idea is that you can 
pull them directly from the dictionary and slap them into your app's UI as-is, without needing to do anything else. This should be all
you need to know!!! 

UML sequence diagram: 
![Untitled presentation](https://github.com/angelia-grace/cs361project/assets/138550182/b609c52e-de63-4597-b36f-aafe84fafe8b)
