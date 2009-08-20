#!/usr/bin/env python
# momo.py

from Momo import Momo

def main():
	Service = Momo.ServiceBase(hostname="localhost", port=80, type="tcp")
	Action = Momo.ActionBase(Service)
	Action.poll()

if __name__ == '__main__':
	main()
