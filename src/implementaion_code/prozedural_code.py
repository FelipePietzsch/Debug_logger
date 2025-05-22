"""file überprüft, ob DebugLog auch funktioniert und eine log-datei geschrieben wird."""
from yaql.standard_library.legacy import range_
from src.debug_logger import DebugLog

def sum_list(lst:list[int]) -> int:
	"""sum_list input"""
	return sum(lst)

def gen_artm_lst(num:int) -> list[int]:
	"""generates a arithmetic list of numbers """
	return [i + i for i in range(num)]

def get_artm_logic_lst(num:int) -> list[dict[str:int]]:
	"""calculates the logic of how the sum of arithmetic lists growing and retunrs a list of dicts"""
	res_lst = []
	for i in range(num):
		artm_lst = gen_artm_lst(num=i)
		sum = sum_list(lst=artm_lst)
		
		res_dict = pack_res_in_dict(i, artm_lst, sum)
		res_lst.append(res_dict)
	
	return res_lst
	
def pack_res_in_dict(num:int, artm_lst:list[int], sum:int) -> dict[str:int]:
	"""stores arguments in dictionary"""
	return {
	"i": num,
	"artm_lst": artm_lst,
	"sum": sum
	}

def get_range_of_nums():
	"""takes user input and turns it into an int"""
	input_num = int(input("Type in a range:"))
	
	
	
	return input_num

		
@DebugLog.raiser
def main():
	input_num = get_range_of_nums()
	
	armt_logic_list = get_artm_logic_lst(input_num)
	
	for i, dict in enumerate(armt_logic_list):
		
		print(f"{i+1}: num: {dict['i']}; \nartm_lst: {dict['artm_lst']}; \nsum: {dict['sum']}")
		
	

if __name__ == "__main__":
	main()














