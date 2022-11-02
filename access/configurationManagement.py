from datetime import datetime
from . import saseApi

class configurationManagement:
	"""configurationManagement class"""

	def checkTokenStillValid(self):
		"""
		Checks to see if the token is still valid. 
		Returns true is still in 15minute window. 
		Returns false if not.
		"""
		rightNow = datetime.now()
		tokenValid = bool(rightNow < self.prismaAccessObject.saseToken['expiresOn'])
		return tokenValid

	def __init__(self, __prismaAccessObject):
		"""configurationManagement class initialization"""
		self.prismaAccessObject = __prismaAccessObject