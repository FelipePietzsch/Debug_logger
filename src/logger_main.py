"""How to use:

from src.debug.debug_log import DebugLog

@DebugLog.debug_log
def do_smth():
	...

for more Exception logging, add the needed Exception to the esception Tuple
"""

import logging
import os
import traceback
from sqlalchemy.exc import SQLAlchemyError, ArgumentError
from functools import wraps
from requests import HTTPError
from mistralai.models.sdkerror import SDKError

EXCEPTIONS = (ValueError, TypeError, AttributeError, SyntaxError)

class DebugLog:
	log_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../debug_data/debug.log"))
	
	@staticmethod
	def _setup_logger():
		"""macht die basic configurationen für den logging prozess"""
		logging.basicConfig(
			filename=DebugLog.log_file_path,
			level=logging.ERROR,
			format="%(asctime)s - %(levelname)s - %(message)s"
		)
	
	@staticmethod
	def log_error():
		"""loggt"""
		DebugLog._setup_logger()
		message = f"{traceback.format_exc()}"
		logging.error(message)  # speichert die message im log file
		print(message)  # Optional: zum schnellen Sehen im Terminal
	
	# decorator methode
	@staticmethod
	def debug_log(func):
		"""wird als @decorator für das Error Handling in einer methode oder funktion genutzt"""
		
		@wraps(func)
		def wrapper(*args, **kwargs):
			try:
				return func(*args, **kwargs)
			# alle möglichen Errors müssten hier aufgeführt werden
			except EXCEPTIONS as e:
				tb = traceback.extract_tb(e.__traceback__)
				last_trace = tb[-1]
				
				DebugLog.log_error()
				print(f"Error: {func.__name__}: {e}")
				
				return None
		
		return wrapper




