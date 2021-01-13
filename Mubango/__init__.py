from __future__ import absolute_import
import pymysql
from Mubango.celery_app import celery_app as app

pymysql.version_info = (1, 3, 13, "final", 0)
pymysql.install_as_MySQLdb()

__all__ = ["app"]
