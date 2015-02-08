#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys

if __name__ == '__main__':
	argvs = sys.argv
	argc = len(argvs)
	if '-h' in argvs:
		print 'cocoa 1.0.0'
		print '使用法:	cocoa [オプション]'
		print 'コマンド'
		print '-a - はぁ…ココアちゃん…！'
		print '-b - はぁ…ココアちゃん…！'
		print '-c - はぁ…ココアちゃん…！'
		print '-d - はぁ…ココアちゃん…！'
		print '-e - はぁ…ココアちゃん…！'
		print '-f - はぁ…ココアちゃん…！'
		print '-g - はぁ…ココアちゃん…！'
		print '-h - はぁ…ココアちゃん…？'
		print '-i - はぁ…ココアちゃん…！'
		print '-j - はぁ…ココアちゃん…！'
		print '-k - はぁ…ココアちゃん…！'
		print '-l - はぁ…ココアちゃん…！'
		print '-m - はぁ…ココアちゃん…！'
		print '-n - はぁ…ココアちゃん…！'
		print '-o - はぁ…ココアちゃん…！'
		print '-p - はぁ…ココアちゃん…！'
		print '-q - はぁ…ココアちゃん…！'
		print '-r - はぁ…ココアちゃん…！'
		print '-s - はぁ…ココアちゃん…！'
		print '-t - はぁ…ココアちゃん…！'
		print '-u - はぁ…ココアちゃん…！'
		print '-v - はぁ…ココアちゃん…！'
		print '-w - はぁ…ココアちゃん…！'
		print '-x - はぁ…ココアちゃん…！'
		print '-y - はぁ…ココアちゃん…！'
		print '-z - はぁ…ココアちゃん…！'
	elif '-cocoa' in argvs:
		cocoa = open('cocoaAA','r')
		print ''
		for line in cocoa:
			print line
		cocoa.close()
		
	else:
		print 'はぁ…ココアちゃん…！'
		
