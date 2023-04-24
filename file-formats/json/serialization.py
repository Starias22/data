import json
var = {
	"Subjects": {
				"Maths":85,
				"Physics":90
				}
	}

with open("Sample.json", "w") as stream:
	json.dump(var, stream)
