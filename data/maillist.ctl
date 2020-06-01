load data
infile 'maillist.csv'
insert into table mail
fields terminated by ','
trailing nullcols(
	title,
	category
)