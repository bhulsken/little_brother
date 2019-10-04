![LittleBrother-Logo](little_brother/static/icons/icon_baby-panda_128x128.png)

# Change History 

This document lists all changes of `LittleBrother` with the most recent changes at the top.

## Version 0.1 Revision 42 (October 5th, 2019)

*   Closes #8, see [here](https://github.com/marcus67/little_brother/issues/8)
*   Fix some minor code quality problems reported by Codacy 
*   Provide special builtin methods to RecurringTask to eliminate tuple handling

## Version 0.1 Revision 41 (June 20th, 2019)

*   Closes #7, see [here](https://github.com/marcus67/little_brother/issues/7) 
    (has actually already been taken care of in previous commits)

*   Closes #16, see [here](https://github.com/marcus67/little_brother/issues/16)

*   Introduce alembic for database initialization and migration

## Version 0.1 Revision 40 (June 9th, 2019)

*   Actually committed the Italian localization (files were missing, mea culpa) 
*   Corrected name of fourth popup tool in sample configuration files
*   Added YouTube presentation

## Version 0.1 Revision 39 (June 5th, 2019)

*   [Albano Battistella](https://github.com/albanobattistella) provided the Italian translation. Thanks! 
*   Fixed some typos in the README file.

## Version 0.1 Revision 38 (June 2nd, 2019)

*   Small changes in README.md and sample configuration file reflecting test installation 
    from scratch on Ubuntu 18.10.

## Version 0.1 Revision 37 (May 29th, 2019)

*   Prepare pybabel files for Italian

## Version 0.1 Revision 36 (May 29th, 2019)

*   Closes #51, see [here](https://github.com/marcus67/little_brother/issues/51)
*   Change defaults for database driver (to match pre-loaded PIP package for mysql)

## Version 0.1 Revision 35 (June 1st, 2019)

*   Closes #9, see [here](https://github.com/marcus67/little_brother/issues/9)
*   Closes #50, see [here](https://github.com/marcus67/little_brother/issues/50)
*   Improve test coverage.

## Version 0.1 Revision 34 (May 26th, 2019)

*   Closes #13, see [here](https://github.com/marcus67/little_brother/issues/13)
*   Improve test coverage.
*   Choose better colors grades for nested rows in admin and index pages

## Version 0.1 Revision 33 (May 11th, 2019)

*   Boost test coverage.
*   Several changes proposed by codacy.
*   Add `post_process` to class `configuration.ConfigModel`

## Version 0.1 Revision 32 (May 9th, 2019)

*   Several changes proposed by codacy.

## Version 0.1 Revision 31 (May 8th, 2019)

*   Closes #44, see [here](https://github.com/marcus67/little_brother/issues/44)
*   Add hyperlink to [Facebook page](https://www.facebook.com/littlebrotherdebian/)

## Version 0.1 Revision 30 (May 4th, 2019)

*   Closes #15, see [here](https://github.com/marcus67/little_brother/issues/15)
*   Several changes proposed by codacy.

## Version 0.1 Revision 29 (May 4th, 2019)

*   Closes #5, see [here](https://github.com/marcus67/little_brother/issues/5)
*   Closes #10, see [here](https://github.com/marcus67/little_brother/issues/10)
*   Closes #14, see [here](https://github.com/marcus67/little_brother/issues/10)
*   Round remaining play times to nearest minute in notifications.
*   Instantiate flask_wtf.FlaskForm instead of flask_wtf.Form (obsolete).
*   Several changes proposed by codacy.
  
## Version 0.1 Revision 28 (May 2nd, 2019)

*   Add code quality badge by codacy to README.md.
*   Make first improvements to code found by codacy.

## Version 0.1 Revision 27 (May 1st, 2019)

*   Closes #17, see [here](https://github.com/marcus67/little_brother/issues/17)
*   Closes #18, see [here](https://github.com/marcus67/little_brother/issues/18)
*   Closes #35, see [here](https://github.com/marcus67/little_brother/issues/35)
*   Closes #36, see [here](https://github.com/marcus67/little_brother/issues/36)
*   Improve test coverage of process_statistics.py.
*   Include requirement.txt to be scanned by snyk.io.

## Version 0.1 Revision 26 (April 29th, 2019)

*   Closes #6 (again), see [here](https://github.com/marcus67/little_brother/issues/6)
*   Closes #11, see [here](https://github.com/marcus67/little_brother/issues/11)

## Version 0.1 Revision 25 (April 27th, 2019)

*   Closes #6, see [here](https://github.com/marcus67/little_brother/issues/6)

## Version 0.1 Revision 24 (April 22nd, 2019)

*   Added first version of ARCHITECTURE.md.

## Version 0.1 Revision 23 (April 22nd, 2019)

*   Add screenshots to README.md.
*   Move "under construction" logo to `doc`.

## Version 0.1 Revision 22 (April 21st, 2019)

*   Add download logo to README.md.
*   Link both directories `release` and `master` at SourceForge.

## Version 0.1 Revision 21 (April 21st, 2019)

*   Add coverage logo to README.md. 
*   Add this CHANGES.md page.
*   Interpret predefined environment variables (e.g. CIRCLE_BRANCH).
*   Expand environment variables before calling scripts.
