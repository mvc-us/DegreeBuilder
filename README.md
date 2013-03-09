DegreeBuilder
=============

A 4 year schedule planner. Requires Python 2.7 and Flask.

Current Functionality:
Creates profile and generates 4-year plan based on profile attributes. Needs work on in numerous ways:
- Have Taken Classes be mapped from a form per semester to translate directly to the final graduation plan.
- Enlarge database with degree maps of all majors, full ap credit policies per college, full prereq lists (harder due to it not being easily accessible, needs to be crawled and filtered)
- Utilize wanted_courses, which lets the user specify courses he wants to take for sure and passes that to the algorithm as "set in stone".
- Expand functionality to all majors and streamline database/function calls.
- Implement Community College credit, Transfer credit, etc.
- Make UI prettier.
- For "broad" required courses such as humanities/electives/technical electives return a list of classes/descriptions that fit the requirement for user to pick

Future addons with improved algorithm(s):
- Double/Triple major, minors, etc
   - Ability to say take "x classes" to get a minor, double major, etc.
- Ability to weight classes or have users "rate and weight" classes which algorithm takes into account to spread workload across semesters
- Ability to graduate in less than 4-years (generate alternate schedules if user wants to graduate a semester/two/three/four, etc early?)

ASAP:
- Put major templates and requirements in database
- Implement wanted_courses
- Implement rough idea of course filling requirement (ie. HUMANITIES filling requirement)
  -Give Major class attributes of requirements such as lower_hss, ac_req, etc.