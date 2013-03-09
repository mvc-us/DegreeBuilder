drop table if exists courses;
create table courses (
  id integer primary key autoincrement,
  abbrv string not null,
  num string not null,
  title string not null,
  units real not null,
  pnp integer not null,
  technical integer not null
);
drop table if exists prereqs;
create table prereqs (
  courseid integer not null,
  prereqid integer not null,
  foreign key (courseid) references courses(id),
  foreign key (prereqid) references courses(id)
);
