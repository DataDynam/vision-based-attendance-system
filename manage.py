#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Attendance_Tracking_System_Using_Computer_Vision.settings')
    try:
        from dj