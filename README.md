# php_mt_seed

​用于破解 PHP mt_rand() 随机数种子的工具。PHP 使用梅森旋转算法（Mersenne Twister）生成伪随机数，这个算法的输出完全由种子决定，同一个种子产生的随机数序列是固定的。只要知道任意一个 mt_rand() 的输出值，就能反推出种子，进而预测后续所有随机数的结果。工具的原理是暴力枚举所有可能的种子（0 到 2^32-1，约 43 亿种），对每个种子计算产生的随机数，与已知输出进行比对，找到匹配的种子后输出结果。

This tool cracks PHP mt_rand() seeds by brute-force. PHP uses the Mersenne Twister algorithm for pseudo-random number generation, where the output is entirely determined by the seed. Given any mt_rand() output, it enumerates all possible seeds (0 to 2^32-1, about 4.3 billion) to find the matching seed and predict subsequent random numbers.此工具通过暴力破解PHP mt_rand（）种子。PHP使用Mersenne Twister算法来生成伪随机数，其中输出完全由种子决定。给定任何mt_rand（）输出，它枚举所有可能的种子（0到2的32-1次方，约43亿），以找到匹配的种子并预测后续的随机数。

​	编译后运行 `./php_mt_seed <已知的随机数值>` 即可。比如页面显示 `Hint: 1219893521`，就运行 `./php_mt_seed 1219893521`，工具会输出种子值和后续的随机数序列。

​	Usage: `./php_mt_seed <known_random_value>`. For example, if the page shows `Hint: 1219893521`, run `./php_mt_seed 1219893521` to get the seed and predict the next values.

