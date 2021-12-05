import controller
import psycopg2

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

if __name__ == "__main__":
    command = input("Enter command: ")
    controller.run(command)
