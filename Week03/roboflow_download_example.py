from getpass import getpass
from roboflow import Roboflow

api_key = getpass("Roboflow API Key: ")

WORKSPACE = "YOUR_WORKSPACE"
PROJECT = "drink-can-detection"
VERSION = 1

rf = Roboflow(api_key=api_key)
project = rf.workspace(WORKSPACE).project(PROJECT)
dataset = project.version(VERSION).download("yolov8")

print("dataset location:", dataset.location)
