def getNextAttribute(file_handle):
	line = file_handle.readline()
	line = line.rstrip()
	return line.split(':')[1]



class Action:
	#Constructor
	def __init__(self, text_file):
		file_handle = open(text_file, 'r')
		
		self.name = getNextAttribute(file_handle)
		self.target_all = getNextAttribute(file_handle) == 'True'
		self.health_steal = float(getNextAttribute(file_handle))/100.0
		self.cooldown = int(getNextAttribute(file_handle))
		self.damage_modifier = float(getNextAttribute(file_handle))/100.0
		self.target_allies = getNextAttribute(file_handle) == 'True'

