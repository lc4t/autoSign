create database autoSign;
create user 'autosign'@'localhost' identified by 'autosign';
grant all on autoSign.* to 'autosign'@'localhost'
