"""testing the debug_log out from a class"""
from debug_logger import DebugLog

class ArmtSum:
	
	def sum_list(self, lst: list[int]) -> int:
		"""sum_list input"""
		return sum(lst)
	
	def gen_artm_lst(self, num: int) -> list[int]:
		"""generates a arithmetic list of numbers """
		return [i + i for i in range(num)]
	
	def get_artm_logic_lst(self, num: int) -> list[dict[str:int]]:
		"""calculates the logic of how the sum of arithmetic lists growing and retunrs a list of dicts"""
		res_lst = []
		for i in range(num):
			artm_lst = self.gen_artm_lst(num=i)
			sum = self.sum_list(lst=artm_lst)
			
			res_dict = self.pack_res_in_dict(i, artm_lst, sum)
			res_lst.append(res_dict)
		
		return res_lst
	
	def pack_res_in_dict(self, num: int, artm_lst: list[int], sum: int) -> dict[str:int]:
		"""stores arguments in dictionary"""
		return {
			"i": num,
			"artm_lst": artm_lst,
			"sum": sum
		}
	
	def get_range_of_nums(self):
		"""takes user input and turns it into an int"""
		input_num = input("Type in a range:")
		
		if not isinstance(input_num, int):
			raise TypeError("This is a test_TypeError!!!")
		
		return input_num
	
	@DebugLog.debug_log
	def run(self):
		input_num = self.get_range_of_nums()
		
		armt_logic_list = self.get_artm_logic_lst(input_num)
		
		for i, dict in enumerate(armt_logic_list):
			print(f"{i + 1}: num: {dict['i']}; \nartm_lst: {dict['artm_lst']}; \nsum: {dict['sum']}")
