#conding:utf8

from scrapy.cmdline import execute
import os
import sys

sys.path.append(os.getcwd())
#execute(['scrapy','crawl','qidian'])
execute(['scrapy','crawl','jobbole'])