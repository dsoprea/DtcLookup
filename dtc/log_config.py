from logging import getLogger, Formatter, FileHandler, DEBUG, WARNING
#from logging.handlers import SysLogHandler

default_logger = getLogger()
default_logger.setLevel(DEBUG)

log_format = 'DTC: %(name)-12s %(levelname)-7s %(message)s'
formatter = Formatter(log_format)

#log_syslog = SysLogHandler(facility=SysLogHandler.LOG_LOCAL0)
#log_syslog.setFormatter(formatter)
#default_logger.addHandler(log_syslog)

log_file = FileHandler('/tmp/dtc.log')
log_file.setFormatter(formatter)
#log_file.setLevel(DEBUG)
default_logger.addHandler(log_file)
