"""How to use:

from src.debug.printer import DebugLog

@DebugLog.printer
def do_smth():
	...

for more Exception logging, add the needed Exception to the exception Tuple 'EXCEPTIONS'.
If you need a Excpetion, wich is not included in python by base, you can import the exception.
Example:
	from sqlalchemy.exc import SQLAlchemyError
	from requests import HTTPError
"""
import logging
import os
import traceback
from functools import wraps
from dotenv import load_dotenv, dotenv_values


EXCEPTIONS = (ValueError, TypeError, AttributeError, SyntaxError)

# lods the .env file
load_dotenv()



class DebugLog:
	
	
	@staticmethod
	def _setup_logger():
		"""macht die basic configurationen für den logging prozess"""
		logging.basicConfig(
			filename=os.getenv("DEBUG_LOG_FILE_PATH"),
			level=logging.ERROR,
			format="%(asctime)s - %(levelname)s - %(message)s"
		)
	
	@staticmethod
	def _log_error():
		"""loggt"""
		DebugLog._setup_logger()
		message = f"{traceback.format_exc()}"
		logging.error(message)  # speichert die message im log file
		print(message)  # Optional: zum schnellen Sehen im Terminal
	
	# decorator methode
	@staticmethod
	def printer(func):
		"""wird als @decorator für das Error Handling in einer methode oder funktion genutzt"""
		
		@wraps(func)
		def wrapper(*args, **kwargs):
			try:
				return func(*args, **kwargs)
			# alle möglichen Errors müssten hier aufgeführt werden
			except EXCEPTIONS:
				
				DebugLog._log_error()
				
				return None
		
		return wrapper
	
	@staticmethod
	def raiser(func):
		"""wird als @decorator für das Error Handling in einer methode oder funktion genutzt"""
		
		@wraps(func)
		def wrapper(*args, **kwargs):
			try:
				return func(*args, **kwargs)
			# alle möglichen Errors müssten hier aufgeführt werden
			except EXCEPTIONS as e:
				
				DebugLog._log_error()
				
				raise(e)
				
		
		return wrapper




