#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 14:17:12 2020

@author: apple
"""

print ("~~~~DESTINASI PERCUTIAN di NEGERI SEMBILAN~~~~")
print("you are required to answer all the questions.")
print("you are required to answer with A NUMBER ONLY.")
bandar = 0
pantai = 0
hutan = 0
print("\n\n\nsoalan 1:")
print("\nwho are you going with?")
print("1.alone 2.family 3.friends")
#answer = str(input("answer:"))
answer = int(input("answer:"))

if answer == 1 :
  pantai = pantai + 1
  hutan = hutan + 1
  bandar = bandar + 1
elif answer == 2:
  pantai = pantai + 1
  hutan = hutan + 1
  bandar = bandar + 1
else : 
  pantai = pantai + 1
  hutan = hutan + 1 
  bandar = bandar + 1 

print("\nsoalan 2:")
print("\nchoose only one activity you would like to do.")
print("1.adventurous  2.go for a walk  3.regular")
answer = int(input("answer:"))
if answer == 1:
  hutan = hutan + 1
elif answer == 2:
  bandar = bandar + 1
else:
  pantai = pantai + 1

print ("\nsoalan 3:")
print("\npick a view to wake up to:")
print("1.lush greenery   2.beach  3.city scene ")
answer = int(input("answer:"))
if answer == 1:
  hutan = hutan + 1 
elif answer == 2 : 
  pantai = pantai + 1
else:
  bandar = bandar + 1

print (pantai,hutan,bandar)
 
if hutan >= 2:
	print("\n\n\nYour holiday destinations are as follows:")
	print("☞ TITI eco farm resort")
	print("☞ Kampung Pelegong Homestay")
	print("☞ Ulu Bendul Recreational Forest, Kuala Pilah")
elif pantai >= 2:
	print("\n\n\nYour destinations are as follows:")
	print("☞ Lexis Hibiscus, Port Dickson")
	print("☞ Baitul Hilal Complex, Teluk Kemang")
elif bandar >= 2:
	print ("\n\n\nYour destinations are as follows:")	
	print("☞ Nilai 3 Wholesale Center")	
	print("☞ Rembau Crystal")
	print("☞ State Museum Complex")

print("\n\n~~GO HAVE FUN OKAY :)~~")	
