# import sqlite3
#
# class super:
#     # common instance value
#     def __init__(self,db,csv=None):
#         connect sqlite3
#         self.conn
#         self.cursor
#         if csv:
#             read file ...
#             self.csvdata
#
# class sub(super):
#     # departual instance value
#     def __init__(self,db,csv=None):
#         super().__init__(db,csv)
#
#     use self.csvdata
#     def insert(self):
#
#     def delete(self):
#
#     ....