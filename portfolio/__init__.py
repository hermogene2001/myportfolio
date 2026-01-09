import os
try:
	import pymysql
	pymysql.install_as_MySQLdb()
except Exception:
	# If PyMySQL isn't installed or import fails, fall back silently to allow SQLite local development
	pass
