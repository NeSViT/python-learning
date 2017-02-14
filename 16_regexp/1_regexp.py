#!/usr/bin/env python

# Description: show how to match some fragment in a line without RegExp

line = "Jan 2 08:01:45 ubuntu sshd[30559]: Failed password for vnesterenko from 192.168.199.433 port 52536 ssh2"

# import module for working with RegExp
import re

# create object that equal to our search method in line
match = re.search('sshd', line)

# output will be like "<_sre.SRE_Match object at 0x7f22536ce648>" if matched 
print match

# find non-exist expression in variable line
match = re.search('hello', line)

# output will be "None" if not mached and string was not found
print match

# RegExp for searching in variable "line"
# Jan 2 08:01:45 ubuntu sshd[30559]: Failed password for vnesterenko from 192.168.199.433 port 52536 ssh2
# [A-Z][a-z]{2}\s\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2}\s\w*\ssshd\[\d*\]: Failed password for \w* from \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} port \d* ssh2
# better site with RegExp https://regex101.com

match = re.search('[A-Z][a-z]{2}\s\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2}\s\w*\ssshd\[\d*\]: Failed password for \w* from \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} port \d* ssh2', line)

print match
print match.group()

# another method for writing regexp
match = re.search('^(.*?)\s(\w+)\ssshd.*?Failed\spass.*?from\s(.*?)\sport.*$', line)
#                      ^      ^                                 ^
#                  group 1   group 2                           group 3
# 
# ^(.*?)\s(\w+)\ssshd.*?Failed\spass.*?from\s(.*?)\sport.*$
# 
# 
# ^ asserts position at start of the string
# 			1st Capturing Group (.*?)
# .*? matches any character (except for line terminators)
# *? Quantifier - Matches between zero and unlimited times, as few times as possible, expanding as needed lazy
# \s matches any whitespace character (equal to [\r\n\t\f\v ])
# 			2nd Capturing Group (\w+)
# \w+ matches any word character (equal to [a-zA-Z0-9_])
# + Quantifier - Matches between one and unlimited times, as many times as possible, giving back as needed (greedy)
# \s matches any whitespace character (equal to [\r\n\t\f\v ])
# sshd matches the characters sshd literally (case sensitive)
# .*? matches any character (except for line terminators)
# *? Quantifier - Matches between zero and unlimited times, as few times as possible, expanding as needed (lazy)
# Failed matches the characters Failed literally (case sensitive)
# \s matches any whitespace character (equal to [\r\n\t\f\v ])
# pass matches the characters pass literally (case sensitive)
# .*? matches any character (except for line terminators)
# from matches the characters from literally (case sensitive)
# \s matches any whitespace character (equal to [\r\n\t\f\v ])
# 
# 			3rd Capturing Group (.*?)
# \s matches any whitespace character (equal to [\r\n\t\f\v ])
# port matches the characters port literally (case sensitive)
# .* matches any character (except for line terminators)
# $ asserts position at the end of the string, or before the line terminator right at the end of the string (if any)
# Global pattern flags
# g modifier: global. All matches (don't return after first match)

print match 
print match.group()

# show groups 
print match.group(1)
print match.group(2)
print match.group(3)