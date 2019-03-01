# Sum All After Benchmarks

## With Lists, Arrays and Generators

generator, N = 4
-------------------------
0.0000010 | sum_first
0.0000014 | generator
0.0000030 | reversed_loop
0.0000096 | stuart
0.0000109 | stuart_two
0.0000157 | user2699


generator to List, N = 4
-------------------------
0.0000012 | sum_first
0.0000015 | generator
0.0000017 | reverse_sum
0.0000032 | reversed_loop
0.0000032 | josep_joestar
0.0000041 | reverse_sum
0.0000056 | stuart
0.0000061 | user2699
0.0000066 | stuart_two


generator to np.array, N = 4
-------------------------
0.0000071 | sum_first
0.0000075 | generator
0.0000075 | stuart_two
0.0000086 | stuart
0.0000137 | user2699
0.0000189 | reversed_loop


np.arange, N = 4
-------------------------
0.0000029 | stuart_two
0.0000032 | sum_first
0.0000036 | generator
0.0000039 | user2699
0.0000046 | stuart
0.0000072 | reversed_loop


list, N = 4
-------------------------
0.0003650 | stuart
0.0003767 | stuart_two
0.0003986 | generator
0.0004732 | user2699
0.0004878 | sum_first
0.0006498 | reverse_sum
0.0015482 | reverse_sum
0.0015797 | josep_joestar
0.0016560 | reversed_loop


np.array, N = 4
-------------------------
0.0003653 | stuart
0.0003654 | stuart_two
0.0003658 | user2699
0.0016395 | sum_first
0.0022938 | generator
0.0030003 | reversed_loop


generator, N = 500
-------------------------
0.0000563 | user2699
0.0000648 | reversed_loop
0.0001013 | generator
0.0001504 | stuart
0.0001628 | stuart_two
0.0001677 | sum_first


generator to List, N = 500
-------------------------
0.0000448 | user2699
0.0000659 | josep_joestar
0.0000671 | reversed_loop
0.0000671 | reverse_sum
0.0001087 | generator
0.0001138 | stuart
0.0001189 | stuart_two
0.0001498 | sum_first
0.0001812 | reverse_sum


generator to np.array, N = 500
-------------------------
0.0000589 | user2699
0.0001440 | stuart_two
0.0001534 | stuart
0.0001819 | reversed_loop
0.0003199 | generator
0.0004460 | sum_first


np.arange, N = 500
-------------------------
0.0000030 | user2699
0.0000107 | stuart_two
0.0000143 | stuart
0.0001143 | reversed_loop
0.0001803 | generator
0.0003067 | sum_first


list, N = 500
-------------------------
0.0006508 | reverse_sum
0.0006573 | user2699
0.0006638 | josep_joestar
0.0008975 | reversed_loop
0.0009321 | generator
0.0009472 | stuart
0.0009686 | stuart_two
0.0012499 | sum_first
0.0019545 | reverse_sum


np.array, N = 500
-------------------------
0.0009143 | user2699
0.0009332 | stuart_two
0.0009519 | stuart
0.0019055 | generator
0.0041857 | sum_first
0.0043007 | reversed_loop


generator, N = 2500
-------------------------
0.0002078 | generator
0.0003033 | stuart
0.0003119 | stuart_two
0.0006930 | sum_first
0.0007153 | user2699
0.0008592 | reversed_loop


generator to List, N = 2500
-------------------------
0.0002134 | stuart
0.0002227 | stuart_two
0.0002242 | generator
0.0005443 | user2699
0.0006631 | sum_first
0.0008440 | reverse_sum
0.0008699 | josep_joestar
0.0008920 | reversed_loop
0.0009189 | reverse_sum


generator to np.array, N = 2500
-------------------------
0.0002966 | stuart
0.0002972 | stuart_two
0.0006369 | generator
0.0007346 | user2699
0.0017304 | reversed_loop
0.0021942 | sum_first


np.arange, N = 2500
-------------------------
0.0000088 | stuart_two
0.0000104 | stuart
0.0000203 | user2699
0.0005032 | generator
0.0006041 | reversed_loop
0.0014530 | sum_first


list, N = 2500
-------------------------
0.0003781 | stuart
0.0006605 | stuart_two
0.0007037 | reversed_loop
0.0008088 | user2699
0.0009213 | sum_first
0.0009792 | generator
0.0015543 | reverse_sum
0.0015864 | josep_joestar
0.0016331 | reverse_sum


np.array, N = 2500
-------------------------
0.0003726 | user2699
0.0003761 | stuart
0.0009025 | stuart_two
0.0015748 | sum_first
0.0025459 | generator
0.0029954 | reversed_loop

## With N 

N = 4
--------------------------------
0.0000012 | sigma_range
0.0000017 | sigma_sum_after
0.0000062 | sigma_arange
0.0000062 | sigma_arange_two
0.0000066 | sigma_arange_three

N = 500
-------------------------------
0.0000215 | sigma_arange
0.0000265 | sigma_arange_two
0.0001557 | sigma_range
0.0003370 | sigma_sum_after
0.0006290 | sigma_arange_three

N = 2500
-------------------------------
0.0000367 | sigma_arange
0.0000374 | sigma_arange_two
0.0008236 | sigma_range
0.0016660 | sigma_sum_after
0.0031791 | sigma_arange_three

N = 10000
-------------------------------
0.0001055 | sigma_arange_two
0.0001057 | sigma_arange
0.0032350 | sigma_range
0.0071889 | sigma_sum_after
0.0124166 | sigma_arange_three
