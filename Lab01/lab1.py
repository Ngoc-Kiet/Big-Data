# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rDa2kYTUZHaYl-BenTxAJWpG0BankBBl
"""


a=[1,3,5,7]
print(a);

binhphuong=lambda x: x**2
print(binhphuong(3));

pip install pyspark

import pyspark

from pyspark import SparkConf , SparkContext
import collections

conf= SparkConf().setMaster("local").setAppName("word couting")
sc= SparkContext.getOrCreate(conf=conf)

text="to be or not to be".split()
rdd=sc.parallelize(text)
counts= rdd.map(lambda word:(word,1))
print(counts.collect())

rsd=counts.reduceByKey(lambda x,y: x+y)

"""# M?c m?i

# M?c m?i
"""