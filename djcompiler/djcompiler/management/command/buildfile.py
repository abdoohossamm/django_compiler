from djcompiler.management.command import BaseCommand


class BuildFile(BaseCommand):
    compiler_config = """# Project details
project_name=DjCompiler
project_author=author
project_version=1.0.0
# Compiler data
build_directory=build
other_files_needed=manage.py .env
ignored_files=manage.py compiler.py
ignored_dirs=venv/ cython/ .git/ .idea/ build/ __pycache__/"""

    def write_compiler_settings(self):
        with open(".djcompiler", "w") as f:
            f.writelines(self.compiler_config)

    def execute(self):
        self.write_compiler_settings()
        return ".djcompiler settings file was generated successfully."
