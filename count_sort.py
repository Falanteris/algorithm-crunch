def count_sort(array):
	def count(num,array):
		return len([i for i in array if(i == num)])
	temp = 0;
	prev = 0;
	count_list = [i for i in range(max(array)+1)]
	count_array = list();
	for i in count_list:
		temp  = count(i,array)
		if(len(count_array) == 0):
			count_array.append(temp);
			prev = count_array[i]
			continue;
		count_array.append(temp+prev);
		prev = count_array[i];
	final_array = list(array)
	print(count_array)
	for i in array:
		print(i)
		pointer = count_array[i]
		print(pointer)
		final_array[pointer-1] = i;
		count_array[i]-=1
	return final_array;

if __name__ == '__main__':
	inp = [1,2,2,1]
	print("INPUT ARRAY: {}".format(inp)) 
	print(count_sort(inp))
