import os 
from networksecurity.exception.exception import NetworkSecurityException
import sys
import subprocess

class S3sync:
    def sync_folder_to_s3(self,folder,aws_bucket_url):
        try:
            # Get the directory of this script
            script_dir = os.path.dirname(os.path.abspath(__file__))
            # Go up to project root
            project_root = os.path.dirname(os.path.dirname(script_dir))
            venv_scripts = os.path.join(project_root, ".venv", "Scripts")
            aws_cmd = os.path.join(venv_scripts, "aws")
            python_exe = os.path.join(venv_scripts, "python.exe")
            
            command = [python_exe, aws_cmd, "s3", "sync", folder, aws_bucket_url]
            result = subprocess.run(command, capture_output=True, text=True)
            if result.returncode != 0:
                raise Exception(f"AWS sync failed: {result.stderr}")
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def sync_flder_from_s3(self,folder,aws_bucket_url):
        try:
            # Get the directory of this script
            script_dir = os.path.dirname(os.path.abspath(__file__))
            # Go up to project root
            project_root = os.path.dirname(os.path.dirname(script_dir))
            venv_scripts = os.path.join(project_root, ".venv", "Scripts")
            aws_cmd = os.path.join(venv_scripts, "aws")
            python_exe = os.path.join(venv_scripts, "python.exe")
            
            command = [python_exe, aws_cmd, "s3", "sync", aws_bucket_url, folder]
            result = subprocess.run(command, capture_output=True, text=True)
            if result.returncode != 0:
                raise Exception(f"AWS sync failed: {result.stderr}")
        except Exception as e:
            raise NetworkSecurityException(e,sys)
                           