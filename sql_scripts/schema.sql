drop table if exists users;
drop table if exists events;
drop table if exists attendance;

CREATE TABLE if not exists users (
  user_id int primary key not null AUTO_INCREMENT,
  name varchar (255) not null, 
  token varchar(100)
);

CREATE TABLE if not exists events (
  -- id integer primary key not null, 
  event_id int  primary key not null AUTO_INCREMENT,
  title varchar(255) not null,
  venue varchar(255),
  date_slot datetime not null,
  time_slot time not null,
  organiser varchar (255) not null,
  description varchar(255),
  status int not null,
  cur_attendance int ,
  qr_image text
);

CREATE TABLE if not exists attendance(
  user_id varchar(255) not null,
  event_id varchar(255) not null,
  user_status integer
);