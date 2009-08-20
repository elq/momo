#!/usr/bin/env python
# momo.py
#
# The start of scrappy, perhaps crappy monitoring system.
#
import os
import sys
import socket

class MomoParentScheduler(object):
	"""
	Who, What, Where, When, How.

	The parent scheduler is responsible for knowing the complete
	catalog of services checks and their schedules. It polls the
	database of services and their checks regularly and feeds
	services checks when they are needed to a child scheduler.
	
	It should feed the checks the children schedulers in a weighted
	least full algorithm.
	"""

class MomoChildScheduler(object):
	"""
	The child scheduler is responsible for managing a local FIFO
	queue of services that need to be checked.

	The parent scheduler feeds 1 -> N child schedulers with checks
	that need to be executed.
	"""

class MomoServiceBase(object):
	"""
	What
	"""

	def __init__(self, hostname=None, port=None, type=None):
		if hostname != None:
			self.hostname = hostname
		if port != None:
			self.port = port
		if type != None:
			self.type = type

class MomoActionBase(object):
	"""
	How
	"""

	def __init__(self, MomoService):
		if MomoService != None:
			self.MomoService = MomoService

	def poll(self):
		if self.MomoService.type == 'tcp':
			try:
				return self.tcp_poll(hostname=self.MomoService.hostname, port=self.MomoService.port)
			except socket.error:
				print "error connecting"

	def tcp_poll(self, hostname=None, port=None):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((hostname, port))
		s.close()


def main():
	Service = MomoServiceBase(hostname="localhost", port=999, type="tcp")
	Action = MomoActionBase(Service)
	Action.poll()

if __name__ == '__main__':
	main()
