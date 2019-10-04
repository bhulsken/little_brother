# -*- coding: utf-8 -*-

#    Copyright (C) 2019  Marcus Rickert
#
#    See https://github.com/marcus67/little_brother
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from setuptools import setup

import little_brother.settings

setup_params = {
    # standard setup configuration

    "install_requires": [
        'alembic',
        'python_google_speak',
        'requests',
        'psutil',
        'python-dateutil',
        'sqlalchemy',
        'pymysql',
        'flask',
        'flask-login',
        'Flask-Babel',
        'Flask-Migrate',
        'python-base-app',
        'flask_helpers',
        'pyttsx3',
        'selenium'],

    "packages": ['little_brother', 'little_brother.test'],

    "include_package_data": True,

    "scripts": ["run_little_brother.py", "run_test_suite.py"],
    "long_description": "Tool to monitor usage time of users on Debian hosts and terminate processes if usage times "
                        "are exceeded.",

    # Target version to be used to upgrade the database
    "target_alembic_version": "647cf46033a9",

    # additional setup configuration used by CI stages

    # technical name used for e.g. directories, PIP-package, and users
    "create_user": True,
    "create_group": True,
    "user_group_mappings": [("little-brother", "audio")],
    "deploy_systemd_service": True,
    "deploy_sudoers_file": True,
    "contributing_setups": ["python_base_app", "flask_helpers"],
    "publish_debian_package": ["master", "release"],
    "debian_extra_files": [
        ("etc/minimal-slave.config", "etc/little-brother/minimal-slave.config"),
        ("etc/minimal-master.config", "etc/little-brother/minimal-master.config"),
        ("etc/multi-rule-master.config", "etc/little-brother/multi-rule-master.config"),
    ]

}
setup_params.update(little_brother.settings.settings)

if __name__ == '__main__':
    setup(**setup_params)
